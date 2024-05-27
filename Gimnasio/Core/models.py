#from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, user_type='regular'):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(username=username, user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        return self.create_user(username, password, user_type='admin')

#class Usuario(AbstractBaseUser):
#    username = models.CharField(max_length=150, unique=True)
#    user_type = models.CharField(max_length=50)
    
#    objects = UsuarioManager()
    
#    USERNAME_FIELD = 'username'
    
#    def __str__(self):
#        return self.username
    

class Usuario(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('normal', 'Normal'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')
    groups = models.ManyToManyField(Group, related_name='core_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='core_user_set', blank=True)
