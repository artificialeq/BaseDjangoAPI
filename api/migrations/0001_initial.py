# Generated by Django 2.2.1 on 2019-05-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('profile_picture', models.CharField(max_length=150)),
                ('about_me', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=500)),
            ],
        ),
    ]