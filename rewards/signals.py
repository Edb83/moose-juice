from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from profiles.models import UserProfile
from products.models import ProductReview
from checkout.models import Order
from .models import Reward, RewardHistory

import math


@receiver(pre_save, sender=ProductReview)
def reward_review(sender, instance, **kwargs):
    """
    Add reward to RewardHistory and update user's points
    on ProductReview creation
    """
    # Get the reward, value, user, product and existing reviews
    reward = Reward.objects.get(type="Product Review")
    reward_value = reward.value
    user = instance.user
    product = instance.product
    reviews = product.reviews.all()

    # Check whether user has already reviewed product
    if reviews.filter(user=user).exists():
        pass

    # Check whether user has previously purchased
    if instance.verified_purchase:
        # Update and save points to user's profile
        user.userprofile.points += reward_value
        user.userprofile.save()

        # Add the reward to user's reward history
        new_reward = RewardHistory.objects.create(
            reward=reward, profile=user.userprofile, product=instance.product, points=reward_value)
        new_reward.save()


@receiver(post_save, sender=UserProfile)
def reward_account_creation(sender, instance, created, **kwargs):
    """
    Add reward to RewardHistory and update user's points
    on UserProfile creation
    """
    if created:
        reward = Reward.objects.get(type="Site Registration")
        reward_value = reward.value

        instance.points += reward_value
        instance.save()

        new_reward = RewardHistory.objects.create(
            reward=reward, profile=instance, product=None, points=reward_value)
        new_reward.save()


@receiver(post_save, sender=Order)
def reward_purchase(sender, instance, **kwargs):
    """
    Add reward to RewardHistory and update user's points
    on Order creation

    As the Order is saved multiple times the signal will
    be fired repeatedly, so checking that the user profile
    has been attached to the instance is necessary to
    carry out the function.
    """
    if instance.user_profile:
        profile = instance.user_profile

        if instance.points_redeemed:
            redemption = Reward.objects.get(type="Redemption")
            new_redemption = RewardHistory.objects.create(
                reward=redemption, profile=profile,
                product=None, points=instance.points_redeemed
            )
            new_redemption.save()

        reward = Reward.objects.get(type="Purchase")
        profile.points += instance.points_earned

        profile.save()

        new_reward = RewardHistory.objects.create(
            reward=reward, profile=profile,
            product=None, points=instance.points_earned
            )
        new_reward.save()
