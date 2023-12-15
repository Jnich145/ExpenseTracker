from django import forms 
from .models import Receipt

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            'vendor',
            'total',
            'tax',
            'date',
            'category',
            'account'
        ]
