from django.db import models


class Bookmark(models.Model):
    bookmark = models.CharField(max_length=300)
