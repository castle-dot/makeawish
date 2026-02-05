from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from comments.forms import CommentForm
from .models import Wish
from .forms import WishForm


class WishListView(ListView):
    model = Wish
    template_name = 'wishes/wish_list.html'
    context_object_name = 'wishes'
    ordering = ['-created_at']           # newest first

class WishCreateView(LoginRequiredMixin, CreateView):
    model = Wish
    form_class = WishForm
    template_name = 'wishes/wish_form.html'
    success_url = reverse_lazy('wishes:list')   # redirect after save

    def form_valid(self, form):
        form.instance.user = self.request.user  # auto-set the owner
        return super().form_valid(form)
class WishDetailView(DetailView):
    model = Wish
    template_name = 'wishes/wish_detail.html'
    context_object_name = 'wish'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  
        return context

class WishUpdateView(LoginRequiredMixin, UpdateView):
    model = Wish
    form_class = WishForm
    template_name = 'wishes/wish_form.html'     # same form as create — good reuse
    success_url = reverse_lazy('wishes:list')

    def get_queryset(self):
        # Only the owner can edit
        return Wish.objects.filter(user=self.request.user)


class WishDeleteView(LoginRequiredMixin, DeleteView):
    model = Wish
    template_name = 'wishes/wish_confirm_delete.html'
    success_url = reverse_lazy('wishes:list')

    def get_queryset(self):
        # Only the owner can delete
        return Wish.objects.filter(user=self.request.user)  # only allow deleting own wishes


@login_required
def mark_granted(request, pk):
    wish = get_object_or_404(Wish, pk=pk)
    
    if request.user != wish.user:
        messages.error(request, "Only the owner can mark this wish as granted.")
    elif wish.is_granted:
        messages.info(request, "This wish is already marked as granted.")
    else:
        wish.is_granted = True
        wish.save()
        messages.success(request, "Wish marked as granted!")
    
    return redirect('wishes:detail', pk=pk)