from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, name, email, phone_number, role, password=None, **kwargs):
        #Creates and saves a new user.
        user = self.model(
            name=name,
            email=email,
        )
         
        user.phone_number=phone_number,
        user.role=role,
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password, phone_number, role):
        #Creates and saves a new superuser.
        user = self.create_user(name, email, phone_number, role,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    #Custom user model.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'phone_number']