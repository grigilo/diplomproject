from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView

from ad.forms import AdForm
from ad.models import Ad


# Create your views here.
class AdCreateView(CreateView, LoginRequiredMixin):
    model = Ad
    form_class = AdForm
    success_url = reverse_lazy('ad:list')

    def form_valid(self, form):
        post = form.save()
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    success_url = reverse_lazy('ad:list')


class AdListView(ListView):
    model = Ad


class AdDetailView(DetailView):
    model = Ad

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class AdDeleteView(DeleteView):
    model = Ad
    success_url = reverse_lazy('ad:list')
