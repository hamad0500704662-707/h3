from django.db import models
from accounts.models import Customer
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المراجعة'),
        ('paid', 'تم الدفع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
        ('canceled', 'ملغي'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    # 🔵 الحقل المطلوب لحل الخطأ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id}"

    @property
    def total_price(self):
        return sum(item.total for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
             
    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    @property
    def total(self):
        return self.product.price * self.quantity
