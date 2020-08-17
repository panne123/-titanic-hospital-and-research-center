from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox


def main():
    root=Tk()
    app=Window1(root)

class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy management system")
        self.master.geometry("600x700+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle =Label(self.frame,text= "Hospital management system",font =("araial",30,'bold'),bd=20,fg='green')
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1 = Frame(self.frame,width =600,height= 300,relief = 'ridge')
        self.Loginframe1.grid(row=1,column= 0)
        
        self.Loginframe2 = Frame(self.frame,width =600,height= 100,relief='ridge')
        self.Loginframe2.grid(row=2,column= 0)

        self.Loginframe3 = Frame(self.frame,width =600,height= 200,relief='ridge')
        self.Loginframe3.grid(row=4,column= 0,pady = 2 ,padx= 10)

#========================================================================================================================================================================================
        self.lblUsername =Label(self.Loginframe1,text= "USERNAME :",font =("arial",20,'bold'),bd=20,fg='black')
        self.lblUsername.grid(row=0,column=0)
        self.enterUsername =Entry(self.Loginframe1,font =("arial",20,'bold'),fg='blue',textvariable= self.Username)
        self.enterUsername.grid(row=0,column=1)
        
        self.lblPassword =Label(self.Loginframe1,text= "PASSWORD :",font =("arial",20,'bold'),bd=20,fg='black')
        self.lblPassword.grid(row=1,column=0)
        self.enterPassword =Entry(self.Loginframe1,font =("arial",20,'bold'),fg='blue',textvariable= self.Password,show='*')
        self.enterPassword.grid(row=1,column=1)

#========================================================================================================================================================================================
        
        self.btnlogin =Button(self.Loginframe2,text="Login",fg = 'green',command = self.login_system,width = 10,font = ('arial',20,'bold'))
        self.btnlogin.grid(row=0,column=0)

        self.btnReset =Button(self.Loginframe2,text="Reset",fg='purple',command = self.Reset,width = 10,font = ('arial',20,'bold'))
        self.btnReset.grid(row=0,column=1)

        self.btnExit =Button(self.Loginframe2,text="Exit",fg= 'red',command = self.Exit,width = 10,font = ('arial',20,'bold'))
        self.btnExit.grid(row=0,column=2)     



#========================================================================================================================================================================================


        

        self.btnRegistration =Button(self.Loginframe3,text="Patients Registration System",font = ('arial',15,'bold'),state = DISABLED,command = self.Registration_window)
        self.btnRegistration.grid(row=0,column=0,padx = 6,pady =8)

        self.btnHospital =Button(self.Loginframe3,text="Hospital Mangement system",font = ('arial',15,'bold'),state = DISABLED,command = self.Hospital_window)
        self.btnHospital.grid(row=0,column=1,padx = 6,pady =8)

#========================================================================================================================================================================================

    def login_system(self):
        user= (self.Username.get())
        psswd = (self.Password.get())

        if (user == 'admin') and (psswd == '12345'):
                
            self.btnRegistration.configure(state = NORMAL)
            self.btnHospital.configure(state = NORMAL)
        else:
            tkinter.messagebox.askyesno('Hospital Management System',"you have entered invalid Username or Password")
            self.btnRegistration.configure(state = DISABLED)
            self.btnHospital.configure(state = DISABLED)
            self.Username.set('')
            self.Password.set('')
            #self.txtUsername.focus()
                
    def Reset(self):
        self.btnRegistration.configure(state = DISABLED)
        self.btnHospital.configure(state = DISABLED)
        self.Username.set('')
        self.Password.set('')
        #self.txtUsername.focus()
    def Exit(self):
        self.Exit =tkinter.messagebox.askyesno('Hospital Management System',"Confirm if you want to exit.")
        if self.Exit >0:
            self.master.destroy()
            return
            
    
        
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2( self.newWindow)
        
    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3( self.newWindow)
        
class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Patient Registraion System")
        self.master.geometry("1300x800+0+0")
        self.frame=Frame(self.master)
        self.frame.grid()
        


        DateofOrder =StringVar()
        DateofOrder.set(time.strftime('%d/%m/%Y'))




        first_name=StringVar()
        last_name=StringVar()
        patient_address=StringVar()
        Sex=StringVar()
        patient_age=StringVar()
        email_id= StringVar()
        phone_no= StringVar()
        refrence_no = StringVar()
        MethofPayment=StringVar()
        var1=StringVar()
        
        color= "blue"
        Registration = StringVar()
        Registration.set("0")
        
        def Exit():
            Exit = tkinter.messagebox.askyesno("Member Registration System","Confirm you want to Exit.")
            if Exit >0:
                master.destroy()
                return

        def Reset():
            MethofPayment.set("")
            first_name.set("")
            last_name.set("")
            patient_address.set("")
            Sex.set("")
            patient_age.set("")
            email_id.set("")
            phone_no.set("")
            refrence_no.set("")
            
            
            
            
            var1.set("")
        def Delete():
            self.txtReceipt.delete("1.0",END)
            
        def ResetRecord():
            ResetRecord = tkinter.messagebox.askyesno("Member REgistration System","Confirm you want to reset.")
            if ResetRecord > 0:
                Reset()
            elif ResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return
        def Ref_No():
            #member_ref= StringVar()
            x= random.randint(1000,10000)
            randomRef =str(x)
            refrence_no.set(randomRef)
            #member_ref.set(randomRef)
        def Receipt():
            Ref_No()
            
            self.txtReceipt.insert(END, refrence_no.get()+ "\t\t" +first_name.get() + "\t\t" + last_name.get()+"\t\t\t" + patient_address.get() +"\t\t" + patient_age.get()
                                   + "\t\t" +email_id.get() +"\t\t"+ Sex.get() + "\t\t" + var1.get() + "\t" + phone_no.get()+ '\n')
            
            
        
        def registration_fees():
            if(var4.get() == 1):
                self.registration.configure(state = NORMAL)
                Item1 = float(50)
                registration.set("RS." + str(Item1))
            elif(var4.get() == 0):
                self.txtRegistration.configure(state = DISABLED)
                Registration.set("0")
            
            
            
#=========================================================FRAMES=========================================================================
        MainFrame=Frame(self.master)
        MainFrame.grid()
        
        TitleFrame=Frame(MainFrame,width=1000,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'),text="PATIENTS REGISTRATION",padx=5,fg='dark slate gray',bg='olive drab')
        self.lblTitle.grid()
    #==========================================================lower frames====================================================================================
        member_detail= LabelFrame(MainFrame , width = 1000, height = 500, bd =5 ,pady = 5,relief =RIDGE,bg='gray')
        member_detail.pack(side=BOTTOM)

        FrameDetail=LabelFrame(member_detail,bd=5, width= 400,height = 800, relief =RIDGE,bg='green')
        FrameDetail.pack(side=LEFT)

        patient_details = LabelFrame(FrameDetail,bd= 5, width= 350, height= 650,font=("arial",14,'bold'),text= "PATIENT DETAILS", relief = RIDGE,bg='gray')
        patient_details.grid(row=0,column=0)
        
        receipt_buttonFrame= LabelFrame(member_detail,bd =5, width = 600, height = 800,relief =RIDGE, bg="gray")
        receipt_buttonFrame.pack(side=RIGHT)

#==========================================================patient info.====================================================================================
        self.lblRefNo=Label( patient_details,font=('arial',14,'bold'),text="REF NO:",bd=5,fg=color,bg='gray')
        self.lblRefNo.grid(row=0,column=0,sticky = W)
        self.txtRefNo=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable = refrence_no)
        self.txtRefNo.grid(row=0,column=1)

        self.lblfirst_name=Label( patient_details,font=('arial',14,'bold'),text="FIRST NAME :",bd=5,pady= 4,padx=2,fg=color,bg='gray')
        self.lblfirst_name.grid(row=1,column=0,sticky = W)
        self.txtfirst_name=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable = first_name)
        self.txtfirst_name.grid(row=1,column=1)

        self.lbllast_name=Label( patient_details,font=('arial',14,'bold'),text="LAST NAME :",bd=5,fg=color,bg='gray')
        self.lbllast_name.grid(row=2,column=0,sticky = W)
        self.txtlast_name=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable= last_name)
        self.txtlast_name.grid(row=2,column=1)

        self.lblpatient_adress=Label( patient_details,font=('arial',14,'bold'),text="ADDRESS :",bd=5,pady= 4,padx=2,fg=color,bg='gray')
        self.lblpatient_adress.grid(row=3,column=0,sticky = W)
        self.txtpatient_adress=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable= patient_address)
        self.txtpatient_adress.grid(row=3,column=1)

        self.lblpatient_age=Label( patient_details,font=('arial',14,'bold'),text="PATIENT AGE :",bd=5,fg=color,bg='gray')
        self.lblpatient_age.grid(row=4,column=0,sticky = W)
        self.txtpatient_age=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable= patient_age)
        self.txtpatient_age.grid(row=4,column=1)
        self.lblemail_id=Label( patient_details,font=('arial',14,'bold'),text=" DISEASE :",bd=5,fg=color,bg='gray')
        self.lblemail_id.grid(row=5,column=0,sticky = W)
        self.txtemail_id=Entry( patient_details,font=('arial',14,'bold'),bd=7,textvariable=email_id)
        self.txtemail_id.grid(row=5,column=1)

     
        
        self.lblSex=Label( patient_details,font=('arial',14,'bold'),text="GENDER :",padx=2,pady=4,fg=color,bg='gray')
        self.lblSex.grid(row=6,column=0,sticky=W)
        
        self.cboSex=ttk.Combobox( patient_details,textvariable=Sex,state='readonly',
                                         font=('arial',14,'bold'),width=19)

        self.cboSex['value']=('','Male','Female','Other')
        self.cboSex.current(0)
        self.cboSex.grid(row=6,column=1)


        self.lblphon_number=Label( patient_details,font=('arial',14,'bold'),text="PHONE NUMBER :",bd=5,fg=color,bg='gray')
        self.lblphon_number.grid(row=7,column=0,sticky = W)
        self.txtphon_number=Entry( patient_details,font=('arial',14,'bold'),bd=5,textvariable = phone_no)
        self.txtphon_number.grid(row=7,column=1)

        self.lblDate=Label( patient_details,font=('arial',14,'bold'),text="DATE :",bd=5,fg=color,bg='gray')
        self.lblDate.grid(row=8,column=0,sticky = W)
        self.txtDate=Entry( patient_details,font=('arial',14,'bold'),bd=5,textvariable =DateofOrder)
        self.txtDate.grid(row=8,column=1)


        self.lblMethofPayment=Label( patient_details,font=('arial',14,'bold'),text="PAYMENT:",padx=2,pady=4,fg=color,bg='gray')
        self.lblMethofPayment.grid(row=9,column=0,sticky=W)
        
        self.cboMethofPayment=ttk.Combobox( patient_details,textvariable=MethofPayment,state='readonly',
                                         font=('arial',14,'bold'),width=19)

        self.cboMethofPayment['value']=('','Visa Card','Master Card','Cash','Paytm','Google Pay','Phone Pay')
        self.cboMethofPayment.current(0)
        self.cboMethofPayment.grid(row=9,column=1)
      

        #self.chkRegistration = Checkbutton(patient_details,text = "REGISTRAION FEES :",variable =var1,onvalue =1,offvalue = 0,font=('arial',14,'bold').grid(row =10,coulmn= 0,sticky =W)
        

        #self.txtRegistration =Entry( patient_details,font =('arial',14,'bold'),textvariable =Registration ,bd=7,insertwidth = 2,state = DISABLED,justify = RIGHT)
        #self.txtRegistration.grid(row= 10,column=1)                
#========================================================================================================================================================================================
        self.lbllabel= Label( receipt_buttonFrame,font=('arial',12,'bold'),pady = 10,padx=2,bg='gray',
        text= 'REF NO\t  FIRST NAME\t LAST NAME\t ADDRESS\t AGE\t DISEASE\t GENDER \t PHONE NUMBER\t',bd=7)
        self.lbllabel.grid(row= 0,column= 0,columnspan=4)

        self.txtReceipt= Text(receipt_buttonFrame,font=('arial',10,'bold'),pady = 10,width=145 ,height= 22,bg='brown')
        self.txtReceipt.grid(row= 1,column= 0,columnspan=4)

        #==============================================BUTTONS=================================================================================
        self.btnReceipt=Button(receipt_buttonFrame,text='RECEIPT',font=('arial',12,'bold'),width=27,bd=8,command=Receipt)
        self.btnReceipt.grid(row=2,column=0)
        self.btnReset=Button(receipt_buttonFrame,text='RESET',font=('arial',12,'bold'),width=20,bd=8,command=Reset)
        self.btnReset.grid(row=2,column=1)
        self.btnExit=Button(receipt_buttonFrame,text='EXIT',font=('arial',12,'bold'),width=20,bd=8,command=Exit)
        self.btnExit.grid(row=2,column=3)
        self.btnDELETE=Button(receipt_buttonFrame,text='DELETE',font=('arial',12,'bold'),width=20,bd=8,command=Delete)
        self.btnDELETE.grid(row=2,column=2)
        
    

       
#==========================================================window 3====================================================================================================        
class Window3:
    
    def __init__(self,master):
        self.master=master
        self.master.title("Hospital Management System")
        self.master.geometry("1300x800+0+0")
        self.frame=Frame(self.master)
        self.frame.grid()


        cmbNameTablets= StringVar()
        Ref= StringVar()
        Dose=StringVar()
        NumberTablets=StringVar()
        LOt=StringVar()
        IssueDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        Possiblesideeffects=StringVar()
        FurtherInformation=StringVar()
        Storageadvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientNHSNo=StringVar()
        Dateofbirth=StringVar()
        PatientName=StringVar()
        PatientId=StringVar()
        PatientAdress=StringVar()
        Prescription=StringVar()
        DateOfAdmission=StringVar()
        Sex=StringVar()
        rand=StringVar()
    
        
        #=======================================================================FunctionDatails======================================

        def iExit():
            iExit=tkinter.messagebox.askyesno("titanic Hospital Managment System","confirm if you want to exit")
            if iExit>0:
                self.master.destroy()
                return


        def iprescription():

         
            
            
            self.textprescription.insert(END,'Name Of Tablets:\t\t\t'+  cmbNameTablets.get()+"\n")
            self.textprescription.insert(END,'Referenc Number:\t\t\t'+  Ref.get()+"\n")
            self.textprescription.insert(END,'Dose:\t\t\t'+  Dose.get()+"\n")
            self.textprescription.insert(END,'Number Of Tablets:\t\t\t'+  NumberTablets.get()+"\n")
            self.textprescription.insert(END,'LOt:\t\t\t'+  LOt.get()+"\n")
            self.textprescription.insert(END,'Issue Date:\t\t\t'+ IssueDate.get()+"\n")
            self.textprescription.insert(END, 'Exp Date:\t\t\t'+  ExpDate.get()+"\n")
            self.textprescription.insert(END,'Daily Dose:\t\t\t'+  DailyDose.get()+"\n")
            self.textprescription.insert(END,'Storage Advice:\t\t\t'+  Storageadvice.get()+"\n")
            self.textprescription.insert(END,'PatientNHSNo:\t\t\t' +  PatientNHSNo.get()+"\n")
            self.textprescription.insert(END,'PatientName:\t\t\t' +  PatientName.get()+"\n")
            self.textprescription.insert(END,'DOB:\t\t\t' +  Dateofbirth.get()+"\n")
            self.textprescription.insert(END,'PatientAresss:\t\t\t' +  PatientAdress.get()+"\n")
            self.textprescription.insert(END,'Sex:\t\t\t' +  Sex.get()+"\n")
            
            
            


            return

        def iprescriptionData():
            
            
            self.textFrameDetail.insert(END,cmbNameTablets.get()+"\t\t"+Ref.get()+"\t"+Dose.get()+"\t"+
            NumberTablets.get()+"\t" +LOt.get()+"\t\t"+IssueDate.get()+"\t\t"+ExpDate.get()+"\t\t"+
            DailyDose.get()+"\t\t"+Storageadvice.get()+"\t"+PatientNHSNo.get()+"\t\t"+PatientName.get()+
                                        "\t"+Dateofbirth.get()+"\t"+PatientAdress.get()+"\n",)

            return
            

        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            LOt.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            Possiblesideeffects.set("")
            FurtherInformation.set("")
            Storageadvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientNHSNo.set("")
            Dateofbirth.set("")
            PatientName.set("")
            PatientId.set("")
            PatientAdress.set("")
            DateOfAdmission.set("")
            Sex.set("")
            self.textprescription.delete("1.0",END)
            self.textFrameDetail.delete("1.0",END)
                


            return


        def iReset():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            LOt.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            Possiblesideeffects.set("")
            FurtherInformation.set("")
            Storageadvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientNHSNo.set("")
            Dateofbirth.set("")
            PatientName.set("")
            PatientId.set("")
            PatientAdress.set("")
            DateOfAdmission.set("")
            Sex.set("")
            self.textprescription.delete("1.0",END)
            self.textFrameDetail.delete("1.0",END)
            
       

            return
            

      #---------------------------------------------------------------------------------------------frame--------------------------------------------
        MainFrame=Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=5,width=1585,padx=20,relief=RIDGE,bg="red")
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'),text="APOLLO*HOSPITAL*AND*RESEARCH*CENTER",padx=2,bg="red")
        self.lblTitle.grid()
        
        FrameDetail=Frame(MainFrame,bd=5,width=1600, height=100,padx=20,relief=RIDGE,bg="red")
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=5,width=1600,height=50,padx=20,relief=RIDGE,bg="red")
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=5,width=1600,height=400,padx=20,relief=RIDGE,bg="red")
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=1000,height=400,padx=20,relief=RIDGE,bg="red"
                            ,font=('arial',12,'bold'),text="patients Information:")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=400,padx=20,relief=RIDGE
                              ,font=('arial',12,'bold'),text="Prescription:",bg="red")
        DataFrameRIGHT.pack(side=RIGHT)
        #-------------------------------------------------FrameLEFT-------------------------------------------------------------
        self.lblNameTablet=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Name Of Tablets:",padx=2,pady=4,bg="red")
        self.lblNameTablet.grid(row=0,column=0,sticky=W)
        
        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state='readonly',
                                         font=('arial',12,'bold'),width=23)

        self.cboNameTablet['value']=('','Inbuprofen','Co-codamol','Paracetamol','Amlodupine','Althrosine','Calpol','Seridone' 'Acilock','Clidakem','Avemom ht','Glycobira','Sumo')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Further Information:",padx=2,pady=4,bg="red")
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.textFurtherInfo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation,width=25)
        self.textFurtherInfo.grid(row=0,column=3)

        self.lblRef=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Reference NO:",padx=2,pady=4,bg="red")
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.textRef=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.textRef.grid(row=1,column=1)

        self.lblStorage=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=4,bg="red")
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.textStorage=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Storageadvice,width=25)
        self.textStorage.grid(row=1,column=3)

        self.lblDose=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dose:",padx=2,pady=4,bg="red")
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.textDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose,width=25)
        self.textDose.grid(row=2,column=1)


        self.lblDUseMachine=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Driving Machine:",padx=2,pady=4,bg="red")
        self.lblDUseMachine.grid(row=2,column=2,sticky=W)
        self.textDUseMachine=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DrivingUsingMachines,width=25)
        self.textDUseMachine.grid(row=2,column=3)

        self.lblNoOftablets=Label(DataFrameLEFT,font=('arial',12,'bold'),text="No. Of Tablets:",padx=2,pady=4,bg="red")
        self.lblNoOftablets.grid(row=3,column=0,sticky=W)
        self.textNoOftablets=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=NumberTablets,width=25)
        self.textNoOftablets.grid(row=3,column=1)

        self.lblUseMedication=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Use Of Medication:",padx=2,pady=4,bg="red")
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.textUseMedication=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=HowtoUseMedication,width=25)
        self.textUseMedication.grid(row=3,column=3)

        self.lblPatientName=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Name:",padx=2,pady=4,bg="red")
        self.lblPatientName.grid(row=4,column=0,sticky=W)
        self.textPatientName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientName,width=25)
        self.textPatientName.grid(row=4,column=1)

        
        self.lblPatientId=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Id:",padx=2,pady=4,bg="red")
        self.lblPatientId.grid(row=4,column=2,sticky=W)
        self.textPatientId=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientId,width=25)
        self.textPatientId.grid(row=4,column=3)

        self.lblSex=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Sex:",padx=2,pady=4,bg="red")
        self.lblSex.grid(row=5,column=0,sticky=W)
        
        self.cboSex=ttk.Combobox(DataFrameLEFT,textvariable=Sex,state='readonly',
                                         font=('arial',12,'bold'),width=23)

        self.cboSex['value']=('','Male','Female','Other')
        self.cboSex.current(0)
        self.cboSex.grid(row=5,column=1)


        self.lblDateOfBirth=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date Of Birth:",padx=2,pady=4,bg="red")
        self.lblDateOfBirth.grid(row=5,column=2,sticky=W)
        self.textDateOfBirth=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dateofbirth,width=25)
        self.textDateOfBirth.grid(row=5,column=3)


        self.lblSideEffects=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Side Effect:",padx=2,pady=4,bg="red")
        self.lblSideEffects.grid(row=6,column=0,sticky=W)
        self.textSideEffects=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Possiblesideeffects,width=25)
        self.textSideEffects.grid(row=6,column=1)

        self.lblIssueDate=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Issue Date:",padx=2,pady=4,bg="red")
        self.lblIssueDate.grid(row=6,column=2,sticky=W)
        self.textIssueDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=IssueDate,width=25)
        self.textIssueDate.grid(row=6,column=3)

        self.lblNHSNumber=Label(DataFrameLEFT,font=('arial',12,'bold'),text="NHS Number:",padx=2,pady=4,bg="red")
        self.lblNHSNumber.grid(row=7,column=0,sticky=W)
        self.textNHSNumber=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientNHSNo,width=25)
        self.textNHSNumber.grid(row=7,column=1)

        self.lblExpDate=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Exp.Date:",padx=2,pady=4,bg="red")
        self.lblExpDate.grid(row=7,column=2,sticky=W)
        self.textExpDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=ExpDate,width=25)
        self.textExpDate.grid(row=7,column=3)

        self.lblLot=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Lot:",padx=2,pady=4,bg="red")
        self.lblLot.grid(row=8,column=0,sticky=W)
        self.textLot=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=LOt,width=25)
        self.textLot.grid(row=8,column=1)
        
        self.lblDailyDose=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Daily Dose:",padx=2,pady=4,bg="red")
        self.lblDailyDose.grid(row=8,column=2,sticky=W)
        self.textDailyDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DailyDose,width=25)
        self.textDailyDose.grid(row=8,column=3)
        
        #----------------------------------------------------FrameRIGHT-------------------------------------------------------
        self.textprescription=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=61,height=14,padx=2,pady=4,bg="brown")
        self.textprescription.grid(row=0,column=0)
        #--------------------------------------------------------Buttonframme---------------------------------------
        self.btnprescription=Button(ButtonFrame,text='prescription',font=('arial',12,'bold'),width=27,bd=6,command=iprescription)
        self.btnprescription.grid(row=0,column=0)
        self.btnprescriptionData=Button(ButtonFrame,text='prescription Data',font=('arial',12,'bold'),width=27,bd=6,command=iprescriptionData)
        self.btnprescriptionData.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width=27,bd=6,command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width=27,bd=6,command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=27,bd=6,command=iExit)
        self.btnExit.grid(row=0,column=4)
        
        
        #--------------------------------------------------------frammedeatils---------------------------------------
        
        self.lblLabel=Label(FrameDetail,font=('arial',11,'bold'),text="Name Of Tablets \t  Reference No.\tDoses\t  No.Of Tablets\t Lot\t Issue Date \t Exp. Date\t Daily Dose \t Storage Adv. \t NHS Number \t Patient Name \t DOB \t Adress\tSex",pady=10, padx=2)
        self.lblLabel.grid(row=0,column=0)
        


        self.textFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=159,height=4,padx=2,pady=4,bg="brown")
        self.textFrameDetail.grid(row=1,column=0)


        



        





        

        

        
        
        
                                  
                                  




if __name__ == '__main__':
    main()


