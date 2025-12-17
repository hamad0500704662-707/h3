from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.IntegerField(default=0, verbose_name="الكمية المتوفرة")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
