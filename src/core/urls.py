from django.urls import path
from .views import (
	home_page_view,
	detail_candidate_page,
	candidatos_eleitos_municipio_page)

app_name = 'core'

urlpatterns = [
    path('', home_page_view, name="home-page"),
    path('sg=<int:num>/', detail_candidate_page, name='detail-candidato'),
    path('sg-ue=<int:num>/', candidatos_eleitos_municipio_page, name='candidatos-eleitos'),
]
