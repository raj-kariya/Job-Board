from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 255)
    show_description = models.TextField()
    long_description = models.TextField(null = True,blank = True)

    created_by = models.ForeignKey(User,related_name = 'jobs',on_delete = models.CASCADE)
    #add a new job --> created_at
    created_at = models.DateTimeField(auto_now_add = True)
    #updating job --> changed_at
    changed_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return str(self.title)