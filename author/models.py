from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(User, related_name='accounts_author',
                              on_delete=models.PROTECT)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)