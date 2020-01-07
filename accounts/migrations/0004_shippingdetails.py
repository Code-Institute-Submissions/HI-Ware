# Generated by Django 3.0 on 2020-01-06 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address1', models.CharField(max_length=50)),
                ('street_address2', models.CharField(max_length=50)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]