print('W E L K A M TO K A L K U L A T O R')

angka1 = int(input('Masukkan Angka Pertama : '))
print( )
angka2 = int(input('Masukkan Angka Kedua : '))
print('Operator : \n1.Penjumlahan \n2.Pengurangan \n3.Perkalian \n4.Pembagian')
pilih = int(input('Mau Operator Yang Mana Nich : '))
print( )
if pilih == 1:
	tambah = angka1+angka2
	print('Hasilnya Nich :v = ',tambah)
elif pilih == 2:
	kurang = angka1-angka2
	print('Hasilnya Nich :v = ',kurang)
elif pilih == 3:
	kali = angka1*angka2
	print('Hasilnya Nich :v = ',kali)
elif pilih == 4:
	bagi = angka1/angka2
	print('Hasilnya Nich :v = ',bagi)
else:
	print('Operator yang anda masukkan tidak ada dimuka bumi ini :) ')

print( )
print('S E L E S A I A S W')