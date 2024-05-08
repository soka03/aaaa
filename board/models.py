from django.db import models
from django.conf import settings
# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    body = models.TextField(default= "")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
