import time
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_page


def main(request):
    if request.method == 'GET':
        return HttpResponse(request.user.username)
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Done!")
    return HttpResponse("Failed!")

@cache_page(10)
def test(request):
    if request.user:
        time.sleep(3)
        return HttpResponse(request.user.username)
    return HttpResponse("No")
