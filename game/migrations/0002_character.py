# Generated by Django 4.1 on 2022-10-30 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='character', to=settings.AUTH_USER_MODEL)),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_list', to='game.weapon')),
            ],
        ),
    ]
