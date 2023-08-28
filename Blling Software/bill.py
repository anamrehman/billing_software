from tkinter import *
import math, random, os, tempfile, qrcode
from tkinter import messagebox
from PIL import Image,ImageTk
from resizeimage import resizeimage
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x1040+0+0")
        self.root.title("BILLING SOFTWARE")
        bg_color="#074463"
        title=Label(self.root,text="BILLING SOFTWARE",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #==========Variables==============
        #==========Cosmetics==============
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gel=IntVar()
        self.lotion=IntVar()
        self.shampoo=IntVar()

        #==========Grocery===============
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.salt=IntVar()


        #==========Cold Drinks============
        self.maza=IntVar()
        self.coak=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.pepsi=IntVar()
        self.sprite=IntVar()
        self.slice=IntVar()


        #==========Total Product & Tax Variables========
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()


        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()



        #==========customer==========
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,500000)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        



        #===============CUSTOMER DETAIL FRAME==============
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="CUSTOMER  DETAILS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)


        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        


        #========Cosmetic frame==========
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETIC",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=10,y=190,width=325,height=450)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.bath_soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_spray_txt=Entry(F2,width=10,textvariable=self.hair_spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        shampoo_lbl=Label(F2,text="Shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        shampoo_txt=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)


        
        #========Grocery frame==========
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="GROCERY",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=350,y=190,width=325,height=450)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        g7_lbl=Label(F3,text="Salt",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        g7_txt=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)


        
        #========Cold Drink frame==========
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="COLD DRINKS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=690,y=190,width=325,height=450)

        c1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Coak",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.coak,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        c7_lbl=Label(F4,text="Slice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F4,width=10,textvariable=self.slice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)


        #========Bill Area with Qr Code===========
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1070,y=190,width=440,height=450)
       
        bill_title=Label(F5,text="Bill Area With QR ",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        self.qr_code=Label(self.txtarea)
        self.qr_code.place(x=120,y=130,width=180,height=180)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        

        #=======Button Frame =============
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=660,relwidth=1,height=170)

        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=15)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=15)

        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=755,width=760,height=130)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 16 bold").grid(row=0,column=0,padx=5,pady=15)
        generate_QR_btn=Button(btn_F,text="Generate Bill & QR",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=16,font="arial 16 bold").grid(row=0,column=1,padx=5,pady=15)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 16 bold").grid(row=0,column=2,padx=5,pady=15)
        exit=t_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 16 bold").grid(row=0,column=3,padx=5,pady=15)
        self.welcome_bill()

        
        
        
    

    def total(self):
        self.b_s_p=self.bath_soap.get()*30
        self.f_c_p=self.face_cream.get()*120
        self.f_w_p=self.face_wash.get()*60
        self.h_s_p=self.hair_spray.get()*200
        self.h_g_p=self.hair_gel.get()*110
        self.l_p=self.lotion.get()*160
        self.s_p=self.shampoo.get()*170
                                      
        self.total_cosmetic_price=float(
                                     self.b_s_p+
                                     self.f_c_p+
                                     self.f_w_p+
                                     self.h_s_p+
                                     self.h_g_p+
                                     self.l_p+
                                     self.s_p
                                )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round(self.total_cosmetic_price*0.03)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*90
        self.g_fo_p=self.food_oil.get()*175
        self.g_d_p=self.daal.get()*100
        self.g_w_p=self.wheat.get()*35
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*110
        self.g_sa_p=self.salt.get()*20
        self.total_grocery_price=float(
                                     self.g_r_p+
                                     self.g_fo_p+
                                     self.g_d_p+
                                     self.g_w_p+
                                     self.g_s_p+
                                     self.g_t_p+
                                     self.g_sa_p
                                      )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.03)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.cd_m_p=self.maza.get()*50
        self.cd_co_p=self.coak.get()*60
        self.cd_fr_p=self.frooti.get()*50
        self.cd_tu_p=self.thumbsup.get()*40
        self.cd_pe_p=self.pepsi.get()*40
        self.cd_sp_p=self.sprite.get()*40
        self.cd_sl_p=self.slice.get()*50
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_co_p+
                                    self.cd_fr_p+
                                    self.cd_tu_p+
                                    self.cd_pe_p+
                                    self.cd_sp_p+
                                    self.cd_sl_p
                                      )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round(self.total_cold_drink_price*0.03)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_Bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tWELCOME TO PAAM MART \n")
        self.txtarea.insert(END,f"\n BILL NUMBER: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER NAME: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n PHONE NUMBER: {self.c_phone.get()}")
        self.txtarea.insert(END,"\n=================================================")
        self.txtarea.insert(END,"\n Products\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n=================================================")
    
    def generate(self):
        qr_data=(f"\t\tWELCOME TO PAAM MART \n\n BILL NUMBER: {self.bill_no.get()}\n CUSTOMER NAME: {self.c_name.get()}\n PHONE NUMBER: {self.c_phone.get()}\n=================================================\n Products\t\t\tQTY\t\tPrice\n=================================================\n BATH SOAP\t\t\t{self.bath_soap.get()}\n FACE CREAM\t\t\t{self.face_cream.get()}\n FACE WASH\t\t\t{self.face_wash.get()}\n HAIR SPRAY\t\t\t{self.hair_spray.get()}\n HAIR GEL\t\t\t{self.hair_gel.get()}\n LOTION\t\t\t{self.lotion.get()}\n SHAMPOO\t\t\t{self.shampoo.get()}\n RICE\t\t\t{self.rice.get()}\n FOOD OIL\t\t\t{self.food_oil.get()}\n DAAL\t\t\t{self.daal.get()}\n WHEAT\t\t\t{self.wheat.get()}\n SUGAR\t\t\t{self.sugar.get()}\n TEA\t\t\t{self.tea.get()}\n SALT\t\t\t{self.salt.get()}\n MAZA\t\t\t{self.maza.get()}\n COAK\t\t\t{self.coak.get()}\n FROOTI\t\t\t{self.frooti.get()}\n THUMBUPS\t\t\t{self.thumbsup.get()}\n PEPSI\t\t\t{self.pepsi.get()}\n SPRITE\t\t\t{self.sprite.get()}\n SLICE\t\t\t{self.slice.get()}\n-------------------------------------------------\n COSMETIC TAX:\t\t\t\t{self.cosmetic_tax.get()}\n GROCERY TAX:\t\t\t\t{self.grocery_tax.get()}\n COLD DRINKS TAX:\t\t\t\t{self.cold_drink_tax.get()}\n TOTAL BILL:\t\t\t\tRs.{self.Total_Bill}\n-------------------------------------------------")
        qr_code=qrcode.make(qr_data)
        qr_code=resizeimage.resize_cover(qr_code,[180,180])
        qr_code.save("customer_bills/"+str(self.bill_no.get())+".png")
        self.im=ImageTk.PhotoImage(file="customer_bills/"+str(self.bill_no.get())+".png")
        self.qr_code.config(image=self.im)


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details Are Must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            
            self.welcome_bill()
            self.generate()
            
    
    

    def clear_data(self):
        #==========Variables==============
        #==========Cosmetics==============
        self.bath_soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.hair_gel.set(0)
        self.lotion.set(0)
        self.shampoo.set(0)

        #==========Grocery===============
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        self.salt.set(0)


        #==========Cold Drinks============
        self.maza.set(0)
        self.coak.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.pepsi.set(0)
        self.sprite.set(0)
        self.slice.set(0)


        #==========Total Product & Tax Variables========
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")


        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")



        #==========customer==========
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,500000)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()
        self.qr_code.config(image='')
        

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit ?")
        if op>0:
            self.root.destroy()
  

root=Tk()
obj = bill_app(root)
root.mainloop()