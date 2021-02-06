from django.db import models

class myskill(models.Model):
    image = models.ImageField(upload_to="skillimage/")
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(max_length=500,blank=True)
    datetime = models.DateTimeField()

    def summary(self):
        return self.description[0:100]

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    subject = models.TextField(max_length=50,blank=False)
    message = models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.name

