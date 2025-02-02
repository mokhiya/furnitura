# Generated by Django 5.1.2 on 2024-10-21 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Brand Name')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Color Name')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Size Name')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Tag Name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image1', models.ImageField(upload_to='images/', verbose_name='Image 1')),
                ('image2', models.ImageField(upload_to='images/', verbose_name='Image 2')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('long_description', models.TextField(verbose_name='Long Description')),
                ('in_stock', models.BooleanField(default=True, verbose_name='In stock')),
                ('sku', models.CharField(max_length=100, unique=True, verbose_name='SKU')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('discount', models.FloatField(default=0, verbose_name='Discount')),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Real Price')),
                ('brands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brandmodel')),
                ('category', models.ManyToManyField(related_name='products', to='products.categorymodel')),
                ('color', models.ManyToManyField(related_name='products', to='products.colormodel')),
                ('size', models.ManyToManyField(related_name='products', to='products.sizemodel')),
                ('tag', models.ManyToManyField(related_name='products', to='products.tagmodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
