from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from wishes.models import Wish
from .forms import CommentForm

@login_required
def add_comment(request, wish_id):
    wish = get_object_or_404(Wish, pk=wish_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wish = wish
            comment.user = request.user
            comment.save()
            messages.success(request, "Your comment was posted!")
            return redirect('wishes:detail', pk=wish.pk)
    else:
        form = CommentForm()

    # If GET or invalid → go back to detail with form errors
    return redirect('wishes:detail', pk=wish.pk)
