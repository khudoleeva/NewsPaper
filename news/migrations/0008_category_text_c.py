# Generated by Django 4.1.4 on 2023-01-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_authorcategory_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text_c',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
