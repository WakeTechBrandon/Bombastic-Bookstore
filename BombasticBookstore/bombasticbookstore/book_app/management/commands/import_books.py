import csv
from django.core.management.base import BaseCommand
from book_app.models import Book, BookQuantity

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                book, created = Book.objects.get_or_create(
                    isbn10=row['isbn10'],
                    defaults={
                        'title': row['title'],
                        'author_first': row['author_first'],
                        'author_last': row['author_last'],
                        'categories': row['categories'],
                        'thumbnail': row['thumbnail'],
                        'published_year': row['published_year'],
                        'num_pages': row['num_pages'],
                    }
                )
                
                BookQuantity.objects.create(book_id=book.id, quantity=0)
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Book '{book.title}' added successfully"))
                else:
                    self.stdout.write(self.style.WARNING(f"Book '{book.title}' already exists"))