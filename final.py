from tkinter import *
from math import *

class test():
	def __init__(self):
		self.a=dict(name="",usn="",q1="",q2="",q3="",q4="",t1="",t2="",ass="")

		
		self.resulttable=Tk()
		self.resulttable.geometry("1500x1500")
		self.resulttable.config()
		self.ent=Frame(self.resulttable)
		self.ent.grid()
		self.res1=Frame(self.resulttable)
		self.res1.grid()
		self.execute()
		self.key=1
		self.res2=Frame(self.resulttable)		
		self.res2.grid()
		self.entab()
	def execute(self):

		ht=2
		wt=8
		Label(self.res1,text=" Subjects ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=1)
		Label(self.res1,text=" Quize 1 ",justify=LEFT,relief="solid",bd=2,font="Times 15",width=wt,height=ht).grid(row=1,column=2)
		Label(self.res1,text=" Quize 2 ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=3)
		Label(self.res1,text=" Quize 3 ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=4)
		Label(self.res1,text=" Quize 4 ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=5)
		Label(self.res1,text=" Test 1 ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=6)
		Label(self.res1,text=" Test 2 ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=7)
		Label(self.res1,text=" Assgt ",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15").grid(row=1,column=8)
		Label(self.res1,text="Credits",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15",bg="yellow").grid(row=1,column=9)
		Label(self.res1,text="Total",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 15",bg="green",fg="white").grid(row=1,column=10)
		print("EXECUTE success")

	def alldestroys(self):
		self.resulttable.destroy()
		self.errorwin.destroy()

	def result(self):
		q=50/17
		wt=9
		ht=2
		if(self.a['name'].get()==""):
			print("Exit this")
			self.errorwin=Tk()
			self.errorwin.geometry("350x50")
			self.errorwin.title("ERROR")
			Label(self.errorwin,text="Sorry!\n No data Added. Press OK to exit").pack()
			Button(self.errorwin,text="   OK   ",bg="red",fg="white",command=self.alldestroys ).pack()
			self.errorwin.mainloop()

		else:
			print(self.key)
			Label(self.res2,text=self.a['name'].get(),bg="blue",fg="white",justify=LEFT,width=wt,relief="solid",bd=2,height=ht,font="Times 13").grid(row=self.key,column=1)
			Label(self.res2,text=ceil((int(self.a['q1'].get()))/5),width=wt,height=ht,justify=LEFT,relief="solid",bd=2,font="Times 13").grid(row=self.key,column=2)
			Label(self.res2,text=ceil((int(self.a['q2'].get()))/5),justify=LEFT,width=wt,height=ht,relief="solid",bd=2,font="Times 13").grid(row=self.key,column=3)
			Label(self.res2,text=ceil((int(self.a['q3'].get()))/5),justify=LEFT,width=wt,height=ht,relief="solid",bd=2,font="Times 13").grid(row=self.key,column=4)
			Label(self.res2,text=ceil((int(self.a['q4'].get()))/5),justify=LEFT,width=wt,height=ht,relief="solid",bd=2,font="Times 13").grid(row=self.key,column=5)
			Label(self.res2,text=ceil((int(self.a['t1'].get()))/q),justify=LEFT,width=wt,height=ht,relief="solid",bd=2,font="Times 13").grid(row=self.key,column=6)
			Label(self.res2,text=ceil((int(self.a['t2'].get()))/q),justify=LEFT,relief="solid",bd=2,width=wt,height=ht,font="Times 13").grid(row=self.key,column=7)
			Label(self.res2,text=ceil((int(self.a['ass'].get()))),relief="solid",bd=2,justify=LEFT,width=wt,height=ht,font="Times 13").grid(row=self.key,column=8)
			t=ceil((int(self.a['ass'].get())))+ceil((int(self.a['t2'].get()))/q)+ceil((int(self.a['t1'].get()))/q)+ceil((int(self.a['q1'].get()))/5)+ceil((int(self.a['q2'].get()))/5)+ceil((int(self.a['q3'].get()))/5)+ceil((int(self.a['q4'].get()))/5)
			Label(self.res2,text=self.a['usn'].get(),font="Times 13",justify=LEFT,relief="solid",bd=2,width=wt,height=ht,bg="yellow").grid(row=self.key,column=9)
			Label(self.res2,text=t,justify=LEFT,font="Times 13",relief="solid",bd=2,width=wt,height=ht,bg="green",fg="white").grid(row=self.key,column=10)
			self.key=self.key+1

			print("result success")
			print(self.a['name'].get())


	def entab(self):
		i=1
		j=1
		self.a['name']=StringVar()
		label=Label(self.ent,text="Subject")
		entry=Entry(self.ent,textvariable=self.a['name'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['usn']=StringVar()
		label=Label(self.ent,text="Credits of Subjects")
		entry=Entry(self.ent,textvariable=self.a['usn'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['q1']=StringVar()
		label=Label(self.ent,text="Quize 1")
		entry=Entry(self.ent,textvariable=self.a['q1'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['q2']=StringVar()
		label=Label(self.ent,text="Quize 2")
		entry=Entry(self.ent,textvariable=self.a['q2'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['q3']=StringVar()
		label=Label(self.ent,text="Quize 3")
		entry=Entry(self.ent,textvariable=self.a['q3'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['q4']=StringVar()
		label=Label(self.ent,text="Quize 4")
		entry=Entry(self.ent,textvariable=self.a['q4'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['t1']=StringVar()
		label=Label(self.ent,text="Test 1")
		entry=Entry(self.ent,textvariable=self.a['t1'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1

		self.a['t2']=StringVar()
		label=Label(self.ent,text="Test 2")
		entry=Entry(self.ent,textvariable=self.a['t2'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1
	
		self.a['ass']=StringVar()
		label=Label(self.ent,text="Assignment")
		entry=Entry(self.ent,textvariable=self.a['ass'])
		label.grid(row=i,column=j)
		entry.grid(row=i,column=j+1)
		i=i+1
		Label(self.ent,text="").grid()
		Label(self.ent,text="").grid()
		Label(self.ent,text="").grid()
		Button(self.ent,text="  Add  ",bg="green",fg="white",command=self.result).grid(row=i+3,column=j+3)
		Button(self.ent, text="  Exit  ", bg="red", fg="white", command=self.resulttable.destroy).grid(row=i + 3, column=j + 5)
		self.resulttable.mainloop()

test()
