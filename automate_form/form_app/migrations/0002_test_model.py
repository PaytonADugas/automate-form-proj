# Generated by Django 3.2.3 on 2021-05-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.CharField(max_length=256)),
                ('is_employed', models.BooleanField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]