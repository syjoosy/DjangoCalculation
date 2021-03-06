# Generated by Django 3.1.3 on 2020-11-16 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expressions',
            fields=[
                ('expression_id', models.IntegerField(primary_key=True, serialize=False)),
                ('expression', models.CharField(max_length=100, verbose_name='Формула')),
                ('value', models.CharField(max_length=100, verbose_name='Значения')),
                ('result', models.IntegerField(null=True, verbose_name='Результат')),
            ],
            options={
                'verbose_name': 'Формула',
                'verbose_name_plural': 'Формулы',
            },
        ),
    ]
