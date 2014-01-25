import jwt

from django.db import models
from django.conf import settings

from blimp.accounts.constants import MEMBER_ROLES
from blimp.users.utils import get_gravatar_url


class SignupRequestManager(models.Manager):
    def get_from_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            return None

        payload_type = payload.get('type')
        payload_email = payload.get('email')

        if payload_type == 'SignupRequest' and payload_email:
            try:
                return SignupRequest.objects.get(email=payload_email)
            except SignupRequest.DoesNotExist:
                pass

        return None


class SignupRequest(models.Model):
    email = models.EmailField(unique=True)
    objects = SignupRequestManager()

    def __unicode__(self):
        return self.email

    @property
    def token(self):
        """
        Returns a JSON Web Token
        """
        payload = {
            'type': 'SignupRequest',
            'email': self.email,
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY)

        return jwt_token.decode('utf-8')

    def send_email(self):
        from django.core.mail import send_mail

        message = '{}'.format(self.token)

        return send_mail(
            'Blimp Signup Request',
            message,
            'from@example.com',
            [self.email],
            fail_silently=False
        )


class InvitedUser(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    user = models.ForeignKey('users.User', null=True, blank=True)
    account = models.ForeignKey('accounts.Account')
    role = models.CharField(max_length=25, choices=MEMBER_ROLES)
    created_by = models.ForeignKey(
        'users.User', related_name='%(class)s_created_by')

    def __unicode__(self):
        return '{} invited to {}'.format(self.email, self.account)

    def save(self, *args, **kwargs):
        if not self.pk and self.user:
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.email = self.user.email

        return super(InvitedUser, self).save(*args, **kwargs)

    def get_email(self):
        return self.user.email if self.user else self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = u'{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_gravatar_url(self):
        return get_gravatar_url(self.email)

    def get_invite_url(self):
        pass

    def accept(self, user):
        pass

    @property
    def token(self):
        """
        Returns a JSON Web Token
        """
        payload = {
            'type': 'InvitedUser',
            'id': self.pk
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY)

        return jwt_token.decode('utf-8')

    @classmethod
    def notify_pending_invitations(cls, user):
        pass
