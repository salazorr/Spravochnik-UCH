from django.contrib import admin
from .models import EducationalInstitution
from .models import Specialty
from .models import Contact


class akudapostupatAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name')


admin.site.register(EducationalInstitution, akudapostupatAdmin)
# admin.site.register(Specialty)
# admin.site.register(Contact)
