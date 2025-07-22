from django.db import models
import hashlib

from django.http import HttpRequest


#md5 for hash


# Create your models here.


class Shorter(models.Model):
    original_url = models.URLField(unique=True)
    shortened_url = models.SlugField()

    def save(self, *args, **kwargs):
        self.original_url = self.original_url
        self.shortened_url = hashlib.md5(self.original_url.encode()).hexdigest()
        super().save(*args, **kwargs)

    def get_short_url(self, request: HttpRequest):
        return request.build_absolute_uri(f"/shorter/{self.shortened_url}/")
