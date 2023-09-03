"""Views for the firearm scoring app.

Classes:
    DrillView -- List of drills.
"""

from django.views.generic.list import ListView
from .models import Drill

class DrillView(ListView):
    """A generic list of available drills."""

    model = Drill

    #def get_context_data(self, **kwargs):
    #    context = Drill.objects.all()
    #    return context