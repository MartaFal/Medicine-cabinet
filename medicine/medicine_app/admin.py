from django.contrib import admin

# Register your models here.
from .models import Medicine, Category, FirstAidKit #FamilyMember,


admin.site.register(Medicine)
admin.site.register(Category)
#admin.site.register(FamilyMember)
admin.site.register(FirstAidKit)

