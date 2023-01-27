from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AddtaskApp import views

urlpatterns = [
    path('addtask/', views.AddtaskList.as_view()),
    path('addtask/<int:pk>/', views.AddtaskDetail.as_view()),
    path('assigntask/', views.AssigntaskList.as_view()),
    path('assigntask/<int:pk>/', views.AssigntaskDetail.as_view()),
]