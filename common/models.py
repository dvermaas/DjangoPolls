from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
