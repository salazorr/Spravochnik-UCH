from django.contrib import admin
from .models import Category, Contacts, Specialities, University, Pluses

class UniversityAdmin(admin.ModelAdmin):
    filter_horizontal = ['specialities', 'list_of_pluses']

admin.site.register(Category)
admin.site.register(Contacts)
admin.site.register(Specialities)
admin.site.register(University, UniversityAdmin)
admin.site.register(Pluses)

