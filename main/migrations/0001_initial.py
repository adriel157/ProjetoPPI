# Generated by Django 4.2.7 on 2023-11-02 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=20)),
                ('nome_empresa', models.CharField(max_length=200)),
                ('quitado', models.BooleanField(default=False)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stand')),
            ],
        ),
    ]