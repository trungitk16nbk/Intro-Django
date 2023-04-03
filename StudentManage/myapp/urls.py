from django.urls import path 
from . import views

urlpatterns = [
    path('get_student', views.StudentView.as_view()),
    path('add_student', views.StudentView.as_view()),
    path('update_student', views.StudentView.as_view()),
    path('delete_student', views.StudentView.as_view()),
]
