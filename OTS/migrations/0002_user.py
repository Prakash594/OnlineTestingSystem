# Generated by Django 3.2.2 on 2022-05-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('usernsme', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('realname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=12)),
                ('role', models.CharField(max_length=12)),
            ],
        ),
    ]
