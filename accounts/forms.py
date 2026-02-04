from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'bio',                  # ← add this
            'profile_picture',      # ← add this
        )

    # Optional: Make bio a textarea and add some nice widgets/help text
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us a bit about yourself...'}),
        required=False,
        help_text='Optional: Share something fun about you!',
    )

    profile_picture = forms.ImageField(
        required=False,
        help_text='Optional: Upload a profile picture (jpg/png)',
    )