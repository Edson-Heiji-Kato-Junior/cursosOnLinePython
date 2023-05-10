# Generated by Django 4.1.5 on 2023-04-23 00:34

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_funcionario_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, null=True, upload_to='equipe', variations={'thumb': {'crop': True, 'heigth': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
    ]
