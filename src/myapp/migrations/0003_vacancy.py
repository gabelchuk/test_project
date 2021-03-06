# Generated by Django 3.1.6 on 2021-04-08 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210402_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=300, verbose_name='Оглавление вакансии')),
                ('company', models.CharField(max_length=300, verbose_name='Компания')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('timestamp', models.TimeField(auto_now_add=True)),
                ('citi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.citi', verbose_name='Город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.language', verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
