# Generated by Django 3.1.4 on 2020-12-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=42)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
