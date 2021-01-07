from django.urls import path

from . import views

app_name = 'lessons'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('about/', views.AboutView.as_view(), name='about'),
    # path('questions/<str:subject>/<str:topic>/',
    #      views.QuestionsView.as_view(),
    #      name='questions'),
    # path('register/', views.register, name='register'),
]
