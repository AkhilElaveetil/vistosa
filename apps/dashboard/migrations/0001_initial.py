# Generated by Django 3.2.9 on 2022-03-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]