from django.shortcuts import render, redirect
from .models import Profile, Favorite, Comment
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    profile = request.user.profile
    favorites = Favorite.objects.filter(user=request.user)
    comments = Comment.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'favorites': favorites, 'comments': comments})
