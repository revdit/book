# Generated by Django 4.1.1 on 2023-02-16 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='', upload_to='author/')),
            ],
        ),
        migrations.CreateModel(
            name='Productss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.CharField(max_length=100)),
                ('product_number', models.BigIntegerField()),
                ('language', models.CharField(default='', max_length=50)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='', upload_to='product/')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adbook.author')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.CharField(max_length=100)),
                ('product_number', models.BigIntegerField()),
                ('language', models.CharField(default='', max_length=50)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='', upload_to='product/')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adbook.author')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.CharField(max_length=100)),
                ('product_number', models.BigIntegerField()),
                ('language', models.CharField(default='', max_length=50)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='', upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adbook.product')),
            ],
        ),
    ]
