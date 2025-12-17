from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # الأعمدة الظاهرة في لوحة التحكم
    list_display = ("id", "name", "price", "stock", "created_at", "show_image")

    # الفلاتر الجانبية
    list_filter = ("created_at", "price", "stock")

    # البحث
    search_fields = ("name", "description")

    # ترتيب الحقول عند الإضافة أو التعديل
    fields = (
        "name",
        "price",
        "stock",
        "description",
        "image",
    )

    # عرض الصورة داخل لوحة التحكم
    def show_image(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='60' height='60' style='border-radius:6px;' />"
        return "لا يوجد صورة"
    show_image.allow_tags = True
    show_image.short_description = "الصورة"
