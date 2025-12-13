from django.contrib import admin
from .models import Order
from django.utils.translation import gettext_lazy as _

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "phone", "total_price", "status", "created_at")
    search_fields = ("customer_name", "phone", "address")
    list_filter = ("status",)

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
