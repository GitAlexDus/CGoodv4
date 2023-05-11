from django.contrib import admin

# Register your models here.

from .models import Placard

admin.site.register(Placard)

from .models import Casier

admin.site.register(Casier)

from .models import Resa

admin.site.register(Resa)