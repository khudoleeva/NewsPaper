# Generated by Django 4.1.4 on 2023-01-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_category_text_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='text_c',
        ),
    ]