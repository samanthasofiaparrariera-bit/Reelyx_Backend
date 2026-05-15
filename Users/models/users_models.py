from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserBase(BaseUserManager):

    def crear_usuario(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.crear_usuario(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = None
    email = models.EmailField(max_length=200, unique=True, blank=False, verbose_name='Email')
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    image = models.ImageField(upload_to='usuarios/',
                              default='usuarios/default-user-pfp.png', null=True, blank=True)
    bio = models.TextField(blank=True, default='')
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserBase()
    #

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = 'usuario_reelyx'