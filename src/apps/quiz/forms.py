from django import forms
from .models import QuizResponse


class MilitaryQuizForm(forms.ModelForm):
    class Meta:
        model = QuizResponse
        fields = ["case_type", "details", "full_name", "phone", "consultation_method"]

        labels = {
            "case_type": "Тип военного дела",
            "details": "Какие-либо действия самостоятельно предпринимали?",
            "full_name": "Полное имя",
            "phone": "Телефон",
            "consultation_method": "Как хотите получить консультацию?",
        }

        widgets = {
            "case_type": forms.Select(
                attrs={"class": "form-select", "placeholder": "Выберите тип дела"}
            ),
            "details": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Опишите вашу ситуацию...",
                }
            ),
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите ваше имя"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите номер телефона"}
            ),
            "consultation_method": forms.Select(
                attrs={"class": "form-select"}
            ),
        }
