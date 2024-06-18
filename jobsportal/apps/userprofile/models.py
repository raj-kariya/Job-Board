from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name="serprofile", on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)
    
def get_or_createuserprofile(user):
    profile, created = Userprofile.objects.get_or_create(user = user)
    return profile
User.Userprofile = property(lambda u : get_or_createuserprofile(u)[0])
