from django.contrib import admin
from .models import Post, Category , AboutUs

# Register your models here.


#admin.site.register(Post)
#admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'content', 'img_url')
    search_fields=('title', 'content', 'img_url')
    list_filter = ('category', 'created_at')  # Correctly defined as a tuple


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)