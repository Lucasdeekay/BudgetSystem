from django.contrib import admin

from MySite.models import Person, Budget, Expense


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'username', 'email')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('person', 'title', 'cost', 'date')


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('person', 'title', 'income', 'total_cost', 'date')


admin.site.register(Person, PersonAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)