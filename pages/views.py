from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext_lazy as _

from pages.admin import ContactModel
from pages.forms import ContactModelForm


class ContentView(TemplateView):
    template_name = 'contact.html'


class HomeView(TemplateView):
    template_name = 'home.html'


# blogs
class BlogListView(TemplateView):
    template_name = 'blog-list.html'


class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'


# pages
class ProductListView(TemplateView):
    template_name = 'product-list.html'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class AboutUsView(TemplateView):
    template_name = 'about-us.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class WishlistView(TemplateView):
    template_name = 'user-wishlist.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ContactCreateView(CreateView):
    model = ContactModel
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('pages:create')
    success_message = _('Your message is submitted!')
