# Generated by Django 3.2.16 on 2022-10-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.kategori'),
        ),
    ]
