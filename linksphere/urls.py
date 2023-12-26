
from django.contrib import admin
from django.urls import path
from socialapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="register"),
    path('',views. SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("logout/",views.SignOutView.as_view(),name="signout"),
    path("profiles/<int:pk>/change",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("profiles/<int:pk>",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profiles/all",views.ProfileListView.as_view(),name="profile_list"),
    path("profiles/<int:pk>/follow",views.FollowView.as_view(),name="follow"),
    path("posts/<int:pk>/like",views.PostLikeView.as_view(),name="like"),
    path("posts/<int:pk>/comments/add",views.CommentView.as_view(),name="comment"),
    path("profile/<int:pk>/block",views.ProfileBlockView.as_view(),name="block"),
    path("sories/add",views.StorieCreateView.as_view(),name="story")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)