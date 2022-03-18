from django.db import models

# Create your models here.
class Shortened(models.Model):
    # stores original URL, unique so we dont take up too much space
    long = models.URLField()

    # stores shortened URL, capped at 20
    short = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.long} to \{self.short}'

