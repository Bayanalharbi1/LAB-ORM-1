# Generated by Django 5.1.3 on 2024-11-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category_post_image_alter_post_published_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Life', 'Lifestyle'), ('Food', 'Food'), ('Travel', 'Travel')], default='Tech', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=2048),
        ),
    ]
