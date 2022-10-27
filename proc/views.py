from django.shortcuts import render
import proc.models
from proc.models import Empresa,Processos,Ativos,Noticias
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
    num_processos=Processos.objects.all().count()
    num_empresas=Empresa.objects.all().count()
    num_processos_vencer=Processos.objects.filter(tempo_restante=10).count()

    context={
        'Número de Processos': num_processos,
        'Número de Empresas': num_empresas,
        'Número de Processos a Vencer': num_processos_vencer,
    }

    return render(request,'index.html',context=context)
#Fim da Página Index

#Início da Página Noticias Conselho
def noticias(request):

    return render(request,'noticias.html')

#Fim da Página de Notícias



# Criação de Lista Detalhada de Dados

# Mensagem para usuário não Autorizado
def alertaempresa(request):

    return render(request,'alerta-empresa.html')

def alertaprocesso(request):

    return render(request,'alerta-processo.html')

def alertaativo(request):

    return render(request,'alerta-ativo.html')

def alertanoticia(request):

    return render(request,'alerta-noticia.html')
# Fim da mensagem para o não Autorizado


from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#from braces.views import GroupRequiredMixin
#from django.urls import reverse_lazy

class EmpresaListView(LoginRequiredMixin,generic.ListView):
    model = Empresa
    paginate_by = 10

    def get_queryset(self):
        txt_empresa = self.request.GET.get('empresa')

        if txt_empresa:
            empresa=Empresa.objects.filter(empresa__icontains=txt_empresa)
        else:
            empresa=Empresa.objects.all()

        return empresa


from datetime import datetime,timedelta

def EmpresaDataList(request):
    currentDateTime = datetime.datetime.now()
    hoje = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia = date.strftime("%d")


    context={
        'hoje':hoje,
    }

    return render(request,'empresa_list.html',context=context)


class EmpresaDetailView(LoginRequiredMixin,generic.DetailView):
    model = Empresa
    paginate_by=20

    def empresa_detail_view(request,primary_key):
        try:
            empresa=Empresa.objects.get(pk=primary_key)
        except Empresa.DoesNotExist:
            raise Http404('Empresa Não Existe')
        return render(request,'empresa/empresa_detail.html',context={'empresa':empresa})

class ProcessosListView(LoginRequiredMixin,generic.ListView):
    model = Processos
    paginate_by = 10

    def get_queryset(self):

        txt_processo = self.request.GET.get('processo')
        if txt_processo:
            processo=Processos.objects.filter(processo__icontains=txt_processo)
        else:
            processo=Processos.objects.all()
        return processo

class ProcessosDetailView(LoginRequiredMixin,generic.DetailView):
    model = Processos
    paginate_by=20

    def processo_detail_view(request,primary_key):
        try:
            processo=Processos.objects.get(pk=primary_key)
        except Processos.DoesNotExist:
            raise Http404('Empresa Não Existe')
        return render(request,'processo/processo_detail.html',context={'processo':processo})


# Início da Classe Ativo
class AtivosListView(LoginRequiredMixin,generic.ListView):
    model = Ativos
    paginate_by = 10

    def get_queryset(self):

        txt_ativo=self.request.GET.get('ativo')
        if txt_ativo:
            ativo=Ativos.objects.filter(ativo__icontains=txt_ativo)
        else:
            ativo=Ativos.objects.all()
        return ativo

class AtivosDetailView(LoginRequiredMixin,generic.DetailView):
    model = Ativos
    paginate_by = 20

    def ativo_detail_view(request,primary_key):
        try:
            ativo=Ativos.objects.get(pk=primary_key)
        except Ativos.DoesNotExist:
            raise Http404('Ativo não Existe')
        return render(request,'ativo/ativo_detail.html',context={'ativo':ativo})


#Fim da Classe Ativo

#Início da Classe Noticias

class NoticiasListView(LoginRequiredMixin,generic.ListView):
    model = Noticias
    paginate_by = 3

    def get_queryset(self):

        txt_noticias=self.request.GET.get('noticias')
        if txt_noticias:
            noticia=Noticias.objects.filter(ativo__icontains=txt_noticias)
        else:
            noticia=Noticias.objects.all()
        return noticia

class NoticiasDetailView(LoginRequiredMixin,generic.DetailView):
    model = Noticias
    paginate_by = 3

    def noticia_detail_view(request,primary_key):
        try:
            noticia=Noticias.objects.get(pk=primary_key)
        except Noticias.DoesNotExist:
            raise Http404('Ativo não Existe')
        return render(request,'noticia/noticia_detail.html',context={'noticia':noticia})

#Fim da Classe Notícias

#Fazendo Download de Arquivo de Noticias

def download_view(request):
 from django.http import HttpResponse, Http404
 from os import path
 import mimetypes

 arquivo = "%s/%s" % (settings.MEDIA_ROOT, request.GET.get('filename'), )

 if not (path.exists(arquivo)):
  raise Http404()

 mimetype, encoding = mimetypes.guess_type(arquivo)

 if mimetype is None:
  mimetype = 'application/force-download'

 file = arquivo.split("/")[-1]

 response = HttpResponse(open(arquivo, 'r').read())
 response['Content-Type'] = mimetype
 response['Pragma'] = 'public'
 response['Expires'] = '0'
 response['Cache-Control'] = 'must-revalidate, post-check=0, pre-check=0'
 response['Content-Disposition'] = 'attachment; filename=%s' % file
 response['Content-Transfer-Encoding'] = 'binary'
 response['Content-Length'] = str(path.getsize(arquivo))
 return response


#Ffim do Download

#Views dos Formulários
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from proc.models import Empresa,Processos,Ativos,Noticias
from braces.views import GroupRequiredMixin

#Formulário de Cadastro
class CadastrarEmpresa(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('alerta-empresa')
    group_required=u"Controladores"
    model = Empresa
    fields=['data_cadastro','cnpj','empresa','processo','razao_social','responsavel','telefone','email','setor']
    success_url = reverse_lazy('cadastrarempresa')


class CadastrarProcesso(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('alerta-processo')
    group_required = u"Controladores"
    model = Processos
    fields = ['data_cadastro', 'processo', 'produto', 'inicio', 'termino', 'garantia','descricao', 'observacao','anexo']
    success_url = reverse_lazy('cadastrarprocesso')

class CadastrarAtivo(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('alerta-ativo')
    group_required = u"Controladores"
    model = Ativos
    fields = ['data_cadastro', 'nr_bem','notafiscal','ativo', 'marca', 'modelo', 'conta', 'centro_custo', 'local', 'fornecedor','data_aquisicao', 'vlr_custo', 'vlr_residual_desc','obs']
    success_url = reverse_lazy('cadastrarativo')

class CadastrarNoticia(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('alerta-noticia')
    group_required = u"Controladores"
    model = Noticias
    fields = ['data_publicacao','titulo','texto', 'documento', 'publicado', 'comentario']
    success_url = reverse_lazy('cadastrarnoticia')

# Formulário Atualização

class AtualizarEmpresa(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('alerta-empresa')
    group_required = u"Controladores"
    model = Empresa
    fields = ['data_cadastro','cnpj','empresa','processo','razao_social','responsavel','telefone','email','setor']
    success_url = reverse_lazy('empresas')

class AtualizarProcesso(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('alerta-processo')
    group_required = u"Controladores"
    model = Processos
    fields = ['data_cadastro', 'processo', 'produto', 'inicio', 'termino', 'garantia','descricao', 'observacao','anexo' ]
    success_url = reverse_lazy('processos')

class AtualizarAtivos(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('alerta-ativo')
    group_required = u"Controladores"
    model = Ativos
    fields = ['data_cadastro', 'nr_bem','notafiscal','ativo', 'marca', 'modelo', 'conta', 'centro_custo', 'local', 'fornecedor','data_aquisicao', 'vlr_custo', 'vlr_residual_desc','obs']
    success_url = reverse_lazy('ativo')

class AtualizarNoticias(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('alerta-noticia')
    group_required = u"Controladores"
    model = Noticias
    fields = ['data_publicacao','titulo','texto', 'documento', 'publicado', 'comentario']
    success_url = reverse_lazy('noticias-list')

# Formulário Exclusão

class ExcluirEmpresa(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('alerta-empresa')
    group_required = u"Controladores"
    model = Empresa
    success_url = reverse_lazy('empresas')

class ExcluirProcesso(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('alerta-processo')
    group_required = u"Controladores"
    model = Processos
    success_url = reverse_lazy('processos')

class ExcluirAtivo(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('alerta-ativo')
    group_required = u"Controladores"
    model = Ativos
    success_url = reverse_lazy('ativo')

class ExcluirNoticia(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('alerta-noticia')
    group_required = u"Controladores"
    model = Noticias
    success_url = reverse_lazy('noticia')

#Gera Planilha Excel para Download do Mês Corrente dos Processos

import xlwt
import datetime
from django.shortcuts import render
from django.http import HttpResponse

def processos_excel(request):

    #Criando filtro para Processos por data
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia=date.strftime("%d")


    # Fim do Filtro

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=Planilha-Processos_'+f'{date}'+'.xls'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Processos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 20
    ws.col(2).width = 256 * 30
    ws.col(3).width = 256 * 30
    ws.col(4).width = 256 * 15
    ws.col(5).width = 256 * 15
    ws.col(6).width = 256 * 20
    ws.col(8).width = 256 * 60
    ws.col(9).width = 256 * 40


    columns = ['CADASTRO', 'PROCESSO', 'PRODUTO', 'EMPRESA', 'INÍCIO', 'TÉRMINO', 'GARANTIA (MESES)', 'DESCRIÇÃO', 'OBSERVAÇÃO']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Processos.objects.filter().values_list('data_cadastro','processo','produto','empresa','inicio','termino', 'garantia','descricao','observacao')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Fim do Excel Download

# Gera Planilha Excel para Download de Ativos
import xlwt
import datetime
from django.shortcuts import render
from django.http import HttpResponse

def ativos_excel(request):

    #Criando filtro para Processos por data
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia=date.strftime("%d")


    # Fim do Filtro

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=Planilha-Ativos'+f'{date}'+'.xls'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Ativos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 20
    ws.col(2).width = 256 * 20
    ws.col(3).width = 256 * 20
    ws.col(4).width = 256 * 20
    ws.col(5).width = 256 * 20
    ws.col(6).width = 256 * 20
    ws.col(7).width = 256 * 20
    ws.col(8).width = 256 * 20
    ws.col(9).width = 256 * 20
    ws.col(10).width = 256 * 20
    ws.col(11).width = 256 * 20


    columns = ['CADASTRO', 'NR. BEM','NOTA FISCAL', 'ATIVO', 'MARCA', 'MODELO', 'CONTA', 'CENTRO CUSTO','LOCAL','FORNECEDOR','AQUISIÇÃO','VLR CUSTO','VLR RESIDUAL DESCONTADO','OBSERVAÇÃO']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Ativos.objects.filter().values_list('data_cadastro','nr_bem','notafiscal', 'ativo', 'marca', 'modelo', 'conta', 'centro_custo','local','fornecedor','data_aquisicao','vlr_custo','vlr_residual_desc','obs')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Fim do Excel Download

# Gera Planilha Excel para Download do Mês Corrente das Empresas
import xlwt
import datetime
from django.shortcuts import render
from django.http import HttpResponse

def empresas_excel(request):

    #Criando filtro para Processos por data
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia=date.strftime("%d")


    # Fim do Filtro

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=Planilha-Empresas'+f'{date}'+'.xls'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Empresas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 20
    ws.col(2).width = 256 * 30
    ws.col(3).width = 256 * 30
    ws.col(4).width = 256 * 20
    ws.col(5).width = 256 * 20
    ws.col(6).width = 256 * 50
    ws.col(7).width = 256 * 20


    columns = ['CADASTRO', 'CNPJ', 'EMPRESA', 'RAZÃO', 'RESPONSÁVEL', 'TELEFONE', 'EMAIL','SETOR']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Empresa.objects.filter().values_list('data_cadastro','cnpj','empresa','razao_social','responsavel','telefone','email','setor')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Fim do Excel Download

# Gera Planilha Excel para Download do Mês Corrente das Noticias
import xlwt
import datetime
from django.shortcuts import render
from django.http import HttpResponse

def noticias_excel(request):

    #Criando filtro para Processos por data
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia=date.strftime("%d")


    # Fim do Filtro

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=Planilha-Documentos'+f'{date}'+'.xls'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Documentos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 20
    ws.col(2).width = 256 * 30
    ws.col(3).width = 256 * 30
    ws.col(4).width = 256 * 20
    ws.col(5).width = 256 * 20
    ws.col(6).width = 256 * 50
    ws.col(7).width = 256 * 20


    columns = ['CADASTRO', 'TÍTULO', 'TEXTO', 'CATEGORIA']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Noticias.objects.filter().values_list('data_cadastro','titulo','texto','categoria')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Fim do Excel Download



# Envio de Email Programado

from django.shortcuts import render
import proc.models
from proc.models import Empresa,Processos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


from django.conf import settings
import schedule
import time
from django.core.mail import EmailMessage
from .models import Processos,Empresa
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages


def sendmyemail(request,*args,**kwargs):
    # Criando filtro para Laudos por data
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    mes = date.strftime("%m")
    dia = date.strftime("%d")
    # Fim do Filtro
    # Pegando cada registro


    pk = kwargs.get('pk')
    processos = get_object_or_404(Processos, pk=pk)

    terminos=processos.termino

    terminos_dia= (terminos.strftime("%d"))
    terminos_mes= (terminos.strftime("%m"))
    terminos_ano = (terminos.strftime("%Y"))

    term_dia=int(terminos_dia)
    term_mes=int(terminos_mes)
    term_ano=int(terminos_ano)

    resultado = str(365*(term_ano-int(year))+30*(term_mes-int(mes))+(term_dia-int(dia)))
    res=int(resultado)

    # import email

    if res == 33:
        subject, from_email, to = 'Aviso de Vencimento de Contrato', 'josildo.oliveira@grupostorm.com', 'jpoliv2001@yahoo.com.br'
        text_content = 'Faltam aproximadamente ' + str(
            365 * (term_ano - int(year)) + 30 * (term_mes - int(mes)) + (term_dia - int(dia))) + \
                       ' dias para o encerramento do contrato sob número de' \
                       ' Processo: ' \
                       + str(processos.processo) + \
                       ' | Produto: ' + str(processos.produto) + \
                       ' | Empresa: ' + str(processos.empresa) + '.'
        html_content = 'Prezados Segue teste de envio do dia.'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "html/html_content")

        msg.send()
        messages.success(request,'Atualização bem sucedida!')
        # Envio de email II
    else:
        #return HttpResponse(msgBox)
        return HttpResponse('Não foi enviado e-mail')

    schedule.every(1).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Fim do Envio de E-mail Programado


