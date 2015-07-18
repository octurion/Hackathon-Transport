from django.shortcuts import render

from forms import UserForm
from models import UserProfile
from django.contrib.auth import authenticate, login

from django.http import Http404

from models import User
from models import Route


def index(request):
    return render(request, 'webapp/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            # Hash the password and update the user object.
            user.set_password(user.password)
            user.save()

            profile = UserProfile()
            profile.user = user
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    context = {'user_form': user_form, 'registered': registered}
    return render(request, 'webapp/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)   

        if user:
            login(request, user)
            return render(request, "webapp/index.html", {'logged_in_user': user.username})
        else:
            return render(request, 'webapp/login.html', {'error': "Invalid login! Try Again!"})
    else:
        return render(request, 'webapp/login.html', {})


def user_routes(request):
    try:
        user = User.objects.get(username=request.GET.get('username', ''))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    routes = Route.objects.all().filter(user=user.pk)

    return render(routes, 'webapp/user_routes.html')