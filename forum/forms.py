from django import forms
from django.core.exceptions import ValidationError
from . models import(Evenement, Publication, Matiere, Professeur)

class EvenementForm(forms.ModelForm):
	class Meta:
		model = Evenement
		fields ='__all__'
	


	def clean_theme(self):
		return self.cleaned_data['theme'].title()
	

	class PublicationForm(forms.ModelForm):
		class Meta:
			model = Publication
			fields = '__all__'


		def clean_titre(self):
			return self.cleaned_data['titre'].title()

	class ProfesseurForm(forms.ModelForm):
		class Meta:
			model = Professeur
			fields = '__all__'


		def clean_nom(self):
			return self.cleaned_data['nom'].title()

	class MatiereForm(forms.ModelForm):
		class Meta:
			model = Matiere
			fields = '__all__'


		def clean_matiere(self):
			return self.cleaned_data['matiere'].title()