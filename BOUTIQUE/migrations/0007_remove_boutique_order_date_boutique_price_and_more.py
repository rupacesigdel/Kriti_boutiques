# Generated by Django 5.0.6 on 2024-10-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOUTIQUE', '0006_boutique_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boutique',
            name='order_date',
        ),
        migrations.AddField(
            model_name='boutique',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boutique',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]