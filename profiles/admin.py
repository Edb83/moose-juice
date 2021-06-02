from django.contrib import admin
from profiles.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'points',
    )

    filter_horizontal = (
        'favourites', 'favourites',
        )


admin.site.register(UserProfile, UserProfileAdmin)
