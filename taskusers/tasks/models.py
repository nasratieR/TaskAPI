from django.db import models
from django.contrib.auth.models import User


def get_default_author():
    user = User.objects.get_or_create(username='Nasratie')[0]
    return user.id

# Create your models here.
class TasksModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', default=get_default_author)
    
    def __str__(self):
        return self.name