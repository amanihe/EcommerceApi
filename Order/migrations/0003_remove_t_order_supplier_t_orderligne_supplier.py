# Generated by Django 4.0.1 on 2022-06-18 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_alter_t_user_u_statut'),
        ('Order', '0002_t_facture_t_orderligne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_order',
            name='Supplier',
        ),
        migrations.AddField(
            model_name='t_orderligne',
            name='Supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Supplier_Order', to='Accounts.t_user'),
            preserve_default=False,
        ),
    ]
