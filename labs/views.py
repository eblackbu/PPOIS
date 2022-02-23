from django.shortcuts import redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from labs import models


def root_view(request):
    return redirect('/labs/')


class LabListView(ListView):
    model = models.Lab
    template_name = 'lab_list.html'
    paginate_by = 50


class LabDetailView(DetailView):
    model = models.Lab
    template_name = 'lab_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['results'] = context_data['object'].results.select_related('sgroup').all()
        return context_data


class GroupDetailView(DetailView):
    model = models.StudentsGroup
    template_name = 'group_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['labs'] = {
            lab: lab.results.filter(sgroup_id=context_data['object'].id)
            for lab in models.Lab.objects.all()
        }
        return context_data

