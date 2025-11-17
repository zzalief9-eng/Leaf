L='Anis Rania'
A='Putri Keisha'
F='Nur Jannatul Humaira'
R='Iman Qaisara'
D='Nanira'
S='Arissa Alma'
E='Athirah'

d='***Selamat datang***'
print(d.upper())

kata=int(input('Masukkan kata laluan: '))
if kata == int(119089):
   print('___ACCESS GRANTED___')
   nama=input('Masukkan nama (gunakan huruf besar bagi permulaan nama): ')
   if nama == 'Adrian':
       print('Buah hati Adrian ialah',A)
   elif nama == 'Faheem':
       print('Buah hati Faheem ialah',F)
   elif nama == 'Rizqin':
       print('Crush Rizqin ialah',R)
   elif nama== 'Davies':
       print('Crush Davies ialah',D)
   elif nama== 'Syafiq':
       print('Crush Syafiq ialah',S)
   elif nama=='Emir':
       print('Crush Emir ialah',E)
   elif nama == 'Amat Alief':
        kata_2= int(input('Masukkan kata laluan: '))
        if kata_2== int(809011):
                    print('Crush Amat ialah',L)
        else:
             print('___ACCESS DENIED___')
   else:
        print('Nama tiada dalam list')
else:
    print('___ACCESS DENIED___')
