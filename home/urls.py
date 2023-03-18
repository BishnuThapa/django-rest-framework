
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.post_student, name='post-student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
]
