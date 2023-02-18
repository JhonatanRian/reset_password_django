from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm#, PasswordResetForm
# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = User.objects.filter(email=email).first()

            if user:
                user = authenticate(username=user.username, password=password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Usuario ou senha inválidos'
        else:
            msg = 'Erro ao logar'

    return render(request, "accounts/sign-in.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html", {"msg": "Olá humano"})


# class PasswordResetView(auth_views.PasswordResetView):
#     # form_class = PasswordResetForm
#     template_name = "password/password-reset.html"
#     email_template_name = "password_reset_email.txt"
