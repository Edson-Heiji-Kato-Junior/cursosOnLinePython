from django import forms
from django.core.mail.message import EmailMessage
from sqlparse import format


class ContatoForm(forms.Form):
    nome      = forms.CharField( label='Nome'     , max_length=100)
    email     = forms.EmailField(label='E-mail'   , max_length=100)
    assunto   = forms.CharField( label='Assunto'  , max_length=100)
    menssagem = forms.CharField( label='Menssagem', widget=forms.Textarea())

    def send_mail(self):
        nome      = self.cleaned_data['nome']
        email     = self.cleaned_data['email']
        assunto   = self.cleaned_data['assunto']
        menssagem = self.cleaned_data['menssagem']

        conteudo  = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMenssagem: {menssagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@katoecia.com.br',
            to=['contato@katoecia.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()