# Generated by Django 3.2.5 on 2021-07-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped_date',
            field=models.DateField(null=True),
        ),
    ]
