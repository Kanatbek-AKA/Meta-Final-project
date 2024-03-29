# Generated by Django 4.2.10 on 2024-03-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "restaurant",
            "0003_remove_booking_comment_remove_booking_guest_number_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=50)),
                ("no_of_guests", models.IntegerField()),
                ("bookingDate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]
