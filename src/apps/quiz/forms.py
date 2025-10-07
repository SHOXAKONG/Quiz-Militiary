from django import forms
from .models import QuizResponse


class BaseQuizForm(forms.ModelForm):
    class Meta:
        model = QuizResponse
        fields = [
            "full_name",
            "phone",
            "email",
            "question_1",
            "question_2",
            "question_3",
            "question_4",
        ]
        labels = {
            "full_name": "Полное имя",
            "phone": "Номер телефона",
            "email": "Эл. почта (необязательно)",
            "question_1": "Опишите вашу ситуацию",
            "question_2": "Обращались ли вы раньше к юристу?",
            "question_3": "Когда возникла проблема?",
            "question_4": "Дополнительные детали",
        }
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите ваше имя"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+7..." }),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "example@gmail.com"}),
            "question_1": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "question_2": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "question_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Например: месяц назад"}),
            "question_4": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


# class FamilyQuizForm(BaseQuizForm):
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.case_type = "family"
#         if commit:
#             instance.save()
#         return instance


class MilitaryQuizForm(BaseQuizForm):
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.case_type = "military"
        if commit:
            instance.save()
        return instance
