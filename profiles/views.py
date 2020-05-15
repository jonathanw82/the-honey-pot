from django.shortcuts import render, get_object_or_404
from .models import User_Profile
from .form import User_Profile_form, Logged_In_User_Form
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def user_profile(request):
    """ A view to show user profile """

    user = request.user
    logged_in_form = Logged_In_User_Form(instance=user)
    profileGet = get_object_or_404(User_Profile, user=user)
    profileform = User_Profile_form(instance=profileGet)

    if request.method == 'POST':
        logged_in_form = Logged_In_User_Form(request.POST, instance=user),
        profileform = User_Profile_form(request.POST, instance=profileform),

        if logged_in_form.is_valid():
            logged_in_form.save()

        if profileform.is_Valid():
            profileform.save()

    context = {
        'logged_in_form': logged_in_form,
        'profileform': profileform,
        }

    return render(request, 'profiles/user_profile.html', context)


# def update_user_profile(request):
#     """A view to updating user profile"""
#     profile = get_object_or_404(User_Profile, user=request.user)
#     if request.method == 'POST':
#         form = User_profile_form(request.POST)
#         if form.is_valid:
#             form.save()
#             messages.success(request, 'Your Profile has been updated!')
#         else:
#             messages.error(request, 'Something went wrong please \
#                                         check your form')

#     context = {
#         'profile': profile
#     }
