def garis(): #fungsi
    print(70*'-')

def enter():
    print('\n')

print('\t' '\t' '\t' "CV. ARUNIKA LABS")
enter()
garis()
print("CV. Arunika Labs bergerak dibidang Jasa Servise Komputer sedang membutuhkan" )
print("1.          IT SUPPORT ")
print("2.          ADMIN SOSIAL MEDIA ")
garis()
print('\t' '\t' '\t' 'SILAKAN ISI DATA DIRI ANDA')
garis()
enter()

#input
nama=str(input('Nama                    : '))
umr=str(input('Umur                    : '))
alamat=str(input('Alamat                  : '))
pend=str(input('Pendidikan              : '))
jur=str(input('Jurusan                 : '))
peng=str(input('Pengalaman              : '))
email=str(input('Email                   : '))

garis()
print('\t' '\t' '\t' 'DATA DIRI ANDA')
garis()
print('Nama                         : ',nama)
print('Umur                         : ',umr)
print('Alamat                       : ',alamat)
print('Pendidikan                   : ',pend)
print('Jurusan                      : ',jur)
print('Pengalaman                   : ',peng)
print('Email                        : ',email)
garis()
print('\t' '\t' '\t' 'SOAL PSIKOTEST SELEKSI')
garis()


#Soal 1 jawaban C
print('1. Berapa Faktorial Dari 6!')
print('A.                   120')
print('B.                   520')
print('C.                   720')
s1=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 2 jawaban A
print('2. 11,22,44,88,176....704')
print('A.                   352')
print('B.                   300')
print('C.                   320')
s2=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 3 jawaban B
print('3. Singa termasuk dalam kategori hewan....')
print('A.                   Reptil')
print('B.                   Mamalia')
print('C.                   Inverbrata')
s3=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 4 jawaban a
print('4. Perusahaan - Karyawan = Sekolah -......')
print('A.                   Pelajar')
print('B.                   Ujian')
print('C.                   Kelas')
s4=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 5 jawaban b
print('5. Urutkan P-A-S-I-R menjadi sebuah nama ibu kota......')
print('A.                   Jerman')
print('B.                   France')
print('C.                   Spanyol')
s5=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 6 jawaban B
print('6. Sekuler >< ...')
print('A.       Hedonisme')
print('B.       Keagamaan')
print('C.       Duniawi')
s6=str(input('Masukkan Jawaban Mu = '))
enter()

#oal 7 jawaban C
print("7 ... - WISUDA = PERTUNANGAN - ... ")
print('A.   toga-cincin')
print('B.   gelar-pelaminan')
print('C.   kuliah-pernikahan')
s7=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 8 Jawaban A
print("8. SAKIT - ... = ... - MAKAN")
print('A.   dokter-sakit')
print('B.   istirahat-lapar')
print('C.   pasien-gizi')
s8=str(input('Masukkan Jawaban Mu = '))
enter()

#soal 9 jawaban A
print('9. Mobil - Bensin = Pelari - ...')
print('A.   Sepatu')
print('B.   Kaos')
print('C.   Lintasan')
s9=str(input('Masukkan jawaban Mu = '))
enter()

#soal 10 Jawaban C
print('10. Dingin - Selimut = Hujan - ...')
print('A.   Basah')
print('B.   Air')
print('C.   Payung')
s10=str(input('Masukkan Jawaban Mu = '))
enter()

#proses soal1
if s1=="C" or s1=="c":
    h1=5*2
else:
    h1=5*0

#proses soal2
if s2=="A" or s2=="a":
    h2=5*2
else:
    h2=5*0

#proses soal3
if s3=="B" or s3=="b":
    h3=5*2
else:
    h3=5*0

#proses soal 4
if s4=="A" or s4=="a":
    h4=5*2
else:
    h4=5*0

#proses soal 5
if s5=="b" or s5=="B":
    h5=5*2
else:
    h5=5*0

#proses soal 6
if s6=="C" or s6=='c':
    h6=5*2
else:
    h6=5*0

#proses soal 7
if s7=='C' or s7=='c':
    h7=5*2
else:
    h7=5*0

#proses soal 8 
if s8=='A' or s8=='a':
    h8=5*2
else:
    h8=5*0 

#proses soal 9
if s9=='A' or s9=='a':
    h9=5*2
else:
    h9=5*0

#proses soal 10
if s10=='C' or s10=='c':
    h10=5*2
else:
    h10=5*0

jumlah=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10

garis()
print('\t' '\t' '\t' 'NILAI PSIKOTES MU',jumlah)
garis()

tupleKet=['BAIK > 80', 'CUKUP <= 80', 'Kurang < 60']
for ket in tupleKet:
    print(ket)
garis()

lolos=jumlah
if lolos>=80:
    print('Selamat Anda Lolos Seleksi, Pihak Kami Akan Email Kalian Untuk Jadwal Interview ')
else:
    print('Terima Kasih Sudah Melamar, Kami akan menginfokan lebih lanjut')
garis()
