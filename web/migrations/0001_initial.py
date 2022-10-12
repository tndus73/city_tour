# Generated by Django 4.1.1 on 2022-10-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='citytourdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city1', models.CharField(max_length=50)),
                ('city2', models.CharField(max_length=50)),
                ('cos_name', models.CharField(max_length=50)),
                ('cos_info', models.CharField(max_length=200, null=True)),
                ('start_time', models.CharField(max_length=50, null=True)),
                ('close_time', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('number', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
