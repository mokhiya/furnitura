from django.urls import path
from pages import views


app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContentView.as_view(), name='contact'),
    path('blogs/list/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/', views.BlogDetailView.as_view(), name='blog'),
    path('pages/about/', views.AboutUsView.as_view(), name='about'),
    path('pages/productlist/', views.ProductListView.as_view(), name='products'),
    path('pages/product', views.ProductDetailView.as_view(), name='product'),

    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('create/', views.ContactCreateView.as_view(), name='create'),

    path('', views.HomeView.as_view(), name='home'),
]