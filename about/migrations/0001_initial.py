# Generated by Django 4.2.2 on 2023-07-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tname', models.CharField(max_length=30)),
                ('temail', models.CharField(max_length=20)),
                ('tedu', models.CharField(max_length=40)),
            ],
        ),
    ]
