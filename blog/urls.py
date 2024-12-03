from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),  # Home page view
    # Dynamic URL for post detail view using slug
    path("post/<str:slug>", views.detail, name="detail"),  
    # URL for a new page
    path("new_url", views.new_url_view, name="new_page_url"),  
    # Redirect from old URL to a new one
    path("old_url", views.old_url_redirect, name="old_url"),  
    # Contact page view
    path('contact/', views.contact_view, name='contact'),  
    # About page view
    path('about/', views.about_view, name='about'),  
]
