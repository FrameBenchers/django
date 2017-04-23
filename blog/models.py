from django.db import models
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
