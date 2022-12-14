# Generated by Django 3.2.5 on 2021-08-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Painting_Id', models.IntegerField()),
                ('Painting_Title', models.TextField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Available', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Painting',
        ),
    ]
