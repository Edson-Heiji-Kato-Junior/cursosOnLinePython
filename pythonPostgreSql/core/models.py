from turtle import mode
import uuid

from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    data_cadastro = models.DateField('Data de Cadastro', auto_now_add=True)
    data_alteracao = models.DateField('Ultima Ateração', auto_now=True)
    ativo = models.BooleanField('Ativo?', default = True)
    usuario = models.CharField('Usuário', max_length=40)
    usuario_atualizou = models.CharField('Usuário Atualizou', max_length=40)

    class Meta:
        abstract = True
class Servico(Base):
        ICONE_CHOICES = (
            ('lni-cog'     , 'Engrenagem'),
            ('lni-stats-up', 'Gráfico'   ),
            ('lni-users'   , 'Usuários'  ),
            ('lni-layers'  , 'Design'    ),
            ('lni-mobile'  , 'Mobile'    ),
            ('lni-rocket'  , 'EFoguete'  ),
        )
        servico   = models.CharField('Serviços' , max_length=100)
        descricao = models.TextField('Descrição', max_length=200)
        icone     = models.CharField('Icone'    , max_length=12, choices=ICONE_CHOICES)

        class Meta:
            verbose_name   = 'Serviço'
            verbose_name_plural = 'Serviços'

        def __str__(self):
            return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#' )
    twiter = models.CharField('Twitter', max_length=100, default='#' )
    instagram = models.CharField('Instagram', max_length=100, default='#' )

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class TipoPessoa(Base):
    descricao_tipo_pessoa = models.CharField('Descrição Tipo Pessoa', max_length=100)

    class Meta:
        verbose_name = 'TipoPessoa'
        verbose_name_plural = 'TiposPessoa'

    def __str__(self):
        return self.nome


class Pessoa(Base):
    tipo_pessoa = models.ForeignKey(TipoPessoa)
    razao_nome  = models

    class Meta:
        verbose_name = 'TipoPessoa'
        verbose_name_plural = 'TiposPessoa'

    def __str__(self):
        return self.nome