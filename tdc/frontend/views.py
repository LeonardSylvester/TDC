from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import *
from core.models import Design, Gallery


class HomeView(TemplateView):
    template_name = "home.html"


class GalleryListView(ListView):
    context_object_name = "gallery_list"
    queryset = Gallery.objects.all()
    template_name = "gallery_list.html"

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GalleryListView, self).dispatch(*args, **kwargs)


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryDetailView, self).get_context_data(**kwargs)
        context['designs'] = Design.objects.filter(gallery=self.get_object())
        return context