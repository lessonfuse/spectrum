"""
Writing our own generic views with a bit of extending from the default classes provided by django

This extension is mainly done to pass a form helper class from crispy forms. (as of now)
"""

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from onlydjango.helpers.formclass import ODFormHelper


class ODListView(ListView):
    template_name = "generic/list.html"


class ODDetailView(DetailView):
    template_name = "generic/detail.html"


class ODCreateView(CreateView):
    template_name = "generic/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["helper"] = ODFormHelper()

        return context


class ODUpdateView(UpdateView):
    template_name = "generic/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["helper"] = ODFormHelper(form=self.get_form())

        return context


class ODDeleteView(DeleteView):
    template_name = "generic/delete.html"
