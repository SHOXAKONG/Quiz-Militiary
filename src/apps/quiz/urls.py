from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("quiz/family/", views.family_quiz, name="family-quiz"),
    path("quiz/military/", views.military_quiz, name="military-quiz"),
    path("quiz/success/", views.quiz_success, name="quiz-success"),
]
