from django.shortcuts import render
from .models import Book, Author, Language, BookInstance, Genre


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    all_genres = Genre.objects.all()
    all_languages = Language.objects.all()
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'all_genres': all_genres,
            'all_languages': all_languages
        },
    )