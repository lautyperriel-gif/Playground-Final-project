from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

# CBV mínima 1: Home (simple)
class HomeView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'pages'

# Decorador en view común (requisito)
def about_view(request):
    return render(request, 'about.html')

# Mixin de dueño (requisito)
class OwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            messages.error(request, 'No tenés permiso para modificar esta página.')
            return redirect('pages:list')
        return super().dispatch(request, *args, **kwargs)

# Listado con buscador simple
class PageListView(ListView):
    model = Page
    template_name = 'pages/pages_list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        qs = Page.objects.order_by('-created_at')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

# Detalle
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/pages_detail.html'
    context_object_name = 'page'

# Crear
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/pages_form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada correctamente.')
        return super().form_valid(form)

# Editar
class PageUpdateView(OwnerRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/pages_form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada.')
        return super().form_valid(form)

# Borrar
class PageDeleteView(OwnerRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/pages_confirm_delete.html'
    success_url = reverse_lazy('pages:list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Página eliminada.')
        return super().delete(request, *args, **kwargs)
