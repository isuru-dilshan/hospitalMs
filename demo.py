from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameofTablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMediaction=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="light blue",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\HospitalMs\Image\h.jpg")
        img1=img1.resize((100,76),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=80,y=20)

        # ================ DataFrame ===============================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,bg="powder blue",relief=RIDGE,padx=10,font=("times new roman",16,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10,bg="powder blue",relief=RIDGE, padx=10, font=("times new roman", 16, "bold"),text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # ================ Button Frame ===========================================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ================ Details Frame ==========================================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ================ DataFrameLeft ===========================================
        lblNameTablet=Label(DataFrameLeft,text="Name Of Tablet:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.NameofTablets,width=33)
        comNametablet["values"]=("Nice","CoronaVacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,text="Reference No:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=32)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),bg="powder blue",text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=32)
        txtDose.grid(row=2,column=1)

        lblNoOFTablet=Label(DataFrameLeft,text="No Of Tablet:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOFTablet.grid(row=3,column=0,sticky=W)
        txtNoOFTablet=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=32)
        txtNoOFTablet.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,text="Lot:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=32)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,text="Issue Date:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.IssueDate,width=32)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,text="Exp Date:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=32)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,text="Daily Dose:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=32)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,text="Side Effect:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=32)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinformation=Label(DataFrameLeft,text="Further Information:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblFurtherinformation.grid(row=0,column=2,sticky=W)
        txtFurtherinformation=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=32)
        txtFurtherinformation.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,text="Blood Pressure:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=32)
        txtBloodPressure.grid(row=1,column=3)

        lblStorageAdvice=Label(DataFrameLeft,text="Storage Advice:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=32)
        txtStorageAdvice.grid(row=2,column=3)

        lblMedication=Label(DataFrameLeft,text="Medication:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMediaction,width=32)
        txtMedication.grid(row=3,column=3)

        lblPatientID=Label(DataFrameLeft,text="Patient Id:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=32)
        txtPatientID.grid(row=4,column=3)

        lblNHSNumber=Label(DataFrameLeft,text="NHS Number:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=32)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,text="Patient Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=32)
        txtPatientName.grid(row=6,column=3)

        lblDataOfBirth=Label(DataFrameLeft,text="Date of Birth:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDataOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=32)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft,text="Patient Address:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=32)
        txtPatientAddress.grid(row=8,column=3)

        # =========================== DataFrameRight ====================================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        # =========================== Button ===========================================
        btnPrescription=Button(Buttonframe,text="Prescription",command=self.iPrectioption,bg="Blue",fg="white",font=("arial",13,"bold"),width=24)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",command=self.iPrescriptionData,bg="Blue",fg="white",font=("arial",13,"bold"),width=24)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="Blue",fg="white",command=self.Update,font=("arial",13,"bold"),width=24)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="red",fg="white",command=self.idelete,font=("arial",13,"bold"),width=24)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="Blue",fg="white",command=self.clear,font=("arial",13,"bold"),width=24)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="red",fg="white",command=self.Exit,font=("arial",13,"bold"),width=24)
        btnExit.grid(row=0,column=5)

        # =================================== Table ==================================

        # =================================== Scrollbar ==============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name OF Tablets")
        self.hospital_table.heading("ref",text="Reference NO.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No OF Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.farch_data()

    # ====================== Functionality Dec =====================================
    def iPrescriptionData(self):
        if self.NumberofTablets.get()==""or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="7986@1223Id",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.NameofTablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.IssueDate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvice.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()

                                                                                                    ))
            conn.commit()
            self.farch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def Update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_NO=%s",(

                                                                                             self.NameofTablets.get(),
                                                                                             self.Dose.get(),
                                                                                             self.NumberofTablets.get(),
                                                                                             self.Lot.get(),
                                                                                             self.IssueDate.get(),
                                                                                             self.ExpDate.get(),
                                                                                             self.DailyDose.get(),
                                                                                             self.StorageAdvice.get(),
                                                                                             self.nhsNumber.get(),
                                                                                             self.PatientName.get(),
                                                                                             self.DateOfBirth.get(),
                                                                                             self.PatientAddress.get(),
                                                                                             self.ref.get()
                                                                                                                ))
        conn.commit()
        self.farch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been Updated")

    def farch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.NameofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference NO:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        query="delete from hospital where Reference_NO=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.farch_data()
        messagebox.showinfo("Deleted","Patient has been deleted successfully")

    def clear(self):
        self.NameofTablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMediaction.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def Exit(self):
        Exit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if Exit>0:
            root.destroy()
            return

root=Tk()
obj=Hospital(root)
root.mainloop()


