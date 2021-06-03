from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request,
                "Failed to update profile - please check form and try again")

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    rewards = profile.rewards.all()
    points = profile.points

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'user': profile.user,
        'orders': orders,
        'rewards': rewards,
        'points': points,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Displays information about a user's order history.
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
