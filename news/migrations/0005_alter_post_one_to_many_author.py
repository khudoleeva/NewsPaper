# Generated by Django 4.1.4 on 2022-12-20 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_comment__rating_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='one_to_many_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='news.author'),
        ),
    ]
