# Generated by Django 2.2.6 on 2019-10-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RudnikModel',
            fields=[
                ('RudnikLevel', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('RudnikPrice', models.IntegerField(default=50)),
                ('RudnikBonus', models.IntegerField(default=2)),
            ],
        ),
    ]