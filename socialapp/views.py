from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView, View
from django.contrib.auth import authenticate, login, logout
from socialapp.forms import RegistrationForm, LoginForm
from django.urls import reverse


class SignUpView(CreateView):
    template_name = "register.html"
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("signin")

    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("register")
    #     else:
    #         return render(request,"register.html",{"form":form})


class SignInView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse("index")

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user_object = authenticate(request, username=uname, password=pwd)
            if user_object:
                login(request, user_object)
                print("success")
                return redirect("index")
        print("fail")
        return render(request, "login.html", {"form": form})


class IndexView(TemplateView):
    template_name = "index.html"


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class LoginController(FormView):
    print("works")
