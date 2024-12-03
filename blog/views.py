from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
import logging
from .models import Post, AboutUs, Category  # Added Category model
from .forms import ContactForm


# Home Page (Index View)
def index(request):
    blog_title = "Latest Posts"

    # Get selected category from query params
    category_name = request.GET.get('category')
    if category_name:
        all_posts = Post.objects.filter(category__name=category_name)  # Filter by category name
    else:
        all_posts = Post.objects.all()

    # Paginate posts (6 per page)
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all categories for filtering
    categories = Category.objects.all()

    return render(request, "index.html", {
        'blog_title': blog_title,
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_name  # Pass the selected category to the template
    })


# Post Detail View
def detail(request, slug):
    try:
        # Fetch the post by slug
        post = Post.objects.get(slug=slug)
        # Fetch related posts in the same category, excluding the current post
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist!")

    return render(request, "detail.html", {
        'post': post,
        'related_posts': related_posts
    })


# Old URL Redirect
def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))


# New URL View
def new_url_view(request):
    return HttpResponse("This is the new URL")


# Contact Page
def contact_view(request):
    logger = logging.getLogger("TESTING")

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            logger.debug(f"POST Data: {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = 'Your Email has been sent!'
            return render(request, 'contact.html', {
                'form': form,
                'success_message': success_message
            })
        else:
            logger.debug("Form validation failure")
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})


# About Us Page
def about_view(request):
    # Fetch the first AboutUs entry
    about_instance = AboutUs.objects.first()
    about_content = about_instance.content if about_instance else "About us content not available."

    return render(request, "about.html", {'about_content': about_content})
