# Generated by Django 5.0.6 on 2024-10-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOUTIQUE', '0007_remove_boutique_order_date_boutique_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boutique',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
