# SIBLOG
Kependekan dari Simple Blog. Berbasis Django. SIBLOG membantu untuk membangun sebuah website seperti personal blog yang meliputi:
* Pengelolaan halaman statis/dinamis
* Pengelolaan kategori
* Pengelolaan navigasi menu
* Pengelolaan pengaturan umum website

## Pre-Instalasi
* Python 2.7.x atau yang terbaru
* Django >= 1.8.x

## Instalasi
* Download siblog-master.zip
* Buat folder **django/** di **~/** menjadi **~/django/**
* Ekstrak siblog-master.zip ke folder **django/**
* Buka terminal dan pindah direktori ke **~/django/sblog-master/**. `$ cd ~/django/siblog-master`
* `./manage.py makemigrations && ./manage.py migrate`
* Jalankan **siblog**-nya dengan `./manage.py runserver`
* Buka web browser. `http://localhost:8000`
