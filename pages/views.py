
from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from .sendEmail import send_email
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        if username and email:
            if not Users.objects.filter(email=email).exists():
                users = Users.objects.create(username=username, email=email)
                users.save()
                messages.success(request, "تم اضافتك الى السحب بنجاح")
            else:
                messages.error(request, "البريد الالكتروني موجود من قبل في السحب")
        else:
            messages.error(request, "خطاء في المدخلات")
    return render(request, "pages/index.html")


def send(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            text = request.POST["texts"]
            users = Users.objects.all()
            for item in users:
                username = item.username
                email = item.email
                try:
                    send_email(email, username, text)
                except:
                    pass
            messages.success(request, "تم ارسال لجميع المستخدمين")
        return render(request, "pages/send.html")
    else:
        return redirect("index")