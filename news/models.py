from django.db import models

# Create your models here.

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_created=True)
    text = models.TextField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title