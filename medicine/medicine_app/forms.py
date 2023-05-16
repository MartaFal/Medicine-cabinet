from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Medicine # FamilyMember,
from datetime import datetime

User = get_user_model()


# Form which add new medicine to First Aid Kit.


class MedicineForm(forms.Form):

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

    name = forms.CharField(label="Nazwa", max_lenth=128)
  #  category = forms.ChoiceField(
    category = forms.MultipleChoiceField(
        label="Kategoria",
        widget=forms.CheckboxSelectMultiple,
        choices=DISEASE_CHOICE,
#    widget= forms.SelectMultiple,
    )
    description = forms.CharField(label="Zastosowanie", widget=forms.Textarea(attrs={'class': 'myfield'}), blank=True)  # zastosowanie
    ingredients = forms.CharField(label="Składniki", widget=forms.Textarea(attrs={'class': 'myfield'}), blank=True)
    dosage = forms.CharField(label="Dawkowanie", max_length=255)
    contraindications = forms.CharField(label="Przeciwwskazania", max_length=255)  # przeciwwskaznaia
    comments = forms.CharField(label="Uwagi", max_length=128)
    expiration_date = forms.DateField(
        label="Data ważności",
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
       )
    taken_continuously = forms.BooleanField(label="Przyjmowany na stałe")
    recommended_dose = forms.CharField(label="Rekomendowana dawka", max_length=64)
    opening_date = forms.DateField(
        label="Data otwarcia",
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=False
    )
    shelf_life = forms.IntegerField(label="Czas przydatności od otwarcia w dniach")
#    intended_for = forms.CharField(label="Przeznaczony dla:")

class DuplicateMedicineForm(forms.Form):
    class Meta:
        model = Medicine
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, attr={"type": "password"})


class AddUserForm(forms.Form):
    username = forms.CharField(max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=128)
  # #  age = forms.IntegerField(label="Wiek")
  #  # weight = forms.IntegerField()
    email = forms.EmailField()
  #   family_member = forms.CharField()  #pole wyboru członka rodziny
  #  permissions = forms.ChoiceField(choices=(
  #      ("user_add", "Add user perm"),
 #       ("user_change", "Change user perm")
  #  ) )

    def clean(self):
        # cd - cleandata
        cd = super().clean()
        pass1 = cd.get('password1')
        pass2 = cd.get('password2')
        username =cd.get('username')
        if pass1 != pass2:
            raise ValidationError("Hasła nie są takie same")
        if username and User.objects.filter(username=username).exists():
            raise ValidationError("Użytkownik już istnieje")


class NewFirstAidKitForm(forms.Form):
    name=forms.CharField(label="Nazwa", max_length=64)

# class FamilyMemberForm(forms.Form):
#     class Meta:
#         model = FamilyMember
#         fields = ['first_name', 'last_name', 'weight', 'date_of_birth', 'relationship']