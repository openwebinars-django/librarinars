from django.db import models


class BookCategory(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title
