# Generated by Django 4.0.1 on 2022-06-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_remove_t_request_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_user',
            name='U_Statut',
            field=models.CharField(choices=[('autre', 'Autre'), ('professionnel', 'Professionnel'), ('personnel', 'Personnel')], default='autre', max_length=120),
            preserve_default=False,
        ),
    ]
