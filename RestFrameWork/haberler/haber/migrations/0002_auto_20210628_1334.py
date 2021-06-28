# Generated by Django 3.2 on 2021-06-28 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazeteci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=120)),
                ('soyisim', models.CharField(max_length=120)),
                ('biyografi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='guncellenme_tarihi',
            new_name='güncelleneme_tarihi',
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='olusturulma_tarihi',
            new_name='yaratilma_tarihi',
        ),
        migrations.RenameField(
            model_name='makale',
            old_name='yayinlanma_tarihi',
            new_name='yayımlanma_tarihi',
        ),
        migrations.AlterField(
            model_name='makale',
            name='baslik',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='makale',
            name='sehir',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='makale',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to='haber.gazeteci'),
        ),
    ]