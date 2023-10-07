from django.db import models
from django.core.validators import MinValueValidator


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rizz = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    message = models.TextField()

    def __str__(self):
        return self.name
