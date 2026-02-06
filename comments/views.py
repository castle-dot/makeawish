from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from wishes.models import Wish
from .forms import CommentForm
from .models import Comment  
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
            messages.success(request, f"Your comment was posted! (ID: {comment.id})")
            return redirect('wishes:detail', pk=wish.pk)
        else:
            messages.error(request, "Comment could not be posted. Please check your input.")
            # Show form errors on redirect
            return redirect('wishes:detail', pk=wish.pk)
    else:
        # GET should not happen - redirect
        return redirect('wishes:detail', pk=wish.pk)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    # Only the comment owner or superuser can delete
    if request.user != comment.user and not request.user.is_superuser:
        messages.error(request, "You can only delete your own comments.")
        return redirect('wishes:detail', pk=comment.wish.pk)
    
    if request.method == 'POST':
        wish_id = comment.wish.pk  # remember wish to redirect back
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('wishes:detail', pk=wish_id)
    
    
    return render(request, 'comments/delete_confirm.html', {'comment': comment})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.user:
        messages.error(request, "You can only edit your own comments.")
        return redirect('wishes:detail', pk=comment.wish.pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment.content = content
            comment.save()
            messages.success(request, "Comment updated!")
        else:
            messages.error(request, "Comment cannot be empty.")
        return redirect('wishes:detail', pk=comment.wish.pk)
    
    # GET should not happen (handled by JS)
    return redirect('wishes:detail', pk=comment.wish.pk)