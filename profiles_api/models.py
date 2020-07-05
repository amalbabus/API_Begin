from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManger(BaseUserManager):
    """ manager for UserProfile"""
    def create_user(self, email,name, password=None):
        """create a new userprofile"""
        if not email:
            raise(ValueError('User must have an email adress'))
        email = self.normalize_email(email)

        user= self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return(user)
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser=True
        user.is_staff= True
        user.save(using=self._db)

        return(user)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for user in the system"""
    email= models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False) 


    objects= UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def __str__(self):
        return self.email
    

