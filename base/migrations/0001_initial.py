# Generated by Django 4.1.5 on 2023-01-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data Envio')),
            ],
            options={
                'verbose_name': 'Formulário de Contato',
                'verbose_name_plural': 'Formulários de Contatos',
                'ordering': ['-data'],
            },
        ),
    ]
