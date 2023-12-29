from django.shortcuts import render
from murder.models import City, Scenario
from django.http import Http404


def home(request):
    cities = City.objects.all()
    context = {
        "cities": cities,
    }
    return render(request, 'home.html', context=context)


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


def murder_party_ville(request, city_slug: str):
    try:
        city = City.objects.get(slug=city_slug)
    except City.DoesNotExist:
        raise Http404("City is not referenced")

    scenarios = Scenario.objects.filter(cities=city).select_related("organization", "theme").prefetch_related("cities").all()

    context = {
        "city": city,
        "scenarios": scenarios,
    }

    return render(request, 'murder_party_ville.html', context=context)


def murder_party_france(request):
    scenarios = Scenario.objects.filter().select_related("organization", "theme").prefetch_related("cities").all()

    context = {
        "scenarios": scenarios,
    }

    return render(request, 'murder_party_france.html', context=context)


def murder_party_scenario(request, scenario_slug: str):
    try:
        scenario = Scenario.objects.get(slug=scenario_slug)
    except Scenario.DoesNotExist:
        raise Http404("Scenario is not referenced")

    context = {
        "scenario": scenario,
    }

    return render(request, 'murder_party_scenario.html', context=context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
