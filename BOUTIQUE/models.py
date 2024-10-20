from django.db import models

class Boutique(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='boutique_images/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
