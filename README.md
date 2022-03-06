# LATIHAN4DPBO2022
Repository ini bertujuan untuk memenuhi tugas latihan 4 pada mata kuliah Desain Pemograman Berorientasi Objek. 

------------------

Nama : Sabian Annaya Havid
Program Studi/Kelas : Ilmu Komputer/C2
NIM : 2005021

*Saya Sabian Annaya Havid mengerjakan Latihan dalam mata kuliah Desain Pemograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.*

------------------
## Penjelasan/Konsep program
![Concept diagram](https://user-images.githubusercontent.com/99664611/156929719-437911c6-62fc-4af9-bacb-80018c1f0f06.png) 

Program ini memiliki 2 family yaitu vehicle dan person.
- **Vehicle family's class:** Vehicle (parent), Ship (Child 1), Airplane (Child 2) (Hierarchical Inheritance)
- **Person family's class:** Person (parent), Job (Child 1), Driver (Child of Job/child of child of Person) (Multi-level inheritance)

*Vehicle* menggunakan konsep *hierarchical inheritance* dengan alasan bahwa **Ship** dan **Airplane** merupakan jenis dari **Kendaraan**, lalu semua atribut yang dimiliki **Kendaraan** dapat digunakan oleh kelas **Ship** maupun **Airplane**.

Sedangkan kasus pada *person family* cukup unik, pada dasarnya job tidak terkait apapun dengan person karena merupakan dua entitas yang berbeda. **Namun**, pada kelas **job** memiliki atribut *position* yang dapat dihubungkan dengan identitas **person**. Oleh karena itu, kelas **Job** dipilih menjadi kelas anak dari kelas **Person**.
Sedangkan kelas **Driver** merupakan salah satu jenis pekerjaan sehingga diposisikan menjadi kelas anak dari kelas **Job**. Family **Person** menggunakan jenis *multi-level inheritance*.

------------------
## Hasil menjalankan program
![tesPY](https://user-images.githubusercontent.com/99664611/156929280-971e25f7-20d5-410b-be6d-eedf56b4daf4.png)

