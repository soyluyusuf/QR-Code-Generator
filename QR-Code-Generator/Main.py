import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image
from fpdf import FPDF
import cv2


#Creating the window
win = Tk()
win.title('QR Code Generator')
win.geometry('650x650')
win.config(bg='DarkTurquoise')

#Function to generate the QR code and save it
def generateCode():
    try:
        qr = qrcode.QRCode(version=int(size.get()), box_size=10, border=5)
        qr.add_data(text.get())
        qr.make(fit=True)

        # Renkli QR kodu oluşturuyoruz (siyah-beyaz değil)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        fileDir = loc.get() + '\\' + name.get()
        img.save(f'{fileDir}.png')  # PNG kaydet

        # PDF olarak da kaydetmek için geçici JPG kaydet
        img.save('temp_qr.jpg')

        # PDF oluşturup JPG'yi içine yerleştir
        pdf = FPDF()
        pdf.add_page()
        pdf.image('temp_qr.jpg', x=60, y=60, w=90, h=90)  # Sayfa ortasına yerleştir
        pdf.output(f'{fileDir}.pdf', 'F')

        messagebox.showinfo("QR Code Generator", "QR Code PNG ve PDF olarak kaydedildi!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")

def readFromCamera():
    cap = cv2.VideoCapture(0)  # Kamerayı aç
    detector = cv2.QRCodeDetector()  # QR kod okuyucu başlat

    while True:
        ret, img = cap.read()
        if not ret:
            break
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            messagebox.showinfo("QR Okuma", f"QR İçeriği:\n{data}")
            break
        cv2.imshow("QR Kod Tarayıcı - ESC ile çık", img)
        if cv2.waitKey(1) == 27:  # ESC tuşu ile çık
            break

    cap.release()
    cv2.destroyAllWindows()



#Label for the window
headingFrame = Frame(win,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code 
Frame1 = Frame(win,bg="DarkTurquoise")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
label1 = Label(Frame1,text="Enter the text/URL: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
Frame2 = Frame(win,bg="DarkTurquoise")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label2 = Label(Frame2,text="Enter the location to save the QR Code: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name 
Frame3 = Frame(win,bg="DarkTurquoise")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting the input of the size of the QR Code
Frame4 = Frame(win,bg="DarkTurquoise")
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)

label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)

#Button to generate and save the QR Code
button = Button(win, text='Generate Code',font=('FiraMono',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)
cam_button = Button(win, text='Kameradan Oku', font=('FiraMono', 12), command=readFromCamera)
cam_button.place(relx=0.65, rely=0.9, relwidth=0.25, relheight=0.05)


#Runs the window till it is closed manually
win.mainloop()