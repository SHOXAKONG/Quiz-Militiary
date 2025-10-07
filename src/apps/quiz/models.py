from django.db import models
import uuid

class QuizResponse(models.Model):
    CASE_TYPES = [
        ('family', 'Семейное дело'),
        ('military', 'Военное дело'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    case_type = models.CharField(max_length=50, choices=CASE_TYPES)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    question_1 = models.TextField(blank=True, null=True)  # Describe situation
    question_2 = models.TextField(blank=True, null=True)  # Have you contacted a lawyer before?
    question_3 = models.CharField(max_length=100, blank=True, null=True)  # When did the issue arise?
    question_4 = models.TextField(blank=True, null=True)  # Additional details

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_case_type_display()})"
