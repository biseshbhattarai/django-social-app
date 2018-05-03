from django.contrib import admin


from .models import Profile, Friends

admin.site.register(Profile)
admin.site.register(Friends)