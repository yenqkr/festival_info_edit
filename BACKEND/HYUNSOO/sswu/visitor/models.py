from django.db import models

# Create your models here.
class Visitor(models.Model):
    content = models.CharField(max_length=1000, null=True, blank=True)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-date']