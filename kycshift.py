# -*- coding: utf-8 -*-

import sys
import binascii

print('Project Level UPPER')
print('KYC Shift Ver 1.10')

def kycshift(r, new_song_number):
    f=open(r,"rb")
    f.seek(0)
    fanu = f.read(4)

    f.seek(8)
    song_number = f.read(3)
    song_number_hex=binascii.hexlify(song_number)
    song_number_str=song_number_hex.decode('ascii')
    song_number_1=song_number_str[0:2]
    song_number_2=song_number_str[2:4]
    song_number_3=song_number_str[4:6]
    song_number_all=song_number_3+song_number_2+song_number_1
    song_number_int=int(song_number_all, base=16)
    print(song_number_int)

    print(hex(song_number_int))
    #new_song_number=sys.argv[2]
    #print(new_song_number)
    #print(format(int(new_song_number), 'x'))
    new_song_number_hex=format(int(new_song_number), 'x').encode('ascii').decode('ascii')
    print(new_song_number_hex)
    new_song_hex_len=len(format(int(new_song_number), 'x').encode('ascii').decode('ascii'))

    if new_song_hex_len == 5 :
        new_song_number_hex = '0'+new_song_number_hex
    elif new_song_hex_len == 4 :
        new_song_number_hex = '00'+new_song_number_hex
    elif new_song_hex_len == 3 :
        new_song_number_hex = '000'+new_song_number_hex
    elif new_song_hex_len == 2 :
        new_song_number_hex = '0000'+new_song_number_hex
    elif new_song_hex_len == 1 :
        new_song_number_hex = '00000'+new_song_number_hex
    else :
        print('원하는 곡번호가 잘못된듯 합니다?')
        sys.exit(1)
        
    print(new_song_number_hex) 
    new_song_number_hex_r = new_song_number_hex[4:6]+new_song_number_hex[2:4]+new_song_number_hex[0:2]

    new_song_number_bin = binascii.unhexlify(new_song_number_hex_r)
    print(new_song_number_bin)

    z=open(new_song_number+'.KYC','bw')
    f.seek(0)
    kyc_data_1 = f.read(8)
    kyc_data_2 = new_song_number_bin
    f.seek(11)
    kyc_data_3 = f.read()
    z.write(kyc_data_1+kyc_data_2+kyc_data_3)
    z.close()
    
filename=sys.argv[1]
newnumber=sys.argv[2]

kycshift(filename, newnumber)