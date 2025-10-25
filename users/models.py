from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} → {self.mentor} ({self.rating})"



