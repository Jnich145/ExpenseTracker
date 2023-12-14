from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt


# Register your models here.
@admin.register(ExpenseCategory)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner"
    ]

@admin.register(Account)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner"
    ]

@admin.register(Receipt)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "vendor",
        "total",
        "tax",
        "date",
        "category",
        "account",
        "purchaser"
    ]


# Register your models here.
