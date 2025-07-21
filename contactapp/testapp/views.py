from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

class HomeView(ListView):
    model = Contact
    template_name = 'home.html'
    context_object_name = 'contacts'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('home')

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('home')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('home')