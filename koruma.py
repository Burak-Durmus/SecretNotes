



def decode(key, enc):
    # Giriş verisinin uzunluğunu 4'ün katı yapacak şekilde padding ekle
    missing_padding = len(enc) % 4
    if missing_padding:
        enc += '=' * (4 - missing_padding)
    
    # Base64 çözme işlemi
    try:
        enc = base64.urlsafe_b64decode(enc).decode()
    except Exception as e:
        print(f"Decoding error: {e}")
        return None

    dec = []
    # Anahtarı kullanarak çözme işlemi
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
        
    return "".join(dec)






def for_save():
    kilitli = ""
    if str(forTitle_entry.get()).strip() == "" or str(yourSecret_writen.get(index1="1.0",index2=END)).strip() == "" or str(password_entry.get()).strip() == "":
        show_massage()
    else:
        # Encode işlemi için şifre (key) password_entry'den, şifrelenecek veri (clear) yourSecret_writen'den alınmalı
        kilitli += encode(password_entry.get(), yourSecret_writen.get(index1="1.0", index2=END))
        
        # Dosyaya yazma işlemi
        yazici = open(file="Secret.txt", mode="a")
        yazici.write(f"\n{forTitle_entry.get()}\n{kilitli}")
        yazici.close()
        
        # Giriş kutularını temizleme
        forTitle_entry.delete(first=0, last=END)
        yourSecret_writen.delete(index1="1.0", index2=END)
        password_entry.delete(first=0, last=END)

def for_open():
    if str(yourSecret_writen.get(index1="1.0", index2=END)).strip() == "" or str(password_entry.get()).strip() == "":
        show_massage()
    else:
        # Decode işlemi için şifrelenmiş veri (enc) yourSecret_writen'den, anahtar (key) password_entry'den alınmalı
        cikti = decode(password_entry.get(), yourSecret_writen.get(index1="1.0", index2=END))
        
        # Giriş kutularını temizleme
        yourSecret_writen.delete(index1="1.0", index2=END)
        password_entry.delete(first=0, last=END)
        
        # Çözülen veriyi ekrana yazdırma
        yourSecret_writen.insert("1.0", f"{cikti}")

