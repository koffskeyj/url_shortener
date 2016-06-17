from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids

hashids = Hashids()


class Bookmark(models.Model):
    bookmark = models.CharField(max_length=300)
    bookmark_id = models.CharField(max_length=6)
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.bookmark