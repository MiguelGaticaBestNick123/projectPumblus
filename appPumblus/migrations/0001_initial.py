# Generated by Django 4.2.1 on 2023-05-22 03:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pumblus',
            fields=[
                ('idProducto', models.IntegerField(error_messages='Debe ingresar un producto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('f_creacion', models.DateField()),
                ('f_caducidad', models.DateField()),
                ('c_chumbles', models.CharField(choices=[('KC°', 'KC°'), ('%Z', '%Z'), ('O', 'O'), ('O)', 'O)')], max_length=10)),
                ('imagen', models.ImageField(upload_to='notenemosfotoytengosueño')),
            ],
        ),
        migrations.CreateModel(
            name='PumblusX',
            fields=[
                ('idProducto', models.IntegerField(error_messages='Debe ingresar un producto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('largo_dingle_dop', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vibracion_floops', models.IntegerField()),
                ('grodus_inalambrico', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='notenemosfotoytengosueño')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=12)),
                ('groups', models.ManyToManyField(related_name='custom_user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
                ('imagenPerfil', models.ImageField(upload_to='notenemosfotoytengosueño')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appPumblus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(default='Pendiente', max_length=100)),
                ('direccion_envio', models.CharField(max_length=150)),
                ('carrito', models.ManyToManyField(to='appPumblus.carrito')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPumblus.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='pumblus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPumblus.pumblus'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPumblus.usuario'),
        ),
    ]