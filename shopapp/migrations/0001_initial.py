# Generated by Django 4.2.3 on 2023-07-12 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPlastic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Цвет пластика',
                'verbose_name_plural': 'Цвета пластика',
            },
        ),
        migrations.CreateModel(
            name='TypePlastic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип пластика',
                'verbose_name_plural': 'Типы пластика',
            },
        ),
        migrations.CreateModel(
            name='Plastic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('has_now', models.BooleanField(default=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopapp.colorplastic')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopapp.typeplastic')),
            ],
            options={
                'verbose_name': 'Пластик',
                'verbose_name_plural': 'Пластики',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.TextField()),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('promocode', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='orders', to='shopapp.plastic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
