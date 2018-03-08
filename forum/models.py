from django.core.urlresolvers import reverse
from django.db import models




class Professeur(models.Model):
	email = models.EmailField(max_length=255, unique=True,\
		help_text='Saisir une adresse e-mail correcte', blank=True, null=True)
	nom = models.CharField("Nom", max_length=100)
	prenom = models.CharField("Prénom", max_length=150)
	
	def __str__(self):
		return "{} {}".format(self.nom.title(),self.email)


	def get_absolute_url(self):
		return reverse('forum_professeur_detail', kwargs={'id': self.id})

	
	class Meta:
		ordering = ['nom']


	

class Matiere(models.Model):
	matiere = models.CharField("Matière", max_length=200, unique=True)
	professeur = models.ForeignKey(Professeur)
	
	def __str__(self):
		return self.matiere.title()


	def get_absolute_url(self):
		return reverse('forum_matiere_detail', kwargs={'id': self.id})
	
	
	class Meta:
		ordering = ['matiere']

	
class Publication(models.Model):
	titre = models.CharField(max_length=200)
	contenu = models.TextField()
	fichier = models.FileField(upload_to='post_image/pdf/%Y/%m/%D/', blank=True, null=True)
	date_pub = models.DateField("Date Publication", auto_now_add=True)
	professeur = models.ForeignKey(Professeur)
	
	def __str__(self):
		return self.titre.title()


	def get_absolute_url(self):
		return reverse('forum_publication_detail', kwargs={'id': self.id})
	
	class Meta:
		ordering = ['titre', '-date_pub']
		get_latest_by = 'date_pub'



class Evenement(models.Model):
	theme = models.CharField("Thème", max_length=200)
	date_eve = models.DateField("Date", auto_now_add=True)
	texte = models.TextField()
	photo = models.ImageField(upload_to='post_image/%Y/%m/%D/', blank=True, null=True,
		width_field="largeur", height_field="hauteur")
	largeur = models.IntegerField(default=0, blank=True, null=True)
	hauteur = models.IntegerField(default=0,blank=True, null=True)
	fichier = models.FileField(upload_to='post_image/pdf/%Y/%m/%D/', blank=True, null=True)
	
	
	def __str__(self):
		return self.theme.title()


	def get_absolute_url(self):
		return reverse('forum_evenement_detail', kwargs={'id': self.id})
	
	class Meta:
		ordering = ['-date_eve', 'theme']
		get_latest_by = 'date_eve'
