# Generated by Django 4.2.1 on 2023-06-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Mail del profesor')),
                ('celular', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]