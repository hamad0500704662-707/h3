from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer",
        verbose_name=_("الحساب")
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("رقم الجوال")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )

    class Meta:
        verbose_name = _("عميل")
        verbose_name_plural = _("العملاء")

    def __str__(self):
        return self.user.username


class Address(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("العميل")
    )
    city = models.CharField(
        max_length=100,
        verbose_name=_("المدينة")
    )
    district = models.CharField(
        max_length=100,
        verbose_name=_("الحي")
    )
    details = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("تفاصيل العنوان")
    )

    class Meta:
        verbose_name = _("عنوان")
        verbose_name_plural = _("عناوين العملاء")

    def __str__(self):
        return f"{self.city} - {self.district}"
