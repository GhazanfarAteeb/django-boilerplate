from django.utils.translation import gettext_lazy as _

import settings
# from mail.utils import create_deeplink
from user.models import User
import random
import string


def invite_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def password_reset_request_handler(user: User, code) -> dict:
    """Generates replacement dict for password_reset_mail"""
    # deep_link = create_deeplink(type="password_reset", verificaton_code=code, email=user.email)
    sections = {
        'current_user': user,
        'email': user.email,
        'code': code,
        'url': settings.FRONTEND_URL,
        'text': _('Please use this code for reset password:') % {'code': code},
    }
    return sections


def verify_email_handler(user: User, code) -> dict:
    """Generates replacement dict for verify_email"""
    # deep_link = create_deeplink(type="registration", verificaton_code=code, email=user.email)
    sections = {
        'current_user': user,
        'email': user.email,
        'url': settings.FRONTEND_URL,
        'code': code,
        'text': _('Please use this url for verify email:\n%(url)s\n') % {'url': settings.FRONTEND_URL},
    }
    return sections
