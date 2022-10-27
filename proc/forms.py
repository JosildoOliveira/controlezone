from django import ModelForm
from proc.models import Empresa,Processos,Ativos

class CadastrarEmpresa(ModelForm):
    class Meta:
        model=Empresa
        fields=['data_cadastro','cnpj','empresa','processo','razao_social','responsavel','telefone','email','setor']

class CadastrarProcessos(ModelForm):
    class Meta:
        model=Processos
        fields=['data_cadastro','processo','produto','inicio','termino','garantia','tempo_restante','descricao','observacao']

class CadastrarAtivos(ModelForm):
    class Meta:
        model=Ativos
        fiedlds=['data_cadastro', 'nr_bem', 'ativo', 'marca', 'modelo', 'conta', 'centro_custo','local', 'fornecedor','data_aquisicao','vlr_custo','vlr_residual_desc']