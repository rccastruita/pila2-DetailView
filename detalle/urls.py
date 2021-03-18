from django.urls import path
from . import views as MyViews

urlpatterns = [
    path('', MyViews.DetalleListView.as_view(), name='home'),
    path('posts/<int:pk>/', MyViews.DetalleDetailView.as_view(), name='detail'),
]