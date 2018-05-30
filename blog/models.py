from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # models.ForiegnKey: link to the another model)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # models.CharField: for text with limited length such as title
    title = models.CharField(max_length = 200)
    # models.TextField: for text with unlimited length
    text = models.TextField()
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
            blank = True, null = True)

    def publish(self):
        self.publishd_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
