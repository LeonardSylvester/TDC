from django.views.generic import *
from core.models import Design


class HomeView(TemplateView):
    template_name = "home.html"


class DesignListView(ListView):
    context_object_name = "designs_list"
    queryset = Design.objects.all()
    template_name = "design_list.html"