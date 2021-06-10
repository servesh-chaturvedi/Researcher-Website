from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + " - " + self.desc[:50]

class Published(models.Model):
    TYPE = [("JOUR", "Journal"),("CONF", "Conference"),("OTHR","Others")]
    type = models.CharField(choices=TYPE, default="JOUR",max_length=5)
    year = models.CharField(max_length=4)
    publisher = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    brief = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.type + " - " + self.title[:50] + " - " + self.year