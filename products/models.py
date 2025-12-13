from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        _("اسم المنتج"),
        max_length=255
    )
    price = models.DecimalField(
        _("السعر"),
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField(
        _("الوصف"),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        _("تاريخ الإضافة"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")

    def __str__(self):
        return self.name
