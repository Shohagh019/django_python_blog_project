from django.db import models
from categories.models import Category
from authors.models import Author
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete= models.CASCADE )
    def __str__(self):
        return self.title
