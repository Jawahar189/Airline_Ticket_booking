# Generated by Django 4.2.1 on 2023-10-10 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_bookings_train_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='Train_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numb', to='auctions.train'),
        ),
    ]
