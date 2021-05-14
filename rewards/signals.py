from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import ProductReview
from .models import Reward, RewardHistory


@receiver(post_save, sender=ProductReview)
def reward_review(sender, instance, created, **kwargs):
    """
    Add reward to RewardHistory on ProductReview creation
    """
    if created:
        reward_type = Reward.objects.get(type="Product Review")
        new_reward = RewardHistory.objects.create(reward=reward_type, profile=instance.user.userprofile, product=instance.product)
        new_reward.save()


@receiver(post_save, sender=UserProfile)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Add reward to RewardHistory on UserProfile creation
    """
    if created:
        reward_type = Reward.objects.get(type="Site Registration")
        new_reward = RewardHistory.objects.create(reward=reward_type, profile=instance.user.userprofile, product=None)
        new_reward.save()
