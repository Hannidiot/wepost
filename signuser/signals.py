from django.db.models.signals import post_save
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import UserProfile

@receiver(user_signed_up)
def user_profile_create(sender, **kwargs):
    user = kwargs['user']
    try:
        print("triggered")
        UserProfile.objects.get(user_id=user.id)
    except:
        print(user)
        user_profile = UserProfile(user_id=user.id)
        user_profile.save()

# user_signed_up.connect(user_profile_create)
