from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Candidato

#Views da página inicial do site Recebe duas possíveis entradas,
#uma sobre o número identificador do candidato e outra com o código do município.
#Se os números digitados foram válidos, redireciona para as páginas de detalhe
#Se o número não for validado, retorna uma mensagem na tela pedido que o usuário tente novamente. 
def home_page_view(request):

	if request.GET.get('num-candidato'):
		num_candidato = request.GET.get('num-candidato')
		print(num_candidato)
		candidato 	  = Candidato.objects.filter(sq_candidato__iexact=num_candidato)
		if candidato.exists():
			return redirect(f'sg={num_candidato}/')
		else: 
			messages.info(request, 'Não encontramos o número do candidato. Por favor, tente novamente.')

	if request.GET.get('municipio'):
		municipio 	= request.GET.get('municipio')
		queryset 	= Candidato.objects.filter(sg_ue=municipio)
		if queryset.exists():
			return redirect(f'sg-ue={municipio}/')
		else: 
			messages.info(request, 'Não encontramos o municipio. Por favor, tente novamente')

	template_name = 'home.html'
	context 	  = {'page_title': 'Candidaturas do RJ'}
	return render(request, template_name, context)

#Página que exibe os detalhes do candidato a partir do número identificador digitado
#na página inicial. 
def detail_candidate_page(request, num):
	candidato 		= Candidato.objects.get(sq_candidato=num)

	template_name 	= 'detail-candidato.html'
	context 		= {
		'page_title' : 'Resultado: '+ candidato.nm_urna_candidato.title(),
		'candidato'	 : candidato,
	}
	return render(request, template_name, context)


#Página que retorna os candidatos eleitos dado o municipio digitado pelo usuário na home page
#Usa a biblioteca Q para obter a queryset do candidato que seja do municipio e também 
#eleito, eleito por média ou eleito por QP
def candidatos_eleitos_municipio_page(request, num):

	queryset 		= Candidato.objects.filter(
		Q(sg_ue=num) & (
			Q(cd_sit_tot_turno=1)| 
			Q(cd_sit_tot_turno=2)| 
			Q(cd_sit_tot_turno=3)
			)
		)
	nm_municipio 	= queryset.first().nm_ue
	template_name 	= 'eleitos-municipio.html'
	context		 	= {

			'page_title': 'Candidatos Eleitos em '+ nm_municipio.title(),
			'queryset'	: queryset,
			'nm_ue'		: nm_municipio,
	}
	return render(request, template_name, context) 
