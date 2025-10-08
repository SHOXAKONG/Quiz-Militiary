from django.db import models


class ConsultationMethod(models.TextChoices):
    OFFICE = "office", "В офисе"
    PHONE = "phone", "По телефону"
    WHATSAPP = "whatsapp", "WhatsApp"
    HOME = "home", "Выезд на дом"


class CaseType(models.TextChoices):
    SERVICE = "service", "Прохождение службы"
    BENEFITS = "benefits", "Военные льготы"
    CONTRACT = "contract", "Контрактная служба"
    DISMISSAL = "dismissal", "Увольнение из армии"
    OTHER = "other", "Другое"


class QuizResponse(models.Model):
    case_type = models.CharField(max_length=50, choices=CaseType.choices)
    details = models.TextField()
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    consultation_method = models.CharField(max_length=20, choices=ConsultationMethod.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_case_type_display()})"
