from django.db import models
from django.conf import settings
# from imagekit.models import ProcessedImageField

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'mainpage'


class InfoImage(models.Model):
    info = models.ForeignKey(Info, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='info_images/', null=True, blank=True)