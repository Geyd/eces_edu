from django.shortcuts import(get_object_or_404, redirect, render)
from django.views.generic import View


from .utils import ObjectCreateMixin
from .models import(Professeur, Matiere, Publication, Evenement)
from .forms import EvenementForm

def evenement_list(request):
	return render(request, 'forum/evenement_list.html',{'evenement_list': Evenement.objects.all()})


def evenement_detail(request, id):
	evenement = get_object_or_404(Evenement, id__exact=id)
	return render(request, 'forum/evenement_detail.html', {'evenement': evenement})

class EvenementCreate(ObjectCreateMixin, View):
	form_class = EvenementForm
	template_name = 'forum/evenement_form.html'


def publication_list(request):
	return render(request, 'forum/publication_list.html',{'publication_list': Publication.objects.all()})

def publication_detail(request, id):
	publication = get_object_or_404(Publication, id__exact=id)
	return render(request, 'forum/publication_detail.html', {'publication': publication})


def matiere_list(request):
	return render(request, 'forum/matiere_list.html',{'matiere_list': Matiere.objects.all()})

def matiere_detail(request, id):
	matiere = get_object_or_404(Matiere, id__exact=id)
	return render(request, 'forum/matiere_detail.html', {'matiere': matiere})


class ProfesseurList(View):
	parent_template = 'forum/professeur_list.html'
	def get(self, request):
		return render(request, self.parent_template, {'professeur_list': Professeur.objects.all()})


def professeur_detail(request, id):
	professeur = get_object_or_404(Professeur, id__exact=id)
	return render(request, 'forum/professeur_detail.html',{'professeur': professeur})