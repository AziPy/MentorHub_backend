from django.db import models

class Order(models.Model):
    amount_usd = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
