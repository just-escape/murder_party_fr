import os
from django import forms
from django.db import models
from django.dispatch import receiver


class City(models.Model):
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"City {self.name}"

    class Meta:
        verbose_name_plural = "Cities"


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class Organization(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Organization {self.name}"


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


class Theme(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Theme {self.name}"


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'


class Scenario(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    cities = models.ManyToManyField(City)
    players_min = models.IntegerField()
    players_max = models.IntegerField()
    price = models.IntegerField()
    duration = models.IntegerField(help_text="In minutes")
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="scenario")
    picture = models.ImageField(upload_to="scenario")
    description_short = models.TextField()
    description_long = models.TextField()
    booking_link = models.URLField()


@receiver(models.signals.post_delete, sender=Scenario)
def auto_delete_images_on_picture_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)

    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.pre_save, sender=Scenario)
def auto_delete_images_on_scenario_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_picture = Scenario.objects.get(pk=instance.pk).picture
    except Scenario.DoesNotExist:
        return False

    new_picture = instance.picture
    if old_picture != new_picture and os.path.isfile(old_picture.path):
        os.remove(old_picture.path)

    try:
        old_thumbnail = Scenario.objects.get(pk=instance.pk).picture
    except Scenario.DoesNotExist:
        return False

    new_thumbnail = instance.thumbnail
    if old_thumbnail != new_thumbnail and os.path.isfile(old_thumbnail.path):
        os.remove(old_thumbnail.path)


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = '__all__'
