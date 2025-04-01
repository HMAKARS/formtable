from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_view, name='survey'),
    path('thanks/', views.thanks_view, name='thanks'),
]
