from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
     address = models.CharField(max_length=120, null=True)
     # gender = models.RadioSelect()
     
     education = models.CharField(max_length=60, null=True)
     status = models.TextField(null=True, blank=True)
    #  profile_image = models.FileField(upload_to="documents" ,null=True)
    #  cover_image = models.FileField(upload_to='documents', null=True)
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     objects = models.Manager()

     def __str__ (self):
         return self.user.username


class Friends(models.Model):
    user = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, null=True )

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.add(new_friend)
        is_following = True

        
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.user.remove(new_friend)
        is_following = False


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


