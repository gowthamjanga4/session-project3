from django.shortcuts import render


# Create your views here.

def name_view(request):
    return render(request, 'testapp/name.html')


def age_view(request):
    print(request.COOKIES)
    name = request.GET['name']
    response = render(request, 'testapp/age.html', {'name': name})
    response.set_cookie('name', name)
    return response


def gf_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.GET['age']
    response = render(request, 'testapp/gf.html', {'name': name})
    response.set_cookie('age', age)
    return response


def place_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    response = render(request, 'testapp/place.html', {'name': name})
    response.set_cookie('gf', gf)
    return response


def results_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.COOKIES['gf']
    place = request.GET['place']
    response = render(request, 'testapp/results.html', {'name': name, 'age': age, 'gf': gf, 'place': place})
    response.set_cookie('place', place)
    return response
