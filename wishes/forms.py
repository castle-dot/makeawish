from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['title', 'description', 'phone_number', 'bank_account', 'bank_name'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'I need money holmes:)'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'phone_number': forms.TextInput(attrs={'placeholder': '0912345678 or +2519...'}),
            'bank_account': forms.TextInput(attrs={'placeholder': 'Account number'}),
        }