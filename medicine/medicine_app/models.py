from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""A family member of the user who uses the drugs in his medicine cabinet."""

DISEASE_CHOICE = (
    (1, "kaszel suchy"),
    (2, "kaszel mokry"),
    (3, "gorączka"),
    (4, "ból gardła"),
    (5, "ból"),
    (6, "alergia"),
    (7, "odporność"),
    (8, "katar"),
    (9, "oczy"),
    (10, "układ pokarmowy"),
    (11, "skaleczenia"),
    (12, "ukąszenia owadów"),
    (13, "antybiotyk"),
    (14, "inne"),
)


# class FamilyMember(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     weight = models.DecimalField(max_digits=6, decimal_places=2)
#     date_of_birth = models.DateField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     relationship = models.CharField(max_length=64)


"""Logged-in user who owns the medicine cabinet. 
   May have family members who use the medicines in the first aid kit."""


# class Owner(models.Model):
#     name = models.OneToOneField(User, on_delete=models.CASCADE)
#     family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)


"""A keyword that allows to search for a specific drug."""


class Category(models.Model):

    name = models.CharField(max_length=64)


""" The drug in the medicine cabinet. 
    After assigning it to a specific family member, it calculates the correct dose of the drug"""


class Medicine(models.Model):
    name = models.CharField(max_length=128)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True)  # zastosowanie
    ingredients = models.TextField(blank=True)
    dosage = models.CharField(max_length=255)
    contraindications = models.CharField(max_length=255)  # przeciwwskaznaia
    comments = models.CharField(max_length=128)
    expiration_date = models.DateField()
    taken_continuously = models.BooleanField(default=False)  # było null=True
    recommended_dose = models.CharField(max_length=64)
    opening_date = models.DateField(null=True, blank=True)
    shelf_life = models.IntegerField(default=30)
    usefulness_date = models.DateField()
  #  intended_for = models.ManyToManyField(FamilyMember)

    def __str__(self):
        return self.name


"""A collection of drugs owned by the user."""


class FirstAidKit(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine, null=True)


