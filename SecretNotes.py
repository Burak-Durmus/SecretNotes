import tkinter
from PIL import Image,ImageTk
import tkinter.messagebox
from tkinter import END
import base64

# lock algoritması
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



# screeen
screen = tkinter.Tk()
screen.title("Secret Notes")
screen.minsize(350,550)
screen.config(padx=15,pady=10)

FONT = ("Arial",10,"normal")

# image 
image = Image.open("indir.png")
image = ImageTk.PhotoImage(image=image)
image_label = tkinter.Label(screen,image=image)
image_label.pack()

# label for title
forTitle_label = tkinter.Label(text="Enter your title",padx=10,pady=10,font=FONT)
forTitle_label.pack()

# entry fot title 
forTitle_entry = tkinter.Entry(bg="light blue")
forTitle_entry.pack()


# label for secret
yourSecret = tkinter.Label(text="Enter your secret",padx=10,pady=10,font=FONT)
yourSecret.pack()

# write your secret
yourSecret_writen = tkinter.Text(bg="light blue",padx=10,pady=10,width=15,height=7)
yourSecret_writen.pack()

#label for password
password_label = tkinter.Label(text="Enter your password",padx=10,pady=10,font=FONT)
password_label.pack()

# entry fot password
password_entry = tkinter.Entry(bg="light blue")
password_entry.pack()


def for_save():
    kilitli = ""
    if str(forTitle_entry.get()).strip() == "" or str(yourSecret_writen.get(index1="1.0",index2=END)).strip() == ""  or str(password_entry.get()).strip() == "":
        show_massage()
    else:
        kilitli += encode(password_entry.get(), yourSecret_writen.get(index1="1.0", index2=END))
        yazici = open(file="Secret.txt",mode="a")
        yazici.write(f"\n{forTitle_entry.get()}\n{kilitli}")
        yazici.close()
        forTitle_entry.delete(first=0,last=END)
        yourSecret_writen.delete(index1="1.0",index2=END)
        password_entry.delete(first=0,last=END)

def for_open():
    if str(yourSecret_writen.get(index1="1.0",index2=END)).strip() == ""  or str(password_entry.get()).strip() == "":
        show_massage()
    else:
        cikti = decode(password_entry.get(),yourSecret_writen.get(index1="1.0",index2=END))
        yourSecret_writen.delete(index1="1.0",index2=END)
        password_entry.delete(first=0,last=END)
        yourSecret_writen.insert("1.0",f"{cikti}")




# massage box 
def show_massage():
    tkinter.messagebox.showerror("Hata:","Bigiler eksik ya da hatalıdır")
# save button
save_button = tkinter.Button(text="Save",width=8,command=for_save)
save_button.pack()

# open button
open_button = tkinter.Button(screen,text="Open",padx=5,pady=5,command=for_open)
open_button.pack(side="bottom") # ekran küçük olduğu için 

screen.mainloop()