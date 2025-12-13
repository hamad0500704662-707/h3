from django.http import HttpResponse

def index(request):
    return HttpResponse("صفحة المنتجات تعمل ✔")
