from datetime import date
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Sum

from .models import Lesson, Student, Invoice, Group


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'lessons/index.html'
    context_object_name = "context"

    def get_total_hours(self):
        return sum([lesson.duration_in_hours for lesson in Lesson.objects.all()])

    def get_total_earned(self):
        return sum([lesson.duration_in_hours * lesson.student.rate_per_hour for lesson in Lesson.objects.all()])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'hours_taught': self.get_total_hours()})
        context.update({'total_earned': self.get_total_earned()})
        return context


class LessonCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "lessons/lesson_create.html"

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        lesson = Lesson()
        lesson.student = Student.objects.get(pk=data["student"])
        lesson.date = data["date"]
        lesson.duration_in_hours = data["duration"]
        lesson.topic = data["topic"]
        lesson.report = data["report"]
        lesson.profile = request.user.profile
        lesson.save()

        # return self.get(self, request, *args, **kwargs)
        return redirect('lessons:view_lessons')


class LessonListView(LoginRequiredMixin, generic.ListView):
    model = Lesson
    template_name = "lessons/lesson_list.html"
    context_object_name = 'lessons'
    queryset = Lesson.objects.all()


class LessonDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lesson
    template_name = "lessons/lesson_detail.html"


class InvoiceCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "invoices/invoice_create.html"

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        print(data)

        students = Group.objects.get(pk=data["group"]).students.all()
        lessons = []
        for student in students:
            for lesson in student.lesson_set.all():
                if not lesson.is_invoiced:
                    lesson.is_invoiced = True
                    lesson.save()
                    lessons.append(lesson)

        invoice = Invoice()
        invoice.date = date.today()
        invoice.profile = request.user.profile
        invoice.group = Group.objects.get(pk=data["group"])
        invoice.save()
        invoice.lessons.set(lessons)
        invoice.save()

        return self.get(self, request, *args, **kwargs)


class InvoiceListView(LoginRequiredMixin, generic.ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'invoices'
    queryset = Invoice.objects.all()


class InvoiceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Invoice
    template_name = "invoices/invoice_detail.html"


class InvoiceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Invoice
    success_url = ""
