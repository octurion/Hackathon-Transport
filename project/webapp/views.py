from django.shortcuts import render

from django.http import Http404

from models import User
from models import Route
from models import GeoPoint

def index(request):
    return render(request, 'webapp/index.html')

def user_routes(request):
    try:
        user = User.objects.get(username=request.GET.get('username', ''))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    routes = Route.objects.all().filter(user=user.pk)

    return render(routes, 'webapp/user_routes.html')
