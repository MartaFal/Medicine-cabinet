"""
URL configuration for medicine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medicine_app import views as med_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', med_views.MainView.as_view(), name=""),
    path('add_medicine/', med_views.AddMedicineView.as_view(), name="add-medicine"),
    path('cabinet/', med_views.MedicineCabinetView.as_view(), name="cabinet"),
    path('add_cabinet/', med_views.NewFirstAidKitView.as_view(), name="new_cabinet"),
    path('medicine_details/<int:medicine_id>/', med_views.MedicineDetailsView.as_view(), name="medicine-details"),
    path('medicine/delete/<int:medicine_id>/', med_views.DeleteMedicineView.as_view(), name="delete-medicine"),
    path('medicine/modify/<pk>/', med_views.MedicineUpdateView.as_view(), name="modify_medicine"),
    path('medicine/duplicate/<int:medicine_id>/', med_views.DuplicateMedicineView.as_view(), name="duplicate"),
    path('login/', med_views.LoginView.as_view(), name="login"),
    path('logout/', med_views.LogOutView.as_view(), name="logout"),
    path('add_user/', med_views.AddUserView.as_view(), name="add-user"),
 #   path('add_family_member/', med_views.AddFamilyMemberView.as_view(), name="add_family"),
 #   path('family/', med_views.FamilyMemberView.as_view(), name="family"),
    path('users_list/', med_views.UsersView.as_view(), name="users_list"),
]

