# Generated by Django 2.2 on 2019-06-03 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0008_auto_20190425_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corpus',
            options={'verbose_name': '5. Corpus Identity', 'verbose_name_plural': '5. Corpus Identities'},
        ),
        migrations.AlterModelOptions(
            name='corpusdivide',
            options={'verbose_name': 'Corpus Tokenized (Automatic)', 'verbose_name_plural': 'Corpus Tokenized (Automatic)'},
        ),
        migrations.AlterModelOptions(
            name='corpuslangreq',
            options={'verbose_name': '6. Corpus Language Required', 'verbose_name_plural': '6. Corpus Languages Required'},
        ),
        migrations.AlterModelOptions(
            name='keystrokes',
            options={'verbose_name': 'Keystroke Collection (Automatic)', 'verbose_name_plural': 'Keystroke Collection (Automatic)'},
        ),
        migrations.AlterModelOptions(
            name='langtolang',
            options={'verbose_name': '2 . Language to Language Link', 'verbose_name_plural': '2. Language to Language Links'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': '1. Language', 'verbose_name_plural': '1. Languages'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'Time Data Collection (Automatic)', 'verbose_name_plural': 'Time Data Collection (Automatic)'},
        ),
        migrations.AlterModelOptions(
            name='translatedsentence',
            options={'verbose_name': 'Translated Pairs by Users (Automatic)', 'verbose_name_plural': 'Translated Pair by User (Automatic)'},
        ),
        migrations.AlterModelOptions(
            name='translatedset',
            options={'verbose_name': 'Translated Set (linking pairs together) by Users (Automatic)', 'verbose_name_plural': 'Translated Set (linking pairs together) by User (Automatic)'},
        ),
        migrations.AlterModelOptions(
            name='translator',
            options={'verbose_name': '3. Translator Identity', 'verbose_name_plural': '3. Translator Identities'},
        ),
        migrations.AlterModelOptions(
            name='translatorlangs',
            options={'verbose_name': '4. Translator Language Possible', 'verbose_name_plural': '4. Translator Languages Possible'},
        ),
        migrations.AlterField(
            model_name='corpus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]