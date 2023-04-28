
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('get-book/', views.get_book, name='get-book'),
    # path('student/', views.post_student, name='post-student'),
    # path('update-student/<int:id>/', views.udpate_student, name='update-student'),
    # path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
    path('student/', views.StudentAPI.as_view()),
    path('student/<int:id>', views.StudentAPI.as_view())
]
