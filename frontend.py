import requests 
import json
import datetime 
import tkinter as tk
from tkinter import Frame, Label, ttk
from tkinter.ttk import Treeview



# parminderfromspic@gmail.com
class final :
    
    def __init__(self):
                    
            
                
        self.app = tk.Tk()
        notebook = ttk.Notebook(self.app)

        self.tab1 = Frame(notebook)
       
        self.tab3 = Frame(notebook)



        notebook.add(self.tab1, text='World Currencies - USD')
        
        notebook.add(self.tab3, text='View Saved Data')

        notebook.pack()


        self.app.title("BTC Live Price")
        self.app.geometry("600x500")

        tk.Label(self.tab1 , width=70 , height=30).pack()
  
        tk.Label(self.tab3 , width=70 , height=30).pack()


        #TREE
        self.Currencies_Name = tk.StringVar()
        self.Price_USD = tk.StringVar()

        #TREE VIEW
        colummn = ('S_no','Currencies_Name','Date','Price_USD')
        
        self.tree = Treeview(self.tab3, columns=colummn , show='headings')
        self.tree.configure(height=18)
        self.tree.column('S_no', width=50)
        self.tree.column('Currencies_Name', width=130)
        self.tree.column('Price_USD', width=150)
        self.tree.column('Date', width=130)

        self.tree.heading('S_no', text='S No', )
        self.tree.heading('Currencies_Name', text='Currencies Name')
        self.tree.heading('Price_USD', text='Price USD')
        self.tree.heading('Date', text='Date')

        self.tree.place(x=0,y=0)
        
        
         

        bg = tk.PhotoImage(file = "E:\Python\py project(only front-end)\img.png")

        # Show image using label
        label_img = tk.Label( self.tab1, image = bg)
        label_img.place(x = 0, y = 0)

        
        bg2 = tk.PhotoImage(file = "E:\Python\py project(only front-end)\img.png")

    

        def feild_update():  
        
        
    # CUrrencies Rate 
        
            result = requests.get('https://exchange-rates.abstractapi.com/v1/live?api_key=056c487f42bc4a72b2482471271fcf62&base=USD')
            res = result.json()
            result_INR = json.dumps(res['exchange_rates']['INR'] , indent=2)
            result_EURO = json.dumps(res['exchange_rates']['EUR'] , indent=2)
            result_CANADA = json.dumps(res['exchange_rates']['CAD'] , indent=2)
            result_Indonesia = json.dumps(res['exchange_rates']['IDR'] , indent=2)



            print("inr - "+result_INR) 
            print("euro - "+result_EURO) 
            print("cad - "+result_CANADA) 
            print("Indo rs - "+result_Indonesia) 
            
            self.label1.config(text=result_INR)
            self.label2.config(text=result_EURO)
            self.label3.config(text=result_CANADA)
            self.label4.config(text=result_Indonesia)
            


    # Crypto Rates
            
            resultcrypto = requests.get('http://api.coinlayer.com/live?access_key=b607524beeee598cf749e95c32549981')
            res_crypto = resultcrypto.json()
            result_btc = json.dumps(res_crypto['rates']['BTC'] , indent=2)
            result_eth = json.dumps(res_crypto['rates']['ETH'] , indent=2)
            result_bnb = json.dumps(res_crypto['rates']['BNB'] , indent=2)
            result_xrp = json.dumps(res_crypto['rates']['XRP'] , indent=2)
            
            print("btc - "+result_btc) 
            print("eth - "+result_eth) 
            print("bnb - "+result_bnb) 
            print("xpr - "+result_xrp) 
            
            self.label5.config(text=result_btc)
            self.label6.config(text=result_eth)
            self.label7.config(text=result_bnb)
            self.label8.config(text=result_xrp)
            
            
            self.label5.after(16500,feild_update)

            
        #Tkinter Frontend Work
        # INR

        self.labelheading = tk.Label(self.tab1, text='Live Price From Exchange Rate - (USD)',fg='#5A5955' , background='#F0F0F0', font=('helvitica',15) )
        self.labelheading.place( x=50 , y = 15)


        self.label_inr = tk.Label(self.tab1, text = 'INDIAN - RUPEE' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_inr.place( x=20 , y = 50 )

        self.label1 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label1.place( x=230 , y = 50)


        #EURO
        self.label_EURO = tk.Label(self.tab1, text = 'EURO' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_EURO.place( x=20 , y = 75 )

        self.label2 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label2.place( x=230 , y = 75)

        #CAD
        self.label_CAD = tk.Label(self.tab1, text = 'CANAD-DOLLAR' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_CAD.place( x=20 , y = 100 )

        self.label3 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label3.place( x=230 , y = 100)

        #INDO_RS 
        self.label_INDO_RS = tk.Label(self.tab1, text = 'INDONES-RUPIAH' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_INDO_RS.place( x=20 , y = 125 )

        self.label4 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label4.place( x=230 , y = 125)



        #-------------------> Crypto Frontend

        #Tkinter Frontend Work
        # bitcoin


        self.labelheading_Crypto = tk.Label(self.tab1, text='LIVE PRICE CRYPTO-CURRENCIES - (USD)',fg='#5A5955' , background='#F0F0F0', font=('helvitica',15) )
        self.labelheading_Crypto.place( x=50 , y = 190)


        self.label_btc = tk.Label(self.tab1, text = 'BITCOIN' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_btc.place( x=20 , y = 225 )

        self.label5 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label5.place( x=230 , y = 225)


        #ETH
        self.label_eth = tk.Label(self.tab1, text = 'ETHEREUM' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_eth.place( x=20 , y = 250 )

        self.label6 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label6.place( x=230 , y = 250)

        #BNB
        self.label_bnb = tk.Label(self.tab1, text = 'BNB' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_bnb.place( x=20 , y = 275 )

        self.label7 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label7.place( x=230 , y = 275)

        #XRP 
        self.label_xrp = tk.Label(self.tab1, text = 'XRP' , background='#F0F0F0' , fg='#F0C21B', font=('helvitica',12) )
        self.label_xrp.place( x=20 , y = 300 )

        self.label8 = tk.Label(self.tab1, fg='#5A5955' , background='#F0F0F0', font=('helvitica',12) )
        self.label8.place( x=230 , y = 300)

        

        #Save button Label--------->
        self.label_save = tk.Label(self.tab1, text = 'Click on "SAVE BUTTON" to save real time values into Database -' , background='#F0F0F0' , fg='black', font=('helvitica',9) )
        self.label_save.place( x=20 , y = 370 )


        # #Buttons ----->
        # self.btnTAB1 = tk.Button(self.tab1, text="Save" ,command=self.Save )
        # self.btnTAB1.place(x=30 , y=390)
        
        # self.btnTAB3 = tk.Button(self.tab3, text="DELETE" ,command=self.dele )
        # self.btnTAB3.place(x=30 , y=400)


        # self.btn_update = tk.Button(self.tab3, text="Update" ,command=fetch )
        # self.btn_update.place(x=130 , y=400)

        

        feild_update()
        self.app.mainloop()
        
        

  
    

f = final()




                        