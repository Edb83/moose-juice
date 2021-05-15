from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Reward(models.Model):
    type = models.CharField(max_length=254, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.type


class RewardHistory(models.Model):

    class Meta:
        verbose_name_plural = 'Reward History'

    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name="rewards")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.reward)
