import os


from cryptography.fernet import Fernet #cryptography.fernet import Fernet'ten gelen kod, bir simetrik anahtar kullanarak mesajları şifrelemek ve şifresini çözmek için kullanılabilen cryptography.fernet modülünden Fernet sınıfını içe aktarır.


files = []

for file in os.listdir(): #şu andaki dizindeki her dosya/dizin için bir döngü başlatır.
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py": # koşulları kontrol eder, geçerli dosya "encrypt.py", "thekey.key" veya "decrypt.py"'den herhangi biri ise, döngünün diğer kısmına devam eder ve geri kalan kod bloğunu atlar.
        continue
    if os.path.isfile(file): #geçerli dosya gerçek bir dosya mı değil mi, dizin değil mi. Eğer geçerli dosya bir dosya ise, dosya adını files adlı listede ekler.
        files.append(file)



with open("thekey.key", "rb") as key: #"thekey.key" dosyasını okuma modunda binary olarak açar ve dosya nesnesini "key" değişkenine atar. Daha sonra dosya nesnesinin read() metodunu kullanarak dosyanın içeriğini okur ve değeri "secretkey" değişkenine atar.
    secretkey = key.read()

    secret_sifre = "testsifre"
    user_sifre = input("Dosyanın şifresini çözmek için gizli ifadeyi giriniz:\n")

    if user_sifre == secret_sifre: ##Kullanıcının girdiği şifre ile gerçek şifrenin eşleşip eşleşmediği kontrol edilir
        for file in files: #files listesindeki her dosya için döngü başlatılır
            with open(file, "rb") as thefile: # #dosya okuma modunda binary olarak açılır ve dosya nesnesi thefile değişkenine atanır
                contents = thefile.read() # #dosyanın içeriği okunur ve contents değişkenine atanır
            contents_decrypted = Fernet(secretkey).decrypt(contents) # #okunan içerik şifresi çözülür ve contents_decrypted değişkenine atanır
            with open(file, "wb") as thefile: # #dosya yazma modunda binary olarak açılır ve dosya nesnesi thefile değişkenine atanır
                thefile.write(contents_decrypted) #çözülmüş içerik dosyaya yazılır
        print("Dosyaların şifresi açıldı !!") 

    else:
        print("HATALI ŞİFRE")
