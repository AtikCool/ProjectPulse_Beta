from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Q
from .models import Friendship, User
from django.urls import reverse
from .forms import SignInForm
from django.contrib import auth
def send_friend_request(request, to_user_id):
    from_user = request.user
    to_user = get_object_or_404(User, pk=to_user_id)
    friendship_request = Friendship(from_user=from_user, to_user=to_user, status='pending')
    friendship_request.save()
    return redirect('friends_list')

def accept_friend_request(request, from_user_id):
    friendship_request = get_object_or_404(Friendship, from_user_id=from_user_id, to_user=request.user, status='pending')
    friendship_request.status = 'accepted'
    friendship_request.save()
    return redirect('friends_list')

def reject_friend_request(request, from_user_id):
    friendship_request = get_object_or_404(Friendship, from_user_id=from_user_id, to_user=request.user, status='pending')
    friendship_request.status = 'rejected'
    friendship_request.save()
    return redirect('friends_list')
def friends_list(request):
    user = request.user
    friend_requests_received = Friendship.objects.filter(to_user=user, status='pending')
    friend_requests_sent = Friendship.objects.filter(from_user=user, status='pending')
    friends = Friendship.objects.filter((Q(from_user=user) | Q(to_user=user)) & Q(status='accepted'))
    return render(request, 'users/friends_list.html', {'friends': friends, 'friend_requests_received':friend_requests_received, 'friend_requests_sent':friend_requests_sent})
# Create your views here.



def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            remeber = request.POST.get('remember_me', None)
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

                if remeber:
                    request.session.set_expiry(604800)
                else:
                    request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('main:friends'))

    else:
        form = SignInForm()

    return render(request, 'users/login.html', {'form': form})
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))