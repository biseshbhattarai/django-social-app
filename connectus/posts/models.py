from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    status = models.TextField()
    upload_image = models.FileField(upload_to="documents", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    

    def __str__ (self):
        return self.user.username
