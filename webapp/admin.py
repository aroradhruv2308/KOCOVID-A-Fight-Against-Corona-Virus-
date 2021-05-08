from django.contrib import admin
from webapp.models import Contact
from webapp.models import Help
from webapp.models import Plasma
from webapp.models import Oxygen
from webapp.models import Bed
from webapp.models import nHelp




# Register your models here.
admin.site.register(Contact)
admin.site.register(Help)
admin.site.register(Plasma)
admin.site.register(Bed)
admin.site.register(Oxygen)
admin.site.register(nHelp)



