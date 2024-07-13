"""Views for the firearm scoring app.

Classes:
    DrillView -- List of drills.
"""

from django.views.generic import DetailView, ListView, TemplateView
from . import models

class IndexView(TemplateView):
    template_name = 'scoring/index.html'

class DrillView(ListView):
    """A generic list of available drills."""

    context_object_name = 'drills'
    model = models.Drill

    #def get_context_data(self, **kwargs):
    #    context = Drill.objects.all()
    #    return context

class DrillDetails(DetailView):
    """A detailed view of the drills"""

    context_object_name = 'drill_details'
    model = models.Drill
    template_name = 'scoring/drill_list.html'