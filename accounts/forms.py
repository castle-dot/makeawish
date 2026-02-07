from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "bio", "profile_picture_url")
    
    profile_picture_url = forms.URLField(
        required=False,
        label="Profile Picture Link",
        help_text="Optional: Paste a direct link to an image (e.g. https://i.imgur.com/abc123.jpg). No upload needed."
    )
    # Optional: Make bio a textarea and add some nice widgets/help text
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us a bit about yourself...'}),
        required=False,
        help_text='Optional: Share something fun about you!',
    )

    profile_picture_url = forms.URLField(
        required=False,
        help_text="Optional: Direct link to your profile picture (jpg/png)"
    )