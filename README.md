# UAS_PAA2_Bubble_Insertion_TSP_Djikstra
# Niluh Nia Devi_F55121058
# Kelas B_Teknik Informatika
                                                  **ANALISIS ALGORITMA UNTUK EVALUASI PROGRAM**
  A. Bubble Sort Dan Insertion Sort
     Worst Case:
       1. Bubble Sort: Dalam kasus ini, worst case terjadi ketika array diurutkan secara terbalik (dalam urutan menurun). Hal ini akan    
           menghasilkan kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam array. Dalam implementasi Bubble Sort pada kode 
           tersebut, semua elemen akan saling dibandingkan dan dilakukan penukaran pada setiap iterasi, menghasilkan jumlah operasi yang 
           banyak.
       2.  Insertion Sort: Dalam kasus ini, worst case terjadi ketika array diurutkan secara terbalik (dalam urutan menurun). Hal ini 
           akan menghasilkan kompleksitas waktu O(n^2). Dalam implementasi Insertion Sort pada kode tersebut, setiap elemen harus 
           dipindahkan ke posisi yang tepat dalam array yang sudah diurutkan. Pada setiap iterasi, elemen yang sedang diproses akan 
           dibandingkan dengan elemen-elemen sebelumnya dan pergeseran akan dilakukan jika diperlukan.
      Best Case
        1. Bubble Sort: Dalam kasus ini, best case terjadi ketika array sudah terurut secara menaik sejak awal. Meskipun demikian, dalam
           implementasi Bubble Sort pada kode tersebut, setiap elemen masih akan dibandingkan dengan elemen lainnya pada setiap iterasi. 
           Oleh karena itu, kompleksitas waktu tetap O(n^2).
        2. Insertion Sort: Dalam kasus ini, best case terjadi ketika array sudah terurut secara menaik sejak awal. Pada kasus terbaik 
           ini, kompleksitas waktu Insertion Sort adalah O(n), di mana n adalah jumlah elemen dalam array. Pada setiap iterasi, hanya 
           perbandingan yang dilakukan untuk menemukan posisi yang tepat bagi setiap elemen. Tidak ada pergeseran yang diperlukan.
      Average Case:
        1. Bubble Sort: Dalam kasus ini, rata-rata kompleksitas waktu Bubble Sort tetap O(n^2). Meskipun ada beberapa elemen yang sudah 
           dalam posisi yang benar dan tidak memerlukan penukaran, tetapi setiap elemen masih harus dibandingkan dengan elemen lainnya 
           pada setiap iterasi.
        2. Insertion Sort: Dalam kasus ini, rata-rata kompleksitas waktu Insertion Sort tetap O(n^2). Meskipun ada beberapa elemen yang 
           sudah dalam posisi yang benar dan tidak memerlukan pergeseran, tetapi setiap elemen masih harus dibandingkan dan mungkin 
           dilakukan pergeseran pada kasus rata-rata.
           
  B. TSP dan Djikstra
     Wort Case
       1. TSP (Traveling Salesman Problem): Pada kasus terburuk, kompleksitas waktu TSP adalah O(n!), di mana n adalah jumlah node dalam
          graf. Dalam kasus ini, algoritma akan menghasilkan semua kemungkinan permutasi node, sehingga kompleksitas waktu secara 
          eksponensial meningkat seiring bertambahnya jumlah node. Ini menjadikan TSP tidak efisien untuk kasus dengan jumlah node yang
          besar.
       2. Dijkstra: Pada kasus terburuk, kompleksitas waktu Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah 
          jumlah tepi dalam graf. Dalam kasus ini, semua node harus dikunjungi untuk mencari jalur terpendek, dan algoritma Dijkstra akan 
          menjelajahi semua tepi yang terhubung dengan setiap node. Jika graf sangat padat dan terhubung dengan banyak tepi, kompleksitas 
          waktu Dijkstra dapat meningkat secara signifikan.
          
    Best Case
       1. TSP (Traveling Salesman Problem): Tidak ada keadaan terbaik yang signifikan dalam TSP karena algoritma harus memeriksa semua 
          kemungkinan permutasi node. 
       2. Dijkstra: Pada kasus terbaik, kompleksitas waktu Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah 
          jumlah tepi dalam graf. Dalam kasus terbaik, jika node awal dan node akhir berada sangat dekat atau hanya terhubung dengan satu 
          tepi, algoritma Dijkstra dapat mencapai solusi dengan kompleksitas waktu yang lebih baik.
          
    Average Case:
       1. TSP (Traveling Salesman Problem): Tidak ada solusi efisien yang diketahui untuk TSP dalam kasus rata-rata. Kompleksitas waktu 
          algoritma TSP umumnya cenderung eksponensial seiring bertambahnya jumlah node, sehingga sulit untuk memberikan perkiraan yang 
          pasti dalam kasus rata-rata.
       2. Dijkstra: Pada kasus rata-rata, kompleksitas waktu Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah 
          jumlah tepi dalam graf. Dalam kasus rata-rata, Dijkstra akan menjelajahi sebagian besar atau semua tepi dalam graf tergantung 
          pada struktur dan keterhubungan node. Kompleksitas waktu yang diperlukan oleh Dijkstra dapat bervariasi tergantung pada faktor-
          faktor tersebut.
