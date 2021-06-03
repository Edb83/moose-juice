from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Reward(models.Model):
    """
    Stores types of reward and their values when awarded to users
    on account creation, verified purchase reviews and purchases
    made.
    """
    type = models.CharField(max_length=254, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.type


class RewardHistory(models.Model):
    """
    The history of all the rewards and points a user has received.
    """
    class Meta:
        verbose_name_plural = 'Reward History'
        ordering = ['-pk']

    reward = models.ForeignKey(
        Reward, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        null=True, blank=True, related_name="rewards")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.reward)
