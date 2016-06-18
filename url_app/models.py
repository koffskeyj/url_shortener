from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids

hashids = Hashids()


class Bookmark(models.Model):
    URL = models.URLField(max_length=300)
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User)
    hash_id = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Click(models.Model):
    URL = models.ForeignKey(Bookmark)
    date_time = models.DateTimeField()