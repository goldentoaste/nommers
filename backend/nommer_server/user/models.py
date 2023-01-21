from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid

class AuthorManager(BaseUserManager):

    def create_user(
        self, 
        userName=None,
        password=None,
        ppiUrl = ""):

        if not userName:
            raise ValueError("User must have user name")
        
        if not password:
            raise ValueError("User msut have a password")

        user = self.model(
            id = uuid.uuid4(),
            userName = userName,
            password= password,
            ppiUrl = ppiUrl
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, userName, password, ppiUrl = ""):
        user = self.create_user(userName, password, ppiUrl)
        user.is_admin = True
        user.save(using=self._db)
        return user


def getUUID():
    return str(uuid.uuid4())

class User(AbstractBaseUser):

    id = models.CharField(
        primary_key=True,
        default= getUUID,
        editable=False,
        max_length=200)

    userName = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        unique=True,
        default="null user"
    )

    ppiUrl = models.URLField("profile picture url",
        blank=True,
        null=True
    )

    is_admin = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"User| id: {self.id}, name: {self.userName}"

    objects : AuthorManager = AuthorManager()

    USERNAME_FIELD = "userName"

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app):
        return True

    @property
    def is_staff(self):
        return self.is_admin