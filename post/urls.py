from django.urls import path
from post.views import DetailView

urlpatterns = [
    path('details/<int:pk>/', DetailView.as_view(), name='details'),
]
