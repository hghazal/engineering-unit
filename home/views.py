from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        context = {}
        return self.render_to_response(context)

