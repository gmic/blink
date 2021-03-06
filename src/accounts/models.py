from django.contrib.auth.models import AbstractUser


class BlinkUser(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


BlinkUser._meta.get_field("email")._unique = True
