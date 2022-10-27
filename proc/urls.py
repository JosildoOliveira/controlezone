from django.urls import path
from django.urls.conf import include
from proc import views
from .views import index,noticias,EmpresaDetailView,EmpresaListView,AtivosDetailView,AtivosListView,NoticiasListView,NoticiasDetailView,CadastrarNoticia,CadastrarEmpresa,CadastrarProcesso,CadastrarAtivo,AtualizarEmpresa,AtualizarProcesso,AtualizarAtivos,AtualizarNoticias,ExcluirEmpresa,ExcluirProcesso,ExcluirAtivo,ExcluirNoticia,ativos_excel,processos_excel,empresas_excel,noticias_excel,alertaempresa,alertaprocesso,alertaativo,alertanoticia,sendmyemail

urlpatterns=[
    path('',views.index,name='index'),
    path('noticias/',views.noticias,name='noticias'),
    path('empresas/',views.EmpresaListView.as_view(),name='empresas'),
    path('empresa/<int:pk>',views.EmpresaDetailView.as_view(),name='empresa-detail'),
    path('processos/',views.ProcessosListView.as_view(),name='processos'),
    path('processos/<int:pk>',views.ProcessosDetailView.as_view(),name='processos-detail'),
    path('ativos/',views.AtivosListView.as_view(),name='ativos'),
    path('ativos/<int:pk>',views.AtivosDetailView.as_view(),name='ativos-detail'),
    path('noticias-list/',views.NoticiasListView.as_view(),name='noticias-list'),
    path('noticias/<int:pk>',views.NoticiasDetailView.as_view(),name='noticias-detail'),
    path('cadastrarempresa',views.CadastrarEmpresa.as_view(),name='cadastrarempresa'),
    path('cadastrarprocesso',views.CadastrarProcesso.as_view(),name='cadastrarprocesso'),
    path('cadastrarativo',views.CadastrarAtivo.as_view(),name='cadastrarativo'),
    path('cadastrarnoticia',views.CadastrarNoticia.as_view(),name='cadastrarnoticia'),
    path('atualizarempresa/<int:pk>',views.AtualizarEmpresa.as_view(),name='atualizarempresa'),
    path('atualizarprocesso/<int:pk>',views.AtualizarProcesso.as_view(),name='atualizarprocesso'),
    path('atualizarativo/<int:pk>',views.AtualizarAtivos.as_view(),name='atualizarativo'),
    path('atualizarnoticia/<int:pk>',views.AtualizarNoticias.as_view(),name='atualizarnoticia'),
    path('excluirempresa/<int:pk>',views.ExcluirEmpresa.as_view(),name='excluirempresa'),
    path('excluirprocesso/<int:pk>',views.ExcluirProcesso.as_view(),name='excluirprocesso'),
    path('excluirativo/<int:pk>',views.ExcluirAtivo.as_view(),name='excluirativo'),
    path('excluirnoticia/<int:pk>',views.ExcluirNoticia.as_view(),name='excluirnoticia'),
    path('processos-excel',views.processos_excel,name='procesos-excel'),
    path('empresas-excel',views.empresas_excel,name='empresas-excel'),
    path('ativos-excel',views.ativos_excel,name='ativos-excel'),
    path('noticias-excel',views.noticias_excel,name='noticias-excel'),
    path('alertaempresa',views.alertaempresa,name='alerta-empresa'),
    path('alertaprocesso',views.alertaprocesso,name='alerta-processo'),
    path('alertaativo',views.alertaativo,name='alerta-ativo'),
    path('alertanoticia',views.alertanoticia,name='alerta-noticia'),
    path('enviaremail/<int:pk>',views.sendmyemail,name='enviaremail'),
]