from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View

from MySite.models import Person, Budget, Expense


# Create your views here.
class LoginView(View):
    template_name = "mysite/login.html"

    def get(self, request):
        # Go to the register page
        return render(request, self.template_name)

    def post(self, request):
        # Check if form is submitting
        if request.method == "POST":
            # Collect inputs
            username = request.POST.get("username").strip()
            password = request.POST.get("password")

            # Authenticate user
            user = authenticate(username=username, password=password)

            # Check if user exist
            if user is not None:
                # Login user
                login(request, user)
                # Redirect to learning page
                return HttpResponseRedirect(reverse("MySite:home"))
            else:
                # Send error message
                messages.error(request, "Invalid credentials")
                # Redirect to login page
                return HttpResponseRedirect(reverse("MySite:login"))


class RegisterView(View):

    def post(self, request):
        # Check if form is submitting
        if request.method == "POST":
            # Collect inputs
            full_name = request.POST.get("full_name").strip().capitalize()
            username = request.POST.get("username").strip()
            email = request.POST.get("email").strip()
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password").strip()

            # Check if user with username already exists
            if not User.objects.filter(username=username).exists():
                if password == confirm_password:
                    # Create user and person
                    user = User.objects.create_user(username=username, password=password)
                    Person.objects.create(user=user, full_name=full_name, username=username, email=email)
                    # Send success message
                    messages.success(request, "Registration successful. Please login")
                    # Redirect to login page
                    return HttpResponseRedirect(reverse("MySite:login"))
                else:
                    # Send error message
                    messages.error(request, "Password does not match")
                    # Redirect back to register page
                    return HttpResponseRedirect(reverse("MySite:login"))
            else:
                # Send error message
                messages.error(request, "Username already exists")
                # Redirect back to register page
                return HttpResponseRedirect(reverse("MySite:login"))


class HomeView(View):
    template_name = "mysite/home.html"

    @method_decorator(login_required)
    def get(self, request):
        person = Person.objects.get(user=request.user)
        return render(request, self.template_name, {'person': person})

    @method_decorator(login_required)
    def post(self, request):
        person = Person.objects.get(user=request.user)
        # Check if form is submitting
        if request.method == "POST":
            # Collect inputs
            budget_title = request.POST.get("budget_title").strip().upper()
            budget_income = request.POST.get("budget_income").strip()
            all_expenses = request.POST.get("all_expenses")
            all_costs = request.POST.get("all_costs")
            total_cost = request.POST.get("total_cost")

            budget_income = float(budget_income)
            total_cost = float(total_cost)

            budget = Budget.objects.create(person=person, title=budget_title, income=budget_income,
                                           total_cost=total_cost, date=timezone.now())

            all_expenses = all_expenses.split(",")
            all_costs = all_costs.split(",")
            zipped_expenses = zip(all_expenses, all_costs)

            for title, cost in zipped_expenses:
                title = title.strip()
                cost = cost.strip()
                if title != "" or cost != "":
                    cost = float(cost)
                    expense = Expense.objects.create(person=person, title=title, cost=cost, date=timezone.now())
                    budget.expenses.add(expense)
                    budget.save()

            return HttpResponseRedirect(reverse("MySite:reports"))


class ReportsView(View):
    template_name = "mysite/reports.html"

    @method_decorator(login_required)
    def get(self, request):
        person = Person.objects.get(user=request.user)
        budgets = Budget.objects.filter(person=person)
        return render(request, self.template_name, {'budgets': budgets, 'person':person})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("MySite:login"))
