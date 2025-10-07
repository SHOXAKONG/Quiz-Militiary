from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MilitaryQuizForm
import requests
from decouple import config

BITRIX_BASE_URL = config("WEBHOOK_URL")


def home(request):
    return render(request, "home.html")


def send_to_bitrix(quiz):
    comments = f"""
Тип дела: {quiz.get_case_type_display()}
1. Опишите ситуацию: {quiz.question_1}
2. Обращались ли к юристу: {quiz.question_2}
3. Когда возникла проблема: {quiz.question_3}
4. Дополнительно: {quiz.question_4}
"""
    payload = {
        "fields": {
            "TITLE": f"Заявка ({quiz.get_case_type_display()})",
            "NAME": quiz.full_name,
            "PHONE": [{"VALUE": quiz.phone, "VALUE_TYPE": "WORK"}],
            "EMAIL": [{"VALUE": quiz.email or '', "VALUE_TYPE": "WORK"}],
            "COMMENTS": comments,
        }
    }
    try:
        r = requests.post(f"{BITRIX_BASE_URL}crm.lead.add.json", json=payload, timeout=10)
        print("Bitrix response:", r.json())
    except Exception as e:
        print("Ошибка Bitrix24:", e)


def quiz_view(request, form_class, title):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            quiz = form.save()
            send_to_bitrix(quiz)
            messages.success(request, "Спасибо! Мы скоро с вами свяжемся.")
            return redirect("quiz-success")
    else:
        form = form_class()
    return render(request, "index.html", {"form": form, "title": title})


# def family_quiz(request):
#     return quiz_view(request, FamilyQuizForm, "Семейные дела")


def military_quiz(request):
    return quiz_view(request, MilitaryQuizForm, "Военные дела")


def quiz_success(request):
    return render(request, "success.html")
