from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

#PART 1
master = Tk()
canvas = Canvas(master, height=450, width=750)
canvas.pack()


frame_ust = Frame(master, bg="#add8e6")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)


frame_alt_sol = Frame(master, bg="#add8e6")
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)


frame_alt_sag = Frame(master, bg="#add8e6")
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)


hatirlatma_tipi_etiket = Label(frame_ust,bg="#add8e6",text = "Hatırlatma tipi:", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10, side=LEFT)


hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menü = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "Dogun Günü",
    "Alışveriş",
    "Ödeme"
)
hatirlatma_tipi_acilir_menü.pack(padx=10,pady=10, side=LEFT)



hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, year=2019, month=6, day=22,
background='darkblue', foreground='white', borderwidth=2)
hatirlatma_tarih_secici.pack(padx=10, pady=10,side=RIGHT)

hatirlatma_tarihi_etiket = Label(frame_ust,bg="#add8e6",text = "Hatırlatma tarihi:", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10,pady=10, side=RIGHT)

#PART 2

Label(frame_alt_sol, text= "Hatırlatma yöntemi:",bg="#add8e6", font="Verdana 10 bold").pack(padx=10,pady=10, anchor= NW)

var = IntVar()
R1 = Radiobutton(frame_alt_sol, text = "Sisteme kaydet", variable = var, value=1, bg="#add8e6", font="Verdana 10 bold")
R1.pack(padx=15,pady=5, anchor= NW)

R2 = Radiobutton(frame_alt_sol, text = "E-Posta Gönder", variable = var, value=2, bg="#add8e6", font="Verdana 10 bold")
R2.pack(padx=15,pady=5, anchor= NW)

var1 = IntVar()
C1 = Checkbutton(frame_alt_sol,text = "Bir Hafta Önce", variable = var1, onvalue=1, offvalue=0,bg="#add8e6", font="Verdana 10 bold")
C1.pack(padx=25,pady=5, anchor= NW)

var2 = IntVar()
C2 = Checkbutton(frame_alt_sol,text = "Bir Gün Önce", variable = var2, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10 bold")
C2.pack(padx=25,pady=5, anchor= NW)

var3 = IntVar()
C3 = Checkbutton(frame_alt_sol,text = "Aynı Gün", variable = var3, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10 bold")
C3.pack(padx=25,pady=5, anchor= NW)

#PART 3
def gonder():
    son_mesaj = ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz başarılı bir şekilde kaydedilmiştir."

                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() == "" else "genel"
                tarih =hatirlatma_tarih_secici.get()
                mesaj =metin_alanı.get("1.0","end")

                with open("hatırlatmalar.txt", "w") as dosya:
                    dosya.write("{} kategorisinde,{} tarihine ve {} notuyla hatirlatma".format(tip,tarih,mesaj))
                    dosya.close()
            elif var.get() == 2:
                son_mesaj += "E-posta yoluyla hatırlatma size ulaşacaktır."
            messagebox.showinfo("Başarılı işlem",son_mesaj)
        else:
            son_mesaj += "Gerekli alanların doldurulduğundan emin olunuz."
            messagebox.showwarning("Yetersiz bilgi", son_mesaj)
    except:
        son_mesaj += "İşlem basarısız oldu."
        messagebox.showerror("Basarısız islem", son_mesaj)
    finally:
        master.destroy()


Label(frame_alt_sag, text= "Hatırlatma mesajı:",bg="#add8e6", font="Verdana 10 bold").pack(padx=10,pady=10, anchor= NW)
metin_alanı = Text(frame_alt_sag, height=9, width=50)
metin_alanı.tag_configure("style",foreground = "#bfbfbf", font =("Verdana", 7, "bold"))
metin_alanı.pack()
karsilama_metni ="Mesajınızı buraya giriniz..."
metin_alanı.insert(END, karsilama_metni, "style ")

gonder_butonu = Button(frame_alt_sag, text= "Gönder", command =gonder)
gonder_butonu.pack(anchor=S)


master.mainloop()