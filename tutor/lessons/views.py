# Create your views here.
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Lesson


class IndexView(generic.TemplateView):
    template_name = 'lessons/index.html'


class LessonCreateView(CreateView):
    model = Lesson
    template_name = "lessons/lesson_create.html"
    fields = ['student', 'date', 'duration_in_hours', 'topic', 'report', 'profile']

    def get_success_url(self):
        return reverse('lessons:view_lesson', kwargs={'pk': self.object.id})

class LessonListView(generic.ListView):
    model = Lesson
    context_object_name = 'lessons'
    queryset = Lesson.objects.all()


class LessonDetailView(generic.DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
