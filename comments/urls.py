from django.urls import path
from comments.apps import CommentsConfig
from comments.views import CommentCreateView, CommentDeleteView, \
    CommentUpdateView, CommentDetailView, CommentListView

app_name = CommentsConfig.name

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('', CommentListView.as_view(), name='list'),
    path('view/<int:pk>/', CommentDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', CommentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='delete'),
]
