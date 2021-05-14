from django.contrib import admin
from .models import Reward, RewardHistory


class RewardAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'value',
    )
    ordering = ('-value',)


class RewardHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'reward',
        'profile',
        'product',
        'created_on',
    )
    ordering = ('-created_on',)


admin.site.register(Reward, RewardAdmin)
admin.site.register(RewardHistory, RewardHistoryAdmin)
