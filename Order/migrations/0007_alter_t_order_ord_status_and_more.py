# Generated by Django 4.0.1 on 2022-06-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_alter_t_order_ord_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_order',
            name='Ord_Status',
            field=models.CharField(choices=[('créée', 'Créée'), ('envoyée', 'Envoyée'), ('payée', 'Payée'), ('en livraison', 'En livraison'), ('livrée', 'Livrée')], default='created', max_length=120),
        ),
        migrations.AlterField(
            model_name='t_orderligne',
            name='OrdLign_Status',
            field=models.CharField(choices=[('créée', 'Créée'), ('envoyée', 'Envoyée'), ('acceptée', 'Acceptée'), ('annulée', 'Annulée')], default='created', max_length=120, null=True),
        ),
    ]
