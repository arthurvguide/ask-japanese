from django.db import models

class Table(models.Model):
    size = models.IntegerField()

    class Meta:
        ordering = ["-size"]

    def __str__(self):
        return str(self.size)
