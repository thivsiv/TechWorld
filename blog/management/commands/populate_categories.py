from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts Category data"

    def handle(self, *args, **options):

        #Delete Exsisting Data
        Category.objects.all().delete()

        categories=['Sports', 'Technology' , 'Science' , 'Art' , 'Food']
       

        # Inserting the posts into the database
        for category_name in categories:
            Category.objects.create(name = category_name)
            

        # Output success message
        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
