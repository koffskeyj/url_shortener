from django.db import models
from hashids import Hashids

hashids = Hashids()


class Bookmark(models.Model):
    bookmark = models.CharField(max_length=300)
    bookmark_id = models.CharField(max_length=6)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.bookmark