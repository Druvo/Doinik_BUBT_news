"""Core > models > test_user.py"""
# PYTHON IMPORTS
from sys import _getframe
# DJANGO IMPORTS
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """User Manager overridden from BaseUserManager for User"""

    def _create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not email:  # check for an empty email
            print(  # prints class and function name
                f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
                f"User must set an email address"
            )
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email
            email = self.normalize_email(email)
            print(  # prints class and function name
                f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
                f"Normalized email: {email}"
            )

        # create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        print(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"User created: {user}"
        )
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        print(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating user: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        print(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating staffuser: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)

    def create_teletalkuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('user_type', 2)
        print(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating superuser: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 3)
        print(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating superuser: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model that supports using email instead of username"""
    USER_TYPE_CHOICES = (
        (1, 'User'),
        (2, 'Staff'),
        (3, 'Admin'),
    )
    email = models.EmailField(
        _('Email Address'), max_length=255, unique=True,
        help_text='Ex: example@example.com'
    )
    user_type = models.PositiveIntegerField(
        choices=USER_TYPE_CHOICES
    )
    is_staff = models.BooleanField(
        _('Staff status'), default=False
    )
    is_active = models.BooleanField(
        _('Active'), default=False
    )
    date_joined = models.DateTimeField(
        _('Date Joined'), auto_now_add=True
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True
    )

    objects = UserManager()  # uses the custom manager

    USERNAME_FIELD = 'email'

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['email', 'user_type']),
            models.Index(fields=['email', 'user_type', 'is_active']),
        ]

    def __str__(self):
        """User model string representation"""
        return self.email
