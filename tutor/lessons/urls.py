from django.urls import path

from . import views

app_name = 'lessons'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('lessons/', views.LessonListView.as_view(), name='view_lessons'),
    path('lesson/add', views.LessonCreateView.as_view(), name='add_lesson'),
    path('lessons/<int:pk>', views.LessonDetailView.as_view(), name='view_lesson'),
    path('invoices/', views.InvoiceListView.as_view(), name='view_invoices'),
    path('invoices/<int:pk>', views.InvoiceDetailView.as_view(), name="view_invoice")
]
