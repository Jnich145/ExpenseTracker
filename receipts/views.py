from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required

@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts" : receipts,
    }
    return render(request, "receipts/receipt_list.html", context)
