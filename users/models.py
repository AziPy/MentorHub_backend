from django.db import models


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ['user', 'course']
