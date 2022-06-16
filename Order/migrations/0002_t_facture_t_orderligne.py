# Generated by Django 4.0.1 on 2022-06-14 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_Facture',
            fields=[
                ('Fact_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Fact_Num', models.CharField(max_length=150)),
                ('Fact_OrderCost', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('Fact_Discount', models.IntegerField()),
                ('Fact_CostFinal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('Fact_Type', models.CharField(max_length=150)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='T_OrderLigne',
            fields=[
                ('OrdLign_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Ord_Qte', models.IntegerField()),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.t_order')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_product')),
            ],
        ),
    ]
