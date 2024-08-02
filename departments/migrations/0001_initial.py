# Generated by Django 5.0.7 on 2024-08-02 14:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('responsabilitys', models.CharField(max_length=1100)),
                ('user_id', models.ManyToManyField(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
