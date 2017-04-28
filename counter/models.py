from django.db import models

class Counter(models.Model):
    value = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.value)
