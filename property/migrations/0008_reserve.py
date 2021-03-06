# Generated by Django 3.0.5 on 2020-04-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200404_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
            ],
            options={
                'verbose_name': 'Reservation',
            },
        ),
    ]
