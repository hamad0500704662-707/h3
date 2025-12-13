from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ----------------------------
    # 🔵 تضمين روابط التطبيقات الجديدة
    # ----------------------------
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]
