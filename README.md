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