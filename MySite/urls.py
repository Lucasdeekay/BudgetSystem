from django.contrib.auth.views import LogoutView
from django.urls import path

from MySite import views
from MySite.views import LoginView, RegisterView, HomeView, ReportsView

app_name = "MySite"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("home", HomeView.as_view(), name="home"),
    path("reports", ReportsView.as_view(), name="reports"),
    path("logout", views.log_out, name="logout"),
]
