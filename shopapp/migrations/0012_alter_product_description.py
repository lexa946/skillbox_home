# Generated by Django 4.2.3 on 2023-09-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0011_product_description_alter_order_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
