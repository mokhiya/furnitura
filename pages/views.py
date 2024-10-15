from django.shortcuts import render
from django.views.generic import TemplateView


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
