from django.shortcuts import render
from .models import Product


def home(request):
    """
    الصفحة الرئيسية — عرض المنتجات في home.html
    """
    products = Product.objects.all().order_by("-id")  # ترتيب من الأحدث للأقدم
    return render(request, "home.html", {"products": products})


def index(request):
    """
    صفحة عرض جميع المنتجات في products/index.html
    """
    products = Product.objects.all().order_by("-id")  # ترتيب من الأحدث إلى الأقدم
    return render(request, "products/index.html", {"products": products})
