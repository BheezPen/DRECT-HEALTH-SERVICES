from django.db import models

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

User = settings.AUTH_USER_MODEL



class CustomUser(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(_('email address'), unique=True)
	user_name = models.CharField(max_length=150, unique=True)
	bio = models.TextField(default='No bio', blank=True)
	joined = DateTimeField(default=timezone.now)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_name']

	objects = CustomUserManager()

	def __str__(self):
		return self.user_name

