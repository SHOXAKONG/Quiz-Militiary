from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/military/", views.quiz_view, name="military-quiz"),
    path("quiz/success/", views.quiz_success, name="quiz-success"),
]
