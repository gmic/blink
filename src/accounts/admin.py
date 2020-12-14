from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import BlinkUser


admin.site.site_header = "Blink admin"


class BlinkUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(BlinkUser, BlinkUserAdmin)
