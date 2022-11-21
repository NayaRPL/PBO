
user_id  =  0
putaran  =  "n"
pengguna  = [
    {
        "id" : "2433" ,
        "no_rekening" : "1234567890" ,
        "username" : "Suryandini" ,
        "pin" : "1234" ,
        "saldo" : 3000000
    },
    {
        "id" : "2433" ,
        "no_rekening" : "0987654321 " ,
        "username" : "Alya" ,
        "pin" : "2213" ,
        "saldo" : 2000000
    }
]

status_login  =  Salah
pakai_atm  =  "y"


def  cek_login ( p ):
    untuk_pengguna_di_pengguna : 
        jika_pengguna [ 'pin' ] ==  p :
            pengguna_kembali
    mengembalikan  Salah


def  cek_user ( id ):
    untuk  i  dalam  jangkauan ( len ( users )):
        jika  pengguna [ i ][ 'id' ] ==  str ( id ):
            kembali  int ( saya )
    kembali  - 1


def  cek_rekening ( no ):
    untuk  i  dalam  jangkauan ( len ( users )):
        if  str ( users [ i ][ 'no_rekening' ]) ==  str ( no ):
            kembali  int ( saya )
    kembali  - 1


def  transfer_uang ( uang , no_rekening ):
    index1  =  cek_user ( user_id )
    index2  =  cek_rekening ( no_rekening )
    jika  indeks1  >=  0 :
        jika  pengguna [ index1 ][ 'saldo' ] >=  int ( uang ):
            pengguna [ index1 ][ 'saldo' ] =  pengguna [ index1 ][ 'saldo' ] -  int ( uang )
            pengguna [ index2 ][ 'saldo' ] =  pengguna [ index2 ][ 'saldo' ] +  int ( uang )
            print ( "Anda berhasil mentransfer uang Rp."  +  str ( uang ) +  " ke Rekening "  +  no_rekening )
            print ( "sisa saldo anda adalah Rp." , users [ index1 ][ 'saldo' ])
        lain :
            print ( "Saldo ops anda tidak cukup" )


def  ambil_uang ( uang ):
    index1  =  cek_user ( user_id )
    jika  indeks1  >=  0 :
        jika  pengguna [ index1 ][ 'saldo' ] >=  int ( uang ):
            pengguna [ index1 ][ 'saldo' ] =  pengguna [ index1 ][ 'saldo' ] -  int ( uang )
            print ( "Anda berhasil menarik uang Rp."  +  str ( uang ))
            print ( "sisa saldo anda adalah Rp." , users [ index1 ][ 'saldo' ])
        lain :
            print ( "Saldo ops anda tidak cukup" )


while  pakai_atm  ==  "y" :
    sementara  tidak  status_login :
        print ( "SELAMAT DATANG DI ATM BANK BRI" )
        print ( "Silahkan masukan pin anda" )
        pin  =  input ( "Masukan PIN : " )

        cl  =  cek_login ( pin )
        jika  kl :
            print ( "selamat datang "  +  cl [ 'username' ])
            user_id  =  cl [ 'id' ]
            status_login  =  Benar
            lingkaran  =  "y"
        lain :
            cetak ( "" )
            print ( "Ops PIN anda salah" )
            cetak ( "" )
            cetak ( "" )

    while  loop  ==  "y"  dan  status_login :
        u  =  pengguna [ cek_user ( user_id )]
        cetak ( "=========================================== " )
        print ( "SELAMAT DATANG DI ATM BRI" )
        print ( "1.Cek Saldo" )
        print ( "2.Transfer Uang" )
        print ( "3.Ambil Uang" )
        print ( "4.Logout" )
        print ( "5.Keluar ATM" )
        a  =  int ( input ( "Silahkan pilih menu : " ))
        cetak ( "=========================================== " )
        jika  a  ==  1 :
            cetak ( "" )
            print ( "Sisa Saldo anda adalah Rp." , u [ 'saldo' ])
            cetak ( "" )
            cetak ( "" )
            putaran  =  "n"
        
        elif  a  ==  2 :
            print ( "Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan" )
            no_rek  =  input ( "Masukan No Rekening Tujuan : " )
            cnk  =  cek_rekening ( no_rek )

            jika  cnk  >=  0 :
                print ( "Nomor rekening ditemukan,silahkan masukan nominal yang akan di transfer" )
                nominal  =  input ( "Nominal Yang Akan Di Transfer : " )
                transfer_uang ( nominal , no_rek )
                cetak ( "" )
                putaran  =  "n"
            lain :
                cetak ( "" )
                print ( "Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar" )
                cetak ( "" )
                putaran  =  "n"

        elif  a  ==  3 :
            nominal  =  input ( "Nominal Yang Akan Di Tarik : " )
            ambil_uang ( nominal )
            cetak ( "" )
            putaran  =  "n"
        elif  a  ==  4 :
            status_login  =  Salah

        elif  a  ==  5 :
            status_login  =  Salah
            putaran  =  "n"
            pakai_atm  =  "n"
        lain :
            print ( "pilihan tidak tersedia" )
        jika  status_login  ==  Benar :
            input ( "kembali ke menu (Enter) " )
            cetak ( "" )
            lingkaran  =  "y"