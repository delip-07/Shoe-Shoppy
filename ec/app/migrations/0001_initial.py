# Generated by Django 5.0.6 on 2024-08-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('CS', 'CASUAL'), ('FR', 'FORMAL'), ('AL', 'ATHLETIC'), ('BO', 'BOOTS'), ('SP', 'SPECIALTY')], max_length=2)),
                ('product_images', models.ImageField(upload_to='product')),
            ],
        ),
    ]
