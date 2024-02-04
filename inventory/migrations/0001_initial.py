# Generated by Django 4.2 on 2023-04-15 09:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000)])),
                ('name', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000)])),
                ('price', models.FloatField(validators=[django.core.validators.MaxValueValidator(1000)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_add', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000)])),
                ('stockleft', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000)])),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
