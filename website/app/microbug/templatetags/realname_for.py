import datetime
from django import template
from microbug.models import UserProfile

register = template.Library()

@register.simple_tag
def realname_for(user_id):
    user_profile = UserProfile.objects.get(pk=user_id)

    if user_profile and user_profile.realname is not None and user_profile.realname != "":
        return user_profile.realname
    else:
        # Lorem ipsum
        return 'No name set'
