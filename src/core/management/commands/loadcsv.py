from django.core.management.base import BaseCommand

import argparse
import csv

from core.models import Candidato


class Command(BaseCommand):
	help = 'Load CSV to models database'

	def add_arguments(self, parser):
		parser.add_argument('--path', type=str)

	def handle(self, *args, **kwargs):
		path 	= kwargs['path']

		with open(path) as file:
			reader = csv.reader(file, delimiter=';')
			next(reader, None)

			for row in reader:
				cand 	= Candidato.objects.create(
					dt_geraçao=row[0],
					hh_geraçao=row[1],
					ano_eleiçao=row[2],
					cd_tipo_eleicao=row[3],
					nm_tipo_eleicao=row[4],
					num_turnos=row[5],
					cd_eleiçao=row[6],
					ds_eleiçao=row[7],
					dt_eleiçao=row[8],
					tp_abrangecia=row[9],
					sg_uf=row[10],
					sg_ue=row[11],
					nm_ue=row[12],
					cd_cargo=row[13],
					ds_cargo=row[14],
					sq_candidato=row[15],
					nr_candidato=row[16],
					nm_candidato=row[17],
					nm_urna_candidato=row[18],
					nm_social_candidato=row[19],
					nr_cpf_candidato=row[20],
					nm_email=row[21],
					cd_situaçao_candidatura=row[22],
					ds_situaçao_candidatura=row[23],
					cd_detalhe_situaçao_cand=row[24],
					ds_detalhe_situaçao_cand=row[25],
					tp_agremiaçao=row[26],
					nr_partido=row[27],
					sg_partido=row[28],
					nm_partido=row[29],
					sq_colicaçao=row[30],
					nm_coligaçao=row[31],
					ds_composiçao_coligaçao=row[32],
					cd_nacionalidade=row[33],
					ds_nacionalidade=row[34],
					sg_uf_nascimento=row[35],
					cd_municipio_nascimento=row[36],
					nm_municipio_nascimento=row[37],
					dt_nascimento=row[38],
					nr_idade_data_posse=row[39],
					nr_titulo_eleitoral_cand=row[40],
					cd_genero=row[41],
					ds_genero=row[42],
					cd_grau_instruçao=row[43],
					ds_grau_instruçao=row[44],
					cd_estado_civil=row[45],
					ds_estado_civil=row[46],
					cd_cor_raça=row[47],
					ds_cor_raça=row[48],
					cd_ocupaçao=row[49],
					ds_ocupaçao=row[50],
					vr_despesa_max_campanha=row[51],
					cd_sit_tot_turno=row[52],
					ds_sit_tot_turno=row[53],
					st_reeleiçao=row[54],
					st_declarar_bens=row[55],
					nr_protocolo_candidatura=row[56],
					nr_processo=row[57],
					cd_situaçao_candidato_pleito=row[58],
					ds_situaçao_candidato_pleito=row[59],
					cd_situaçao_candidato_urna=row[60],
					ds_situaçao_candidato_urna=row[61],
					st_candidato_inserido_urna=row[62])	