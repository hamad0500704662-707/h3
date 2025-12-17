from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# استدعاء الصفحة الرئيسية من products
from products.views import home

urlpatterns = [

    # ===============================
    # 🔵 لوحة التحكم (Django Admin)
    # ===============================
    path('admin/', admin.site.urls),

    # ===============================
    # 🔵 الصفحة الرئيسية (Home)
    # ===============================
    path('', home, name='home'),

    # ===============================
    # 🔵 روابط التطبيقات (Accounts / Products / Orders)
    # ===============================
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]

# ===============================
# 🔵 دعم ملفات Media & Static أثناء التطوير
# ===============================
if settings.DEBUG:

    # ملفات Media (الصور / الملفات المرفوعة)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    # ملفات Static (CSS / JS / صور ثابتة)
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
