from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MilitaryQuizForm
import requests
from decouple import config

# Bitrix webhook base URL from .env
BITRIX_BASE_URL = config("WEBHOOK_URL")


def send_to_bitrix(title, name, phone, details, consultation_method):
    """Send the form data to Bitrix24 CRM as a new lead."""
    payload = {
        "fields": {
            "TITLE": title,
            "NAME": name,
            "PHONE": [{"VALUE": phone, "VALUE_TYPE": "WORK"}],
            "COMMENTS": f"{details}\nСпособ консультации: {consultation_method}",
        }
    }

    try:
        response = requests.post(f"{BITRIX_BASE_URL}crm.lead.add.json", json=payload, timeout=10)
        print("Bitrix response:", response.json())
    except Exception as e:
        print("Ошибка Bitrix24:", e)


def home(request):
    """Landing page with intro text and navigation."""
    return render(request, "home.html")


def quiz_view(request):
    if request.method == "POST":
        form = MilitaryQuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()

            # Send the data to Bitrix24
            send_to_bitrix(
                title=f"Военное дело ({quiz.get_case_type_display()})",
                name=quiz.full_name,
                phone=quiz.phone,
                details=quiz.details,
                consultation_method=quiz.get_consultation_method_display(),
            )

            messages.success(request, "Спасибо! Мы скоро с вами свяжемся.")
            return redirect("quiz-success")
    else:
        form = MilitaryQuizForm()

    return render(
        request,
        "index.html",
        {
            "form": form,
            "title": "Военные дела",
            "subtitle": "Наши юристы помогут вам разобраться в сложных ситуациях, связанных с военной службой, льготами и контрактной службой.",
        },
    )


def quiz_success(request):
    """Success page after form submission."""
    return render(request, "success.html")
