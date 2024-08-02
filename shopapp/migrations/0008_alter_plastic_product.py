# Generated by Django 4.2.3 on 2023-07-15 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_alter_plastic_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plastic',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type', to='shopapp.product'),
        ),
    ]