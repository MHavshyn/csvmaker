from CSVmaker.forms import NewSchemaCreateForm, NumberRow, SchemaEditForm
from CSVmaker.models import NewSchema
from CSVmaker.tasks import create_csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render  # noqa
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView, ListView, UpdateView


class SchemasListView(LoginRequiredMixin, ListView):
    model = NewSchema
    template_name = 'schemas.html'
    context_object_name = 'schemas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = NewSchema.objects.all().filter(user_id=self.request.user)
        context['user_schemas'] = results
        return context


class SchemasCreateView(LoginRequiredMixin, CreateView):
    model = NewSchema
    form_class = NewSchemaCreateForm
    template_name = 'newschema_create.html'
    success_url = reverse_lazy('datalist:result')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SchemasCreateView, self).form_valid(form)


class SchemasFormView(FormView):
    template_name = 'result.html'
    form_class = NumberRow
    success_url = reverse_lazy('datalist:result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = NewSchema.objects.all().filter(user_id=self.request.user)
        context['results'] = results
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            create_csv(
                row=form.cleaned_data['row_number'])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SchemasUpdateView(LoginRequiredMixin, UpdateView):
    model = NewSchema
    form_class = SchemaEditForm
    template_name = 'schemas_edit.html'
    success_url = reverse_lazy('datalist:list')
    context_object_name = 'schema'
    pk_url_kwarg = 'id'


class SchemasDeleteView(LoginRequiredMixin, DeleteView):
    model = NewSchema
    success_url = reverse_lazy('datalist:list')
    pk_url_kwarg = 'id'
    template_name = 'schema_delete.html'
