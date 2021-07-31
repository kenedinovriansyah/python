# Generated by Django 3.2.5 on 2021-07-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0012_rename_image_product_galery"),
    ]

    operations = [
        migrations.RenameField(
            model_name="currency",
            old_name="sell",
            new_name="sales_price",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="description",
            new_name="desc",
        ),
        migrations.RenameField(
            model_name="productimage",
            old_name="image",
            new_name="picture",
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
