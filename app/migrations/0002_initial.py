# Example of a migration file
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
