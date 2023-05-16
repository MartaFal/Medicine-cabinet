from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MedicineForm, LoginForm, AddUserForm, DuplicateMedicineForm, NewFirstAidKitForm # FamilyMemberForm
from .models import Medicine, Category, FirstAidKit #FamilyMember
from datetime import timedelta

User = get_user_model()

# Create your views here.


class AddMedicineView(View):

    def get(self, request, *args):
        context = {
            "form": MedicineForm(),
            }
        return render(request, "medicine_app/add_medicine.html", context)

    def post (self, request, *args):
        form = MedicineForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            dosage = form.cleaned_data['dosage']
            contraindications = form.cleaned_data['contraindications']
            comments = form.cleaned_data['comments']
            expiration_date = form.cleaned_data['expiration_date']
            taken_continuously = form.cleaned_data['taken_continuously']
            recommended_dose = form.cleaned_data['recommended_dose']
            opening_date = form.cleaned_data['opening_date']
            shelf_life = form.cleaned_data['shelf_life']

            usefulness_date = opening_date + timedelta(days=shelf_life)
 #           intended_for = form.cleaned_data['intended_for']
            medicine = Medicine.objects.create(
                name=name,
                description=description,
                ingredients=ingredients,
                dosage=dosage,
                contraindications=contraindications,
                comments=comments,
                expiration_date=expiration_date,
                taken_continuously=taken_continuously,
                recommended_dose=recommended_dose,
                opening_date=opening_date,
                shelf_life=shelf_life,
                usefulness_date=usefulness_date,
  #              intednded_for=intended_for
            )
            category_ids = [int(c) for c in category]
            category_objects = Category.objects.filter(id__in=category_ids)
            for category_object in category_objects:
                medicine.category.add(category_object)
            medicine.save()
            return redirect("cabinet")
        else:
            return render(request, "medicine_app/add_medicine.html", context)


class MedicineCabinetView(LoginRequiredMixin, View):
    template_name = "medicine_app/medicine_cabinet_list.html"

    def get(self, request, *args, **kwargs):
        medicines = Medicine.objects.all().order_by('id')
        return render(request, self.template_name, {"medicines": medicines})


class UserMedicineCabinetView(LoginRequiredMixin, View):
    template_name = "medicine_app/medicine_cabinet_list.html"

    def get(self, request, *args, **kwargs):
        medicines = Medicine.objects.all().order_by('id')
        return render(request, self.template_name, {"medicines": medicines})


class NewFirstAidKitView(LoginRequiredMixin, View):
    def get(self, request, *args):
        context = {
            "form": NewFirstAidKitForm(),
        }
        return render(request, "medicine_app/add_first_aid_kit.html", context)

    def post(self, request, *args):
        form = NewFirstAidKitForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            first_aid_kit = FirstAidKit.objects.create(
                name=name,
            )
            first_aid_kit.user = self.request.user
            first_aid_kit.save()
            return redirect("cabinet")
        else:
            return render(request, "medicine_app/add_medicine.html", context)


class MedicineDetailsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        medicine_pk = kwargs['medicine_id']
        try:
            medicine = Medicine.objects.get(pk=medicine_pk)
        except Medicine.DoesNotExist:
            raise Http404
        context = {"medicine": medicine}
        return render(request, "medicine_app/medicine_details.html", context)


class DuplicateMedicineView(View):


    def get(self, request, *args, **kwargs):
        medicine_pk = kwargs['medicine_id']
        medicine = Medicine.objects.get(pk=medicine_pk)
        medicine.pk = None
        medicine.save()
        return redirect("cabinet")

    # def get(self, request, *args, **kwargs):
    #     medicine_pk = kwargs['medicine_id']
    #     medicine = Medicine.objects.get(pk=medicine_pk)
    #     form = DuplicateMedicineForm(instance=medicine)
    #     context = {"form": form}
    #     return render(request, "medicine_app/medicine_duplicate.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     medicine_pk = kwargs['medicine_id']
    #     medicine = Medicine.objects.get(pk=medicine_pk)
    #     new_medicine = Medicine.objects.create(
    #         name=medicine.name,
    #         category=medicine.category,
    #         description=medicine.description,
    #         ingredients=medicine.ingredients,
    #         dosage=medicine.dosage,
    #         contraindications=medicine.contraindications,
    #         comments=medicine.comments,
    #         expiration_date=medicine.expiration_date,
    #         taken_continuously=medicine.taken_continuously,
    #         recommended_dose=medicine.recommended_dose,
    #         opening_date=medicine.opening_date,
    #         shelf_life=medicine.shelf_life,
    #         usefulness_date=medicine.usefulness_date,
    #     )
    #     new_medicine.save()
    #     return redirect("cabinet")

class DeleteMedicineView(View):
    def get(self, request, *args, **kwargs):
        medicine_pk = kwargs['medicine_id']
        medicine = Medicine.objects.get(pk=medicine_pk)
        medicine.delete()
        return redirect("cabinet")


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    fields = '__all__'
    # fields = ['name', 'category', 'description', 'ingredients', 'dosage', 'contraindications',
    #           'comments', 'expiration_date', 'taken_continuously', 'recommended_dose',
    #           'opening_date', 'shelf_life', 'usefulness_date']
    template_name = "medicine_app/medicine_update.html"
    success_url = reverse_lazy('cabinet')



class MainView(View):

    def get(self, request):
        return render(request, "medicine_app/main_page.html")


class AddUserView(View):
    template_name = "medicine_app/form.html"
    form_class= AddUserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

 #           family_member = form.cleaned_data['family_member']
            User.objects.create_user(
                username=username,
                password=password1,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            return redirect('login')
        else:
            return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "medicine_app/form.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                form.add_error(None, "Nieprawidłowy login lub hasło")
                return render(request, self.template_name, {"form": form})
            else:
                login(request, user)
                return redirect("cabinet")

        return render(request, self.template_name, {"form": form})


class UsersView(LoginRequiredMixin, View):
    template_name = "medicine_app/users_list.html"

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('id')
        return render(request, self.template_name, {"users": users})


class LogOutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


# class AddFamilyMemberView(LoginRequiredMixin, View):
#
#     def get(self, request, *args):
#         context = {
#             "form": FamilyMemberForm(),
#             }
#         return render(request, "medicine_app/add_family_member.html", context)
#
#     def post(self, request, *args):
#         form = FamilyMemberForm(request.POST)
#         context = {
#             "form": form,
#         }
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             weight = form.cleaned_data['weight']
#             date_of_birth = form.cleaned_data['date_of_birth']
#             relationship = form.cleaned_data['relationship']
#         #   user = form.cleaned_data['user']
#
#
#             family_member = FamilyMember.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 weight=weight,
#                 date_of_birth=date_of_birth,
#                 relationship=relationship
#             )
#
#             return redirect("cabinet")
#         else:
#             return render(request, "medicine_app/add_family_member.html", context)


# class FamilyMemberView(LoginRequiredMixin, View):
#     template_name = "medicine_app/family_member_list.html"
#
#     def get(self, request, *args, **kwargs):
#         family_members = FamilyMember.objects.all()
#         return render(request, self.template_name, {"family_members": family_members})
