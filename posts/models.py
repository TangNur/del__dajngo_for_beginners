from django.db import models


class Post(models.Model):
    test = models.TextField()

    def __str__(self):
        return self.test[:64]
