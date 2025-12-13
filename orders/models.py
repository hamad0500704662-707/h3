from django.db import models
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    customer_name = models.CharField(_("اسم العميل"), max_length=255)
    phone = models.CharField(_("رقم الجوال"), max_length=20)
    address = models.CharField(_("العنوان"), max_length=255)
    total_price = models.DecimalField(_("إجمالي السعر"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)
    status = models.CharField(
        _("حالة الطلب"),
        max_length=50,
        choices=[
            ("pending", _("قيد المعالجة")),
            ("shipped", _("تم الشحن")),
            ("delivered", _("تم التسليم")),
            ("canceled", _("ملغي")),
        ],
        default="pending",
    )

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")

    def __str__(self):
        return f"{self.customer_name} - {self.total_price}"
