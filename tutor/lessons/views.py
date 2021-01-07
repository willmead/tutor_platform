# Create your views here.
from django.views import generic

# from .models import Question, Answer


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})


class IndexView(generic.TemplateView):
    template_name = 'lessons/index.html'


# class AboutView(generic.TemplateView):
#     template_name = 'questions/about.html'
