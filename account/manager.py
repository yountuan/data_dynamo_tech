from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is required!')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        user = self._create_user(email=email, password=password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email=email, password=password, **extra_fields)