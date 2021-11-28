
def data () :
    x = 0
    while x < 10 :
        

        nama = input ("masukan nama :")
        nim = int (input("masukan nim :"))
        nilai_tugas = float (input("masukan nilai :"))
        nilai_uts = float (input("masukan nilai :"))
        nilai_uas = float (input("masukan nilai :"))
        tambah_data =input ("tambah data (y/t)?")

        

        
        if tambah_data =="t" : 
            print ("nama kamu adalah :", nama)
            print ("Nim kamu :", nim)
            print ("Nilai Tugas Kamu :" ,nilai_tugas)
            print ("Nilai UTS kamu ", nilai_uts)
            print ("Nilai Uas Kamu ", nilai_uas)
            nilai1 = nilai_tugas*0.3
            nilai2 = nilai_uts*0.35
            nilai3 = nilai_uas*0.35
            
            nilai_akhir = nilai1 + nilai2 + nilai3
            print ("nilai Akhir Kamu = ", nilai_akhir)

            break

       




data () 

