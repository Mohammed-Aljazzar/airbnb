from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property

# Create your views here.

class PropertyList(ListView):
    model = Property
    paginate_by = 1

    # template_name = 'property/property_list.html'
    # context_object_name = 'properties'

class PropertyDetail(DetailView):
    model = Property
    # template_name = 'property/property_detail.html'
    # context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    pass 