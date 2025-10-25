from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=[('course', 'Course'), ('mentor', 'Mentor')])
    item_id = models.UUIDField()  # ID курса или ментора
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'item_type', 'item_id']