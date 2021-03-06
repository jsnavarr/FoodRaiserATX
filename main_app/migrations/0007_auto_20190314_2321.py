# Generated by Django 2.1.5 on 2019-03-14 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('FoodGiver', 'FoodGiver'), ('FoodTaker', 'FoodTaker')], default='FoodGiver', max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='phone',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='meals',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='meal',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Company'),
            preserve_default=False,
        ),
    ]
