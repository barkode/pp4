from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import CollaborateRequest
from .models import About


class AboutPage(generic.FormView, generic.TemplateView):
    template_name = "about/about.html"
    form_class = CollaborateRequest
    success_url = reverse_lazy('about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all().order_by('-updated_on').first()
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Collaboration request received! I endeavor to respond within 2 working days.')
        return super().form_valid(form)

