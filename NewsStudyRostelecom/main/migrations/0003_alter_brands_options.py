# Generated by Django 4.2.7 on 2023-12-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_brands_desc_brand"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brands",
            options={
                "ordering": ["brand_name"],
                "verbose_name": "Бренд",
                "verbose_name_plural": "Бренды",
            },
        ),
    ]
