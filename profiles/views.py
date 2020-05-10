from django.shortcuts import render


def user_profile(request):
    """ A view to show user profile """

    

    return render(request, 'profiles/user_profile.html')
