# Generated by Django 5.1.6 on 2025-02-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('telefone', models.TextField(null=True)),
            ],
        ),
    ]
