# Generated by Django 4.0.6 on 2022-07-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_alter_t_sousorder_real_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_order',
            name='Ord_Status',
            field=models.CharField(choices=[('créée', 'Créée'), ('envoyée', 'Envoyée'), ('payée', 'Payée'), ('en livraison', 'En livraison'), ('livrée', 'Livrée')], default='envoyée', max_length=120),
        ),
        migrations.AlterField(
            model_name='t_orderligne',
            name='OrdLign_Status',
            field=models.CharField(choices=[('créée', 'Créée'), ('envoyée', 'Envoyée'), ('en livraison', 'En livraison'), ('livrée', 'Livrée'), ('payée', 'Payée')], default='envoyée', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='t_sousorder',
            name='SousOrd_status',
            field=models.CharField(choices=[('créée', 'Créée'), ('envoyée', 'Envoyée'), ('payée', 'Payée'), ('en livraison', 'En livraison'), ('livrée', 'Livrée')], default='envoyée', max_length=120),
        ),
    ]
