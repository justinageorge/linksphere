
from django.contrib import admin
from django.urls import path
from socialapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="register"),
    path('login/',views. SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("logout/",views.SignOutView.as_view(),name="signout"),
    # path("loginValid/",views.LoginController.as_view(),name="loginvalid")
    
]
