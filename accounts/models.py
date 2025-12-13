from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"

    def __str__(self):
        return self.user.username


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "عناوين العملاء"

    def __str__(self):
        return f"{self.city} - {self.district}"
