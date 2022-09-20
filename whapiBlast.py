from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import requests
# from tqdm.auto import tqdm
import os
import time
import random
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import baileys_api 

# import wwjs_api
from datetime import datetime   
import threading


# create the root window
root = tk.Tk()
root.title('Whatsapp Sender v1.07')
root.resizable(False, False)
root.geometry('400x550')

def delaydulu():
    delay1 =textboxDelay.get("1.0", "end-1c")
    delay2 =textboxDelay2.get("1.0", "end-1c")
                
    time.sleep(random.randint(int(float(delay1)),int(float(delay2))))

def sendWa():
    senderNo = textboxSender.get("1.0", "end-1c")
    #trim senderNo
    senderNo = senderNo.strip()
    
     

    # print (senderNo)
    #load workbook
    wb = load_workbook('wassap.xlsx')
    ws = wb.active
    maxPB = ws.max_row-1
    maxPBr = 1/maxPB*100

    # with tqdm(total=int(maxPB)) as progress_bar:
    #iterate over rows by header name
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=6):
        syarikat = ws.cell(row=row[0].row, column=1).value
        phoneNo = ws.cell(row=row[0].row, column=2).value
        
        expDate = ws.cell(row=row[0].row, column=3).value
        #convert expDate to datetime
        expDate = datetime.strptime(expDate, '%d/%m/%Y')
        expDateF = expDate.strftime("%d %b %Y")
        gredSyarikat = ws.cell(row=row[0].row, column=4).value
        

        #compile message from text_widget
        message = text_widget.get("1.0", tk.END)
        message = message.replace('<syarikat>', syarikat)
        message = message.replace('<exp>', expDateF)
        message = message.replace('<gred>', gredSyarikat)
        message = message.replace('&', '%26')
        
        progress_bar['value']+=maxPBr
        #update tkinter label percent
        labelPercent.config(text=str(round(progress_bar['value'],2))+'%'+' '+'(' + str(row[0].row-1)+'/'+str(maxPB)+')')

        #print current iteration number
        # print(row[0].row)


        root.update_idletasks()
        
        #check if cell in column 4(status) is empty
        if ws.cell(row=row[0].row, column=5).value == None: 
            #progressbar
            
            # progress_bar.update(1)
            # print (message)
            

            

            #if empty, send message
            #guna whatsapp-web.js
            # response = wwjs_api.sendWhapi2(phoneNo, message)

            #guna whapi.io
            response = baileys_api.sendWhapi2(senderNo, phoneNo, message)
            #update cell with current date
            ws.cell(row=row[0].row, column=5).value = response
            ws.cell(row=row[0].row, column=6).value = datetime.now()
            # ws.cell(row=row[0].row, column=5).value = "response"
            
            #save workbook
            wb.save('wassap.xlsx')
            #update progress bar
            # add delay
            delaydulu()

        #else continue to next row
        else:
            # progress_bar.update(1)
            
            continue

        
        
        #update progress bar
        # progress['value'] = progress['value'] + 1
        # root.update_idletasks()





#create label
labelSender = tk.Label(root, text="Sender Number 601xxxxx (Wajib)")
#create textbox
textboxSender = tk.Text(root, height=1, width=14)


#create label
labelDelay = tk.Label(root, text="Delay Random from - to in seconds (wajib)")
labelDelay2 = tk.Label(root, text="-")

#create textbox
textboxDelay = tk.Text(root, height=1, width=10)
textboxDelay2 = tk.Text(root, height=1, width=10)

check_button = ttk.Button(
    root,
    text='Send',
    command=threading.Thread(target=sendWa).start
)

progress_bar = ttk.Progressbar(root, style='text.Horizontal.TProgressbar', length=300, mode='determinate')

labelPercent = ttk.Label(root, text="0%")

#create label
labelMsg = tk.Label(root, text="tulis Variable Header, contoh: <syarikat> <exp>") 

#create label
labelFile = tk.Label(root, text="Pastikan nama file adalah wassap.xlsx") 
labelFormat = tk.Label(root, text="format contoh: syarikat, phone, exp, gred, status, time") 
# Create the text widget
text_widget = tk.Text(root, height=15, width=40)
 

 


labelSender.pack()
textboxSender.pack()
labelDelay.pack()
textboxDelay.pack()
labelDelay2.pack()
textboxDelay2.pack()
labelMsg.pack()
 
text_widget.pack()
check_button.pack(pady=10)
progress_bar.pack(pady=5)
labelPercent.pack()
labelFile.pack()
labelFormat.pack()




# run the application
root.mainloop()