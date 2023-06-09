# Generated by Django 4.2.1 on 2023-05-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='product name')),
                ('cat', models.IntegerField(choices=[(1, 'Mobile'), (2, 'Cloths'), (3, 'Shoes')], verbose_name='category')),
                ('price', models.FloatField(verbose_name='product price')),
                ('status', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
    ]
