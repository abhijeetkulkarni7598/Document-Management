# Generated by Django 4.2.8 on 2024-01-02 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('gst_no', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=15)),
                ('contact_person_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipping_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=255)),
                ('po_date', models.DateField()),
                ('project_status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.client')),
                ('file', models.ManyToManyField(related_name='jobs', to='files.file')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='files.job'),
        ),
    ]