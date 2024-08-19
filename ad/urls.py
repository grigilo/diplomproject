from django.urls import path
from django.views.decorators.cache import cache_page

from ad.apps import AdConfig
from ad.views import AdCreateView, AdListView, AdUpdateView, AdDeleteView, \
    AdDetailView

app_name = AdConfig.name

urlpatterns = [
    path('create/', AdCreateView.as_view(), name='create'),
    path('', AdListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(AdDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', AdUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='delete'),
]
