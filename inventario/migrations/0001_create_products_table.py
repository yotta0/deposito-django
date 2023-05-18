# Generated by Django 4.2.1 on 2023-05-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]