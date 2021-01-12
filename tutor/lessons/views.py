# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lesson, Student, Invoice


class IndexView(generic.TemplateView):
    template_name = 'lessons/index.html'


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

        return self.get(self, request, *args, **kwargs)


class LessonListView(LoginRequiredMixin, generic.ListView):
    model = Lesson
    context_object_name = 'lessons'
    queryset = Lesson.objects.all()


class LessonDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lesson


class InvoiceCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "invoices/invoice_create.html"

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        print(data)
        
        # lesson = Lesson()
        # lesson.student = Student.objects.get(pk=data["student"])
        # lesson.date = data["date"]
        # lesson.duration_in_hours = data["duration"]
        # lesson.topic = data["topic"]
        # lesson.report = data["report"]
        # lesson.profile = request.user.profile
        # lesson.save()

        return self.get(self, request, *args, **kwargs)


class InvoiceListView(LoginRequiredMixin, generic.ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'invoices'
    queryset = Invoice.objects.all()


class InvoiceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Invoice
    template_name = "invoices/invoice_detail.html"



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
