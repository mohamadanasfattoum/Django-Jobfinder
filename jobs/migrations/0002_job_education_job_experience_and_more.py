# Generated by Django 4.2.6 on 2023-10-11 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='education',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Experience'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.TextField(max_length=500, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=120, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='logo', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='salary',
            field=models.FloatField(verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='company',
            name='web',
            field=models.CharField(max_length=120, verbose_name='Web'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_jop', to='jobs.company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='job', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.ImageField(upload_to='logo', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.FloatField(verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('full', 'full'), ('part', 'part'), ('remote', 'remote'), ('freelance', 'freelance')], max_length=10, verbose_name='Type'),
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='Logo')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_job', to='jobs.job')),
            ],
        ),
    ]