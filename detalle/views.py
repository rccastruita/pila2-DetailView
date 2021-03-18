from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from . import models as MyModels

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'

class DetalleListView(ListView):
    model = MyModels.Post
    template_name = 'posts.html'
    context_object_name = 'posts'

class DetalleDetailView(DetailView):
    model = MyModels.Post
    template_name = 'detalle-post.html'
    context_object_name = 'post'