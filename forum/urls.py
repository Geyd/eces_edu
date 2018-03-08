from django.conf.urls import url

from  . views import( publication_detail, publication_list, EvenementCreate,evenement_detail, 
	evenement_list, professeur_detail, ProfesseurList, matiere_detail, matiere_list)

urlpatterns = [
	url(r'^evenement/$', evenement_list, name='forum_evenement_list'),
    url(r'^evenement/(?P<id>[0-9]+)/$', evenement_detail, name='forum_evenement_detail'),
    url(r'^evenement/create/$', EvenementCreate.as_view(), name='forum_evenement_create'),
    url(r'^publication/$', publication_list, name='forum_publication_list'),
    url(r'^publication/(?P<id>[0-9]+)/$', publication_detail, name='forum_publication_detail'),
    url(r'^professeur/$', ProfesseurList.as_view(),  name='forum_professeur_list'),
    url(r'^professeur/(?P<id>[0-9]+)/$', professeur_detail,  name='forum_professeur_detail'),
    url(r'^matiere/$', matiere_list, name='forum_matiere_list'),
    url(r'^matiere/(?P<id>[0-9]+)/$', matiere_detail, name='forum_matiere_detail'),

]