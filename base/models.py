from django.db import models
from django.contrib.auth.models import User #takes care of all user information such as username, email, password, etc.
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True) #User is a model name, 1 to many relation(1 user have many items)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False) #false because when the task firstly created probably it's not completed
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
