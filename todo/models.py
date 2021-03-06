from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=timezone.now())

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.datetime = timezone.now()
        self.modified = timezone.now()
        return super(Todo,self).save(*args, **kwargs)