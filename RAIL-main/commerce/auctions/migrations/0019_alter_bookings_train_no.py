# Generated by Django 4.2.1 on 2023-10-10 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_rename_train_no_bookings_train_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='train_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.train'),
        ),
    ]
