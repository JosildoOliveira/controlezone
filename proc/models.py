from django.db import models
from django.urls import reverse

# Tabela de Empresas
class Empresa(models.Model):
    data_cadastro=models.DateField(verbose_name='Data de Cadastro',blank=False,null=False)
    cnpj=models.CharField(verbose_name='CNPJ',max_length=30)
    empresa=models.CharField(verbose_name='Nome Fantasia',max_length=100)
    processo = models.CharField(verbose_name='Processo', max_length=100,null=True)
    razao_social=models.CharField(verbose_name='Razão Social',max_length=100)
    responsavel=models.CharField(verbose_name='Responsável',max_length=150)
    telefone=models.CharField(verbose_name='Telefone', max_length=20)
    email=models.EmailField(verbose_name='E-mail')
    CARREGAR_SETOR=(
        ('Alimentação','Alimentação'),
        ('Transporte', 'Transporte'),
        ('Saúde', 'Saúde'),
        ('Comércio', 'Comércio'),
        ('Comunicações', 'Comunicações'),
        ('Serviços financeiros', 'Serviços financeiros'),
        ('TI', 'TI'),
        ('Outros', 'Outros'),
    )
    setor=models.CharField(
        max_length=50,
        choices=CARREGAR_SETOR,
        blank=True,
        null=True,
        default='----'
    )
    class Meta:
        ordering=['-data_cadastro','empresa']

    def __str__(self):
        return self.processo

    def get_absolute_url(self):
        return reverse('empresa-detail',args=[str(self.id)])

# Fim da Tabela de Empresas

# Tabela de Processos
class Processos(models.Model):
    data_cadastro=models.DateField(verbose_name='Data de Cadastro',blank=False,null=False)
    processo = models.ForeignKey('Empresa',on_delete=models.CASCADE)
    produto=models.CharField(verbose_name='Produto',max_length=200)
    #empresa=models.ForeignKey('Empresa',on_delete=models.SET_NULL, null=True)
    inicio=models.DateField(verbose_name='Data de Início',blank=False,null=False)
    termino=models.DateField(verbose_name='Data de Término',blank=False,null=False)
    garantia=models.IntegerField(verbose_name='Garantia',null=True,blank=True,help_text='Em meses')
    tempo_restante=models.IntegerField(verbose_name='Tempo restante',null=True,blank=True)
    descricao=models.TextField(verbose_name='Descrição',null=True,blank=True)
    observacao=models.TextField(verbose_name='Observação',null=True,blank=True)
    anexo=models.FileField(verbose_name='Arquivo do Processo',null=True,blank=True)

    class Meta:
        ordering=['inicio','data_cadastro']

    def get_absolute_url(self):
        return reverse('processos-detail',args=[str(self.id)])


# Fim da Tabela de Processos

# Tabela de Ativos
class Ativos(models.Model):
    data_cadastro=models.DateField(verbose_name='Data de Cadastro',blank=False,null=False)
    nr_bem=models.CharField(verbose_name='Patrimônio',max_length=100)
    notafiscal=models.CharField(verbose_name='Nota Fiscal',max_length=50,blank=True)
    ativo=models.CharField(verbose_name='Ativo',max_length=200,blank=True)
    marca=models.CharField(verbose_name='Marca',max_length=100)
    modelo=models.CharField(verbose_name='Modelo',max_length=100)
    CONTA_DOTA=(
        ('Moveis e Utensilios','Moveis e Utensilios'),
        ('Equipamentos de Informática', 'Equipamentos de Informática'),
        ('Veículos', 'Veículos'),
        ('Máquinas e Equipamentos', 'Máquinas e Equipamentos'),
    )
    conta=models.CharField(
        max_length=200,
        choices=CONTA_DOTA,
        verbose_name='Dotação',
        blank=True,
        null=True,
        default='------'
    )
    CENTRO_CUSTO = (
        ('Secretaria', 'Secretaria'),
        ('Administrativo', 'Administrativo'),
        ('Técnico', 'Técnico'),
    )
    centro_custo = models.CharField(
        max_length=100,
        choices=CENTRO_CUSTO,
        blank=True,
        null=True,
        default='Administrativo'
    )
    LOCAL = (
        ('Sala Administrativo', 'Sala Administrativo'),
        ('Sala Técnico', 'Sala Técnico'),
        ('Sala Reunião', 'Sala Reunião'),
        ('Área Comum', 'Área Comum'),
        ('Diretoria Administrativa', 'Diretoria Administrativa'),
        ('Diretoria Técnica', 'Diretoria Técnica'),
        ('Sala Secretário Executivo', 'Sala Secretário Executivo'),

    )
    local = models.CharField(
        max_length=100,
        choices=LOCAL,
        blank=True,
        null=True,
        default='Sala Administrativo'
    )
    fornecedor=models.ForeignKey('Empresa',on_delete=models.SET_NULL, null=True, verbose_name='Fornecedor')
    data_aquisicao=models.DateField(verbose_name='Data de Aquisição',blank=False,null=False)
    vlr_custo=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Valor de Custo')
    vlr_residual_desc=models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Vlr Residual de Descarte')
    obs=models.TextField(verbose_name='Observação',null=True,blank=True)

    class Meta:
        ordering=['data_cadastro','nr_bem']

    def __str__(self):
        return self.ativo

    def get_absolute_url(self):
        return reverse('ativos-detail',args=[str(self.id)])

# Fim da Tabela de Ativos

# Tabela de Noticias

class Noticias(models.Model):
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro', blank=False, null=False)
    data_publicacao = models.DateField(verbose_name='Data de Publicação', blank=False, null=False)
    titulo = models.CharField(verbose_name='Título', max_length=100)
    texto = models.TextField(verbose_name='Texto')
    documento = models.FileField(verbose_name='Documento', help_text='Breve descrição do documento',upload_to='media',blank=True,null=True)
    comentario = models.TextField(verbose_name='Comentário',blank=True,null=True)
    publicado = models.BooleanField(default=False)
    CATEGORIA_PUB = (
        ('Contas', 'Contas'),
        ('Contratos', 'Contratos'),
        ('Prestação de Contas', 'Prestação de Contas'),
        ('Informativo', 'Informativo'),
    )
    categoria = models.CharField(
        max_length=100,
        choices=CATEGORIA_PUB,
        blank=True,
        null=True,
        default='----'
    )

    class Meta:
        ordering = ['-data_cadastro']

    def __str__(self):
        return f'{self.id}{self.titulo}'

    def get_absolute_url(self):
        return reverse('noticias-detail',args=[str(self.id)])

#Fim da Tabela Noticias