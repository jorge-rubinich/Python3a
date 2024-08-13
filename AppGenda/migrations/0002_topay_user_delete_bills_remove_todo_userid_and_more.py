# Generated by Django 4.2 on 2024-08-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15)),
                ('detail', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=15)),
                ('realName', models.CharField(max_length=40)),
                ('avatar', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='tododate',
            name='userId',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.CharField(default='BOCHA', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tododate',
            name='user',
            field=models.CharField(default='BOCHA', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tododate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
