from datetime import timedelta

from django.utils import timezone
from oauth2_provider.models import Application, AccessToken, RefreshToken
from oauth2_provider.settings import oauth2_settings
from oauthlib import common

from users.models import User


def generate_tokens(user: User) -> dict:
    application = Application.objects.first()
    expires = timezone.now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = AccessToken(
        user=user,
        scope='',
        expires=expires,
        token=common.generate_token(),
        application=application
    )
    access_token.save()
    refresh_token = RefreshToken(
        user=user,
        token=common.generate_token(),
        application=application,
        access_token=access_token
    )
    refresh_token.save()
    return {
        'access_token': str(access_token),
        'expires_in': str(access_token.expires),
        'refresh_token': str(refresh_token),
    }
