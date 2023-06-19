from django.db import models
import random


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    color = models.CharField(max_length=7, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = "#%06x" % random.randint(0, 0xFFFFFF)
        super(Contact, self).save(*args, **kwargs)
