from django.db import models

# Create your models here.
class Candidato(models.Model):
	dt_geraçao 				= models.CharField(max_length=200, null=True)
	hh_geraçao				= models.CharField(max_length=200, null=True)
	
	ano_eleiçao				= models.IntegerField(null=True)
	cd_tipo_eleicao			= models.IntegerField(null=True)
	nm_tipo_eleicao 		= models.CharField(max_length=200, null=True)
	num_turnos				= models.IntegerField(null=True)
	cd_eleiçao				= models.IntegerField(null=True)
	ds_eleiçao 				= models.CharField(max_length=200, null=True)
	dt_eleiçao				= models.CharField(max_length=200, null=True)
	tp_abrangecia			= models.CharField(max_length=200, null=True)
	sg_uf					= models.CharField(max_length=2, null=True)
	sg_ue					= models.IntegerField(null=True)
	nm_ue					= models.CharField(max_length=200, null=True)
	cd_cargo				= models.IntegerField(null=True)
	ds_cargo				= models.CharField(max_length=200, null=True)
	sq_candidato			= models.IntegerField(null=True)
	nr_candidato			= models.IntegerField(null=True)
	nm_candidato			= models.CharField(max_length=200, null=True)
	nm_urna_candidato		= models.CharField(max_length=200, null=True)
	nm_social_candidato		= models.CharField(max_length=200, null=True)
	nr_cpf_candidato		= models.IntegerField(null=True)
	nm_email				= models.EmailField(null=True)
	cd_situaçao_candidatura	= models.IntegerField(null=True) 
	ds_situaçao_candidatura = models.CharField(max_length=200, null=True)
	cd_detalhe_situaçao_cand= models.IntegerField(null=True)
	ds_detalhe_situaçao_cand= models.CharField(max_length=200, null=True)
	tp_agremiaçao 			= models.CharField(max_length=200, null=True)
	nr_partido				= models.IntegerField(null=True)
	sg_partido				= models.CharField(max_length=10, null=True)
	nm_partido				= models.CharField(max_length=200, null=True)
	sq_colicaçao			= models.IntegerField(null=True)
	nm_coligaçao			= models.CharField(max_length=200, null=True)
	ds_composiçao_coligaçao = models.CharField(max_length=200, null=True)
	cd_nacionalidade		= models.IntegerField(null=True)
	ds_nacionalidade		= models.CharField(max_length=200, null=True)
	sg_uf_nascimento		= models.CharField(max_length=2, null=True)
	cd_municipio_nascimento	= models.IntegerField(null=True)
	nm_municipio_nascimento	= models.CharField(max_length=200, null=True)
	dt_nascimento			= models.CharField(max_length=200, null=True)
	nr_idade_data_posse		= models.IntegerField(null=True)
	nr_titulo_eleitoral_cand= models.IntegerField(null=True)
	cd_genero				= models.IntegerField(null=True)
	ds_genero				= models.CharField(max_length=20, null=True)
	cd_grau_instruçao		= models.IntegerField(null=True)
	ds_grau_instruçao		= models.CharField(max_length=200, null=True)
	cd_estado_civil			= models.IntegerField(null=True)
	ds_estado_civil			= models.CharField(max_length=200, null=True)
	cd_cor_raça				= models.IntegerField(null=True)
	ds_cor_raça				= models.CharField(max_length=200, null=True)
	cd_ocupaçao				= models.IntegerField(null=True)
	ds_ocupaçao				= models.CharField(max_length=200, null=True)
	vr_despesa_max_campanha	= models.DecimalField(max_digits=10000, decimal_places=2, null=True)
	cd_sit_tot_turno		= models.IntegerField(null=True)
	ds_sit_tot_turno		= models.CharField(max_length=200, null=True)
	st_reeleiçao			= models.CharField(max_length=4, null=True)
	st_declarar_bens		= models.CharField(max_length=4, null=True)
	nr_protocolo_candidatura= models.IntegerField(null=True)
	nr_processo				= models.IntegerField(null=True)

	cd_situaçao_candidato_pleito	= models.IntegerField(null=True)
	ds_situaçao_candidato_pleito	= models.CharField(max_length=200, null=True)
	cd_situaçao_candidato_urna		= models.IntegerField(null=True)
	ds_situaçao_candidato_urna		= models.CharField(max_length=200, null=True)
	st_candidato_inserido_urna		= models.CharField(max_length=20, null=True)	

	def __str__(self):
		return self.nm_urna_candidato.title()









