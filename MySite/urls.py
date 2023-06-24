from django.contrib.auth.views import LogoutView
from django.urls import path

from MySite.views import LoginView, RegisterView, HomeView, ReportsView

app_name = "MySite"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("home", HomeView.as_view(), name="home"),
    path("reports", ReportsView.as_view(), name="reports"),
    path("logout", LogoutView.as_view(), name="login"),
]
