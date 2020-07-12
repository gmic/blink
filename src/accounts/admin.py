from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import MyUser


admin.site.site_header = "Blink admin"


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(MyUser, MyUserAdmin)
