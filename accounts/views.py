from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer


# =====================================================
# 🟦 إنشاء حساب جديد (Register)
# =====================================================
def register_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        # التحقق من الحقول
        if not username or not phone or not password:
            messages.error(request, "الرجاء تعبئة جميع الحقول ❌")
            return redirect("register")

        # التحقق من اسم المستخدم
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا ❌")
            return redirect("register")

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # إنشاء العميل
        Customer.objects.create(
            user=user,
            phone=phone
        )

        messages.success(request, "تم إنشاء الحساب بنجاح ✔")
        return redirect("login")

    return render(request, "accounts-te/register.html")



# =====================================================
# 🟦 تسجيل الدخول (Login)
# =====================================================
def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول ✔")
            return redirect("home")   # الرجوع للصفحة الرئيسية
        else:
            messages.error(request, "بيانات غير صحيحة ❌")
            return redirect("login")

    return render(request, "accounts-te/login.html")



# =====================================================
# 🟦 تسجيل الخروج (Logout)
# =====================================================
def logout_view(request):
    logout(request)                       # إزالة الجلسة بالكامل
    messages.success(request, "تم تسجيل الخروج بنجاح ✔")
    return redirect("home")               # ارجاع المستخدم للصفحة الرئيسية
