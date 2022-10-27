from django.contrib import admin
from proc.models import Empresa, Processos,Ativos,Noticias

admin.site.register(Empresa)
admin.site.register(Processos)
admin.site.register(Ativos)
admin.site.register(Noticias)

class EmpresaAdmin(admin.ModelAdmin):
    fields = ['data_cadastro', 'cnpj', 'empresa', 'razao_social', 'responsavel', 'telefone', 'email', 'setor']
    list_display = ('data_cadastro','cnpj','empresa','razao_social','responsavel','telefone','email','setor')


class ProcessosAdmin(admin.ModelAdmin):
    fields = ['data_cadastro', 'processo', 'produto', 'empresa', 'inicio', 'termino', 'tempo_restante','garantia', 'descricao','observacao']
    list_display = ('data_cadastro','processo','produto','empresa','inicio','termino','tempo_restante','garantia','descricao','observacao')

class AtivosAdmin(admin.ModelAdmin):
    fields = ['data_cadastro', 'nr_bem', 'notafiscal', 'ativo', 'marca', 'modelo', 'conta','centro_custo', 'local','fornecedor','data_aquisicao', 'vlr_custo','vlr_residual','obs']
    list_display = ('data_cadastro', 'nr_bem', 'notafiscal', 'ativo', 'marca', 'modelo', 'conta','centro_custo', 'local','fornecedor','data_aquisicao', 'vlr_custo','vlr_residual','obs')

class NoticiasAdmin(admin.ModelAdmin):
    fields = ['data_cadastro', 'data_publicacao', 'titulo', 'texto', 'documento', 'comentario', 'publicado','categoria']
    list_display = ('data_cadastro', 'data_publicacao', 'titulo', 'texto', 'documento', 'comentario', 'publicado','categoria')
# Register your models here.


















