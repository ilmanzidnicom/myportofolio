Nama : Ilman Zidni

NPM : 2506621951

Kelas : PBP B

## Tugas 1

1. Saya menggunakan `<section>` pada tugas ini. `<section>`, walaupun secara fungsi tidak melakukan apa-apa, saat saya koding, saya merasa dengan adanya `<section>`, saya lebih mudah melihat struktur halaman.
2. Tantangan yang saya hadapi saat mengatur CSS agar responsif adalah elemen `<pre>` tidak melakukan *word wrap* secara default. Setelah melakukan *google search*, saya menemukan ini https://stackoverflow.com/questions/248011/how-do-i-wrap-text-in-a-pre-tag yang membantu saya agar elemen `<pre>` dapat melakukan *word wrap*.
3. Sebuah halaman HTML bisa jadi sangat panjang/besar jika murni HTML static. Jika section atau elemen-elemen pada sebuah halaman bisa dipecah atau diinterpretasikan menggunakan format lain seperti *json*, tipe data lain, atau bahkan sebuah *user-friendly user interface* untuk mengatur konten dalam halaman, akan sangat membantu untuk skalabilitas sebuah projek.

#### AI Disclosure Pada Tugas 1
*Saya tidak menggunakan AI pada tugas 1. Proses pemecahan masalah saya jelaskan pada jawaban pertanyaan reflektif ke-2.*

## Tugas 2

1. Alur yang terjadi ketika pengguna membuka situs portofolio saya adalah:
    1. *Request* dikirim oleh browser pengguna.
    2. Django menangkap *request* tersebut melalui `urls.py` projek terlebih dahulu.
    3. Lalu projek Django melihat *root* path menunjuk ke aplikasi `main`.
    4. Pada aplikasi main, terdapat `urls.py` yang memberikan spesifikasi path aplikasi tersebut secara lokal.
    5. `urls.py` aplikasi menunjuk ke *function* yang berada pada `views.py` aplikasi.
    6. Terakhir, `views.py` aplikasi membalas *request* dari browser pengguna dengan halaman html *template* yang sudah dipopulasikan dengan *context* yang didapatkan dari *dictionary* di dalam `views.py` atau dari class model pada `models.py`. 
2. Jika data ditulis langsung pada *template*, maka setiap perubahan konten pada halaman memerlukan pengguna untuk mengganti *template* html. Pada projek skala besar, mengganti *template* html memerlukan waktu dan proses yang panjang. Projek akan kurang cocok untuk digunakan oleh banyak pengguna yang ingin menambahkan atau mengubah konten pada website secara bersamaan. Maka dengan adanya database model dan *template* yang mengambil data dari database, pengguna dapat mengelola konten melalui *user interface* ramah yang dihubungkan ke database.
3. `makemigrations` membuat file `migration` (dapat dilihat pada \<nama aplikasi\>/migrations) yang memberikan spesifikasi pergantian schema database. Lalu `migrate` mengaplikasikan perubahan yang dispesifikasikan file `migration` kepada database.

#### AI Disclosure Pada Tugas 2
*Saya tidak menggunakan AI pada tugas 2.*

Beberapa masalah yang saya pecahkan adalah:
1. Di antara *template* `index.html` dan `experience.html`, saya sering kali lupa untuk mengganti elemen-elemen yang berada pada kedua html ketika saya mengganti elemen pada salah satu saja. Jadi saya menggunakan `{% extends %}` dan `{% block %}` untuk menghindari repetisi. Saya mendapatkan referensi tersebut dari [Learn Django in 20 Minutes!!](https://www.youtube.com/watch?v=nGIg40xs9e4).
2. Untuk konsep baru seperti aplikasi, *database*, *model class*, *Jinja*, dan *unit test*, saya mengikuti alur dan *syntax* yang sudah dicontohkan pada tutorial 2.

## Tugas 3
1. Kita menggunakan `ModelForm` karena `ModelForm` memudahkan kita untuk membuat sebuah *form* dengan struktur data yang lebih simpel dan konsisten. Struktur data `ModelForm` dapat dikonversi ke halaman HTML dengan hanya menyatakan `{% for field in form %}` pada template. `{% csrf_token %}` dapat melindungi form dari *exploit* *Cross-Site Request Forgery*. Di mana HTML dari website lain dapat menaruh url POST request website kita pada form yang mereka buat. Dan form tersebut bisa terdapat data yang sudah dipopulasikan oleh data mereka, sehingga mereka bisa mengirim POST request atas nama kita tanpa kita menyetujui. `{% csrf_token %}` meletakkan *invisible field* pada form HTML yang sudah dipopulasikan dengan token unik. Jika pengguna *submit* form tersebut, token tersebut juga ikut terkirim. Jika token tersebut tidak sesuai atau tidak ada, maka Django akan menolak POST request yang dikirim oleh *client*.
2. JSON lebih disukai dibandingkan XML karena JSON memiliki format data yang lebih ringkas dan pendek dibanding XML. XML memerlukan struktur *tag*, sehingga pada akhirnya menghasilkan data yang lebih besar.
3. Kita perlu melakukan *serialization* karena struktur data *class* python belum dalam bentuk JSON, sehingga kita harus mengubahnya dulu ke format JSON melalui *serialization*.
Alur yang terjadi pada fungsi view yang mengembalikan data portofolio dalam bentuk JSON adalah:
    1. Mengambil semua data pada class model dengan cara `<Model>.object.all()`
    2. *Serialize* data ke json menggunakan `serializers.serialize()`
    3. Lalu mengembalikan data yang sudah di-*serialize* menggunakan `HttpResponse()` dengan `content_type="application/json"`

#### AI Disclosure Pada Tugas 3
*Saya tidak menggunakan AI pada tugas 3.*

Beberapa masalah yang saya pecahkan adalah:
1. Untuk form update data, saya menggunakan [Python Django Tutorial #9: Django Update Form, Django Update View](https://www.youtube.com/watch?v=Xin4hjyMe6E) sebagai referensi.
2. Untuk autentikasi, saya mendapatkan info dari teman saya [Ahmad Rafa Robyan [NPM: 2506620721]](https://github.com/Reigits) bahwa *decorator* `@login_required()` dan `{% if user.is_authenticated %}` dapat dipakai sebagai autentikasi sederhana dari bawaan Django.

## Tugas 4

#### AI Disclosure Pada Tugas 4:
*Saya tidak menggunakan AI pada tugas 4.*

Untuk autentikasi saya sudah menerapkannya pada tugas 3.

Untuk konsep baru seperti permissions, saya mendapatkan referensi dari [Check permission inside a template in Django](https://stackoverflow.com/questions/9469590/check-permission-inside-a-template-in-django) dan `Petunjuk Implementasi Peran Editor` pada halaman tugas 4.
