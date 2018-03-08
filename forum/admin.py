from django.contrib import admin

from . models import(Matiere, Professeur, Publication, Evenement)

admin.site.register(Matiere)
admin.site.register(Professeur)
admin.site.register(Publication)
admin.site.register(Evenement)

