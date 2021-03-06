from django.db import models

# Create your models here.

class Publisher(models.Model):
    ''' A company that publishes books '''
    name = models.CharField(max_length=50, help_text='The name of the publisher.')

    website = models.URLField(help_text='The Publisher website')

    email = models.EmailField(help_text='The Publisher email address')

class Book(models.Model):
    ''' A published book'''
    title = models.CharField(max_length=70, help_text='The Title of the book')

    publication_date = models.DateField(verbose_name='Date the book was published')

    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book')

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Contributor(models.Model):
    ''' A contributor to a Bookm eg. author, editor, co-author.'''

    first_name = models.CharField(max_length=50, help_text='The contributors The first name or names')
    
    last_name = models.CharField(max_length=50, help_text='The contributors The first name or names')
    
    email = models.EmailField(help_text='The contact email for the contributors')

