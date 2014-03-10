from django.views.generic import *
from core.models import Design, Category


class HomeView(TemplateView):
    template_name = "home.html"


class DesignListView(ListView):
    context_object_name = "designs_list"
    queryset = Design.objects.all()
    template_name = "design_list.html"

    def get_context_data(self, **kwargs):
        context = super(DesignListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context