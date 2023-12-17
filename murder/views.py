from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'search.html')


def teambuilding(request):
    return render(request, 'teambuilding.html')


def friends(request):
    return render(request, 'friends.html')


def how_to(request):
    return render(request, 'how_to.html')


def what(request):
    return render(request, 'qu_est_ce_qu_une_murder_party.html')


def blog(request):
    return render(request, 'blog.html')


def murder_party_paris(request):
    return render(request, 'murder_party_paris.html')


def murder_party_lille(request):
    return render(request, 'murder_party_lille.html')


def murder_party_france(request):
    return render(request, 'murder_party_france.html')
