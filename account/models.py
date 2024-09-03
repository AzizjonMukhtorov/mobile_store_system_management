from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    def create_user(self, name, surname, phone_number, role, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be set")
        user = self.model(name=name, surname=surname, phone_number=phone_number, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, surname, phone_number, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if role is None:
            role, _ = Role.objects.get_or_create(title='SuperUser')
        # Ensure role is a Role instance
        if isinstance(role, int):  # If role is passed as an ID
            role = Role.objects.get(pk=role)
        elif isinstance(role, str):  # If role is passed as a title string
            role = Role.objects.get(title=role)

        return self.create_user(name, surname, phone_number, role, password, **extra_fields)
        


class Role(models.Model):

    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Role")
        verbose_name_plural = ("Roles")

    def __str__(self):
        return self.title


class CustomUser(PermissionsMixin, AbstractBaseUser):

    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'surname', 'role']

    objects = CustomUserManager()

    class Meta:
        verbose_name = ("CustomUser")
        verbose_name_plural = ("CustomUsers")

    def __str__(self):
        return self.name + " " + self.surname

