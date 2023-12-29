from django.shortcuts import render
from murder.models import City, Scenario, Theme
from django.http import Http404
from django import forms


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


class IntegerRangeField(forms.Field):
    def to_python(self, value):
        value = str(value)  # ensure string
        if not value:
            return tuple()
        return value.split(",", 1)

    def clean(self, value):
        value = super().clean(value)
        if not value:
            return value

        # I should ensure there are exactly two values
        lower_bound, upper_bound = value
        return int(lower_bound), int(upper_bound)


class SearchForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        initial="",
        required=False,
    )
    city = forms.CharField(
        max_length=128,
        initial="",
        required=False,
    )
    theme = forms.CharField(
        max_length=128,
        initial="",
        required=False,
    )
    players = IntegerRangeField(
        initial="",
        required=False,
    )
    duration = IntegerRangeField(
        initial="",
        required=False,
    )
    price = IntegerRangeField(
        initial="",
        required=False,
    )


def apply_search(queryset, validated_search_form):
    if name := validated_search_form.cleaned_data.get("name"):
        queryset = queryset.filter(name__icontains=name)

    if city := validated_search_form.cleaned_data.get("city"):
        queryset = queryset.filter(cities__name=city)

    if theme := validated_search_form.cleaned_data.get("theme"):
        queryset = queryset.filter(theme__name=theme)

    if "players" in validated_search_form.cleaned_data:
        players_min, players_max = validated_search_form.cleaned_data["players"]
        queryset = queryset.filter(players_min__lte=players_max, players_max__gte=players_min)

    if "duration" in validated_search_form.cleaned_data:
        duration_min, duration_max = validated_search_form.cleaned_data["duration"]
        queryset = queryset.filter(duration__lte=duration_max, duration__gte=duration_min)

    if "price" in validated_search_form.cleaned_data:
        price_min, price_max = validated_search_form.cleaned_data["price"]
        queryset = queryset.filter(price__lte=price_max, price__gte=price_min)

    return queryset


def murder_party_france(request):
    error = False
    scenarios = Scenario.objects

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        try:
            valid = search_form.is_valid()
        except Exception:
            valid = False

        if valid:
            scenarios = apply_search(scenarios, search_form)

        else:
            error = True
    else:
        search_form = SearchForm()

    scenarios = scenarios.select_related("organization", "theme").prefetch_related("cities").all()
    cities = City.objects.all()
    themes = Theme.objects.all()

    context = {
        "cities": cities,
        "themes": themes,
        "search_form": search_form,
        "scenarios": scenarios,
        "error": error,
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
