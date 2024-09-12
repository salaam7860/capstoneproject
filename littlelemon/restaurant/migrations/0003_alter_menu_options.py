from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_number_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu Items'},
        ),
    ]
