from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView

from comments.forms import CommentForm
from comments.models import Comment


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment:list')

    def form_valid(self, form):
        post = form.save()
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment:list')


class CommentListView(ListView):
    model = Comment


class CommentDetailView(DetailView):
    model = Comment


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment:list')
