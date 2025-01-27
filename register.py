from tkinter import* 
from tkinter import ttk

from PIL import ImageTk
from tkinter import messagebox
import re
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")

        self.root.geometry("1366x768+0+0")
      
        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"Images_GUI/bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)        

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register", cursor='hand2', font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

    def validate_password(self, password):
        if len(password) < 6:
            return "Password must be at least 6 characters long."
        if not re.search(r'[A-Z]', password):
            return "Password must contain at least one uppercase letter."
        if not re.search(r'[a-z]', password):
            return "Password must contain at least one lowercase letter."
        if not re.search(r'[0-9]', password):
            return "Password must contain at least one digit."
        if not re.search(r'[@$!%*?&]', password):
            return "Password must contain at least one special character."
        return None
  
    def reg(self):
        # regExp
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # check for empty field
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")

            # check for number in name
        elif any(char.isdigit() for char in self.var_fname.get()):
            messagebox.showerror("Error", "First Name should not contain numbers!")
        elif any(char.isdigit() for char in self.var_lname.get()):
            messagebox.showerror("Error", "Last Name should not contain numbers!")
       
    #    mobile number validation
        elif not self.var_cnum.get().isdigit() or len(self.var_cnum.get()) != 10:
            messagebox.showerror("Error", "Invalid Contact Number! It should be a 10-digit number.")

    #       email validation
        elif not re.match(email_regex, self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Address!")
        
    #       password validation
        else:
            pwd_error = self.validate_password(self.var_pwd.get())
            if pwd_error:
                messagebox.showerror("Plaease enter strong password(a combination of uppercase,lowercase,special characters and numbers) with atleast 6 characters!", pwd_error)
            elif self.var_pwd.get() != self.var_cpwd.get():
                messagebox.showerror("Error", "Password and Confirm Password must match!")

            # checkbox validation
            elif self.var_check.get() == 0:
                messagebox.showerror("Error", "Please agree to the terms and conditions!")
            else:
                try:
                    conn = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='proj_db',port=3306)
                    mycursor = conn.cursor()
                    query=("select * from regteach where email=%s")
                    value=(self.var_email.get(),)
                    mycursor.execute(query,value)
                    row=mycursor.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email")
                    else:
                        mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_cnum.get(),
                        self.var_email.get(),
                        self.var_ssq.get(),
                        self.var_sa.get(),
                        self.var_pwd.get()
                        ))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()