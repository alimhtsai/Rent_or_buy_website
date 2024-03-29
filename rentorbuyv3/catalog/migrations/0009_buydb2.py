# Generated by Django 4.1.6 on 2023-02-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_alter_whichmrtname_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buydb2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Title",
                    models.CharField(help_text="Enter buydb title", max_length=200),
                ),
                (
                    "MrtCode",
                    models.CharField(
                        help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站",
                        max_length=200,
                    ),
                ),
                (
                    "MrtName",
                    models.CharField(
                        help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站",
                        max_length=200,
                    ),
                ),
                (
                    "Address",
                    models.CharField(help_text="Enter Address", max_length=200),
                ),
                (
                    "FloorType",
                    models.CharField(help_text="Enter 整層住家 or 套房", max_length=200),
                ),
                (
                    "RoomNum",
                    models.IntegerField(help_text="Enter Room Number, ex: 4 = 4房"),
                ),
                (
                    "Price",
                    models.IntegerField(
                        help_text="Enter buying prices per month, 單位 = 新台幣"
                    ),
                ),
                (
                    "Size",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Enter housing size, 單位 = 坪",
                        max_digits=20,
                    ),
                ),
                ("Floor", models.CharField(help_text="Enter floor", max_length=200)),
                (
                    "Parking",
                    models.CharField(help_text="Enter parking detail", max_length=200),
                ),
                ("Link", models.CharField(help_text="Enter 591 urls", max_length=500)),
            ],
        ),
    ]
