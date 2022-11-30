# Generated by Django 3.2.16 on 2022-11-06 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0021_alter_urun_favori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urun',
            name='favori',
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.urun')),
            ],
        ),
    ]
