from django.shortcuts import render, get_object_or_404
from .models import User_Profile
from .form import User_Profile_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def user_profile(request):
    """ A view to show user profile """

    #profile = User_Profile.objects.get(User_Profile, user=request.user)
    #print(profile)

    return render(request, 'profiles/user_profile.html')


def update_user_profile(request):
    """A view to updating user profile"""
    profile = get_object_or_404(User_Profile, user=request.user)
    if request.method == 'POST':
        form = User_profile_form(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your Profile has been updated!')
        else:
            messages.error(request, 'Something went wrong please \
                                        check your form')

    context = {
        'profile': profile
    }
