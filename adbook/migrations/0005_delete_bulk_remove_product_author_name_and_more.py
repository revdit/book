# Generated by Django 4.1.1 on 2023-02-16 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adbook', '0004_author_bulk_product_author_name_product_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bulk',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author_name',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adbook.author'),
        ),
    ]
