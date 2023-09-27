from django.db import models

# Create your models here.
class Booth(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    kind = models.CharField(max_length=20, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    locate = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True, upload_to='images/')   

    def __str__(self):
        return self.name