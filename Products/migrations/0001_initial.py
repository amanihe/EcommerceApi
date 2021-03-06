# Generated by Django 4.0.1 on 2022-05-19 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_Category',
            fields=[
                ('Categ_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Categ_Name', models.CharField(max_length=100, unique=True)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
                ('Categ_Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Products.t_category')),
            ],
        ),
        migrations.CreateModel(
            name='T_Product',
            fields=[
                ('Prod_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Prod_Name', models.CharField(max_length=150)),
                ('Prod_Description', models.TextField(default='Empty description.', max_length=500)),
                ('Prod_Marque', models.TextField(max_length=500)),
                ('Prod_Price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('Prod_Quantity', models.IntegerField(default=10)),
                ('Prod_Img', models.CharField(default='', max_length=100, unique=True)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_category')),
            ],
        ),
        migrations.CreateModel(
            name='T_ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_product')),
            ],
        ),
        migrations.CreateModel(
            name='T_Characteristic',
            fields=[
                ('Carec_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Carecteristique', models.CharField(max_length=100, unique=True)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='Products.T_Category')),
            ],
        ),
        migrations.CreateModel(
            name='T_Carac_Product',
            fields=[
                ('Carec_Prod_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Carac_Detail', models.CharField(max_length=100, unique=True)),
                ('Carec_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_characteristic')),
                ('Prod_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_product')),
            ],
        ),
        migrations.CreateModel(
            name='T_Carac_detail',
            fields=[
                ('Carac_Detail_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Carac_Detail', models.CharField(max_length=100, unique=True)),
                ('Carac_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.t_characteristic')),
            ],
        ),
    ]
