from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_guests', models.SmallIntegerField()),
                ('booking_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking Records',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Manu',
                'verbose_name_plural': 'Manu Items',
            },
        ),
    ]
