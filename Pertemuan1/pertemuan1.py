import time
mulai_waktu = time.time()
print("Menghitung (Jumlah Perhitungan)")
a = raw_input("Masukan angka a : ")
d = raw_input("Masukan angka d : ")
z = raw_input("masukan angka z : ")
r = raw_input("Masukan angka r : ")
m = raw_input("Masukan angka m : ")
if a == 'satu':
	a=1
if a == 'dua':
	a=2
if a == 'tiga':
	a=3
if a == 'empat':
	a=4
if a == 'lima':
	a=5
if a == 'enam':
	a=6
if a == 'tujuh':
	a=7
if a == 'delapan':
	a=8
if a == 'sembilan':
	a=9
if a == 'nol':
	a=0

if d == 'satu':
	d=1
if d == 'dua':
	d=2
if d == 'tiga':
	d=3
if d == 'empat':
	d=4
if d == 'lima':
	d=5
if d == 'enam':
	d=6
if d == 'tujuh':
	d=7
if d == 'delapan':
	d=8
if d == 'sembilan':
	d=9
if d == 'nol':
	d=0

if z == 'satu':
	z=1
if z == 'dua':
	z=2
if z == 'tiga':
	z=3
if z == 'empat':
	z=4
if z == 'lima':
	z=5
if z == 'enam':
	z=6
if z == 'tujuh':
	z=7
if z == 'delapan':
	z=8
if z == 'sembilan':
	z=9
if z == 'nol':
	z=0

if r == 'satu':
	r=1
if r == 'dua':
	r=2
if r == 'tiga':
	r=3
if r == 'empat':
	r=4
if r == 'lima':
	r=5
if r == 'enam':
	r=6
if r == 'tujuh':
	r=7
if r == 'delapan':
	r=8
if r == 'sembilan':
	r=9
if r == 'nol':
	r=0

if m == 'satu':
	m=1
if m == 'dua':
	m=2
if m == 'tiga':
	m=3
if m == 'empat':
	m=4
if m == 'lima':
	m=5
if m == 'enam':
	m=6
if m == 'tujuh':
	m=7
if m == 'delapan':
	m=8
if m == 'sembilan':
	m=9
if m == 'nol':
	m=0
Jumlah = (z*a)+(d/r)-m
print("Jumlah Perhitungan", Jumlah)
print("Waktu Menghitung : %s detik " % (time.time() - mulai_waktu))
