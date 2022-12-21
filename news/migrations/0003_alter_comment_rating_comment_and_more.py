# Generated by Django 4.1.4 on 2022-12-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_rating_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating_comment',
            field=models.IntegerField(db_column='rating_comment', default=0),
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='rating_comment',
            new_name='_rating_comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(db_column='rating_post', default=0),
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rating_post',
            new_name='_rating_post',
        ),
    ]