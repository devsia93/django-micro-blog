# Generated by Django 3.2.4 on 2021-06-14 20:18

from django.db import migrations, models
import django.db.models.deletion
import precise_bbcode.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
                ('_body_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('body', precise_bbcode.fields.BBCodeTextField(blank=True, db_index=True, no_rendered_field=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='post-title')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
            options={
                'ordering': ['-date_pub'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(db_index=True, max_length=15)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('_text_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('text', precise_bbcode.fields.BBCodeTextField(no_rendered_field=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['is_approved', 'date_pub'],
            },
        ),
    ]