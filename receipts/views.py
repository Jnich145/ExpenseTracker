from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required
from .forms import ReceiptForm, ExpenseCategoryForm

@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts" : receipts,
    }
    return render(request, "receipts/receipt_list.html", context)

@login_required
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()
        context = {
            'form': form
        }

    return render(request, 'receipts/create_receipt.html', context)

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)

    context = {
        'categories': categories
        }
    return render(request, "receipts/category_list.html", context)

@login_required
def accounts_list(request):
    accounts = Account.objects.filter(owner=request.user)

    context = {
    'accounts': accounts
    }
    return render(request, "receipts/accounts_list.html", context)

@login_required
def create_category(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense_category = form.save()
            expense_category.owner = request.user
            expense_category.save()
            return redirect('category_list')
    else:
        form = ExpenseCategoryForm()

    context = {
        "form": form
    }
    return render(request, 'receipts/create_category.html', context)
