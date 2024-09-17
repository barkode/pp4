from django.shortcuts import render
from django.views import generic

from .models import About


# def about(request):
#     """
#     Renders the About page
#     """
#     about = About.objects.all().order_by('-updated_on').first()
#
#     return render(
#         request,
#         "about/about.html",
#         {"about": about},
#         )

class AboutView(generic.TemplateView):
    template_name = "about/about.html"
    context_object_name = 'about_page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all().order_by('-updated_on').first()
        return context
