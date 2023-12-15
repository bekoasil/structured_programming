#file_write.py

fp = open("week10/results", "w")

#r read 
#w write her zaman dosyayi sifirdan olusturur
#a append eger ekleme yapilmak isteniyorsa bu modda acilir
#b byte 
#t text 

fp.write("cihan\n")
fp.write("hakan\n")
fp.write("merve\n")

fp.close()

fp = open("week10/results", "a")

fp.write("bekirasil")
fp.close()

data = ["cihan", "hakan", "aleyna"]
fp = open("week10/resultlines", "w")

fp.writelines(data)
fp.close()