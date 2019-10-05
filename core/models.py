from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    author = models.CharField(max_length=54, default='author')
    title = models.CharField(max_length=54, default='title')
    review = models.TextField(blank=True, null=True)
    if_read = models.BooleanField(default=False)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}, {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[f'{self.id}', ])
