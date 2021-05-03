#This implementation is without scklearn to get deep concept with Graphical interface
from tkinter import *
import pandas as pd
dt=pd.read_csv('dataset.csv')

def m_estimate(m, b, f):
    p = 1/dt[f].nunique()
    return (m*p)/(b+m)
def find_likelihood_probs(x,y,z,o):
	maska=dt['Outcome']==o
	acount=len(dt.where(maska).dropna())
	mask=(dt['Outcome']==o)&(dt['Featurex']==x)
	x_o=len(dt.where(mask).dropna())/acount
	mask=(dt['Outcome']==o)&(dt['Featurey']==y)
	y_o=len(dt.where(mask).dropna())/acount
	mask=(dt['Outcome']==o)&(dt['Featurez']==z)
	z_o=len(dt.where(mask).dropna())/acount
	p_o=len(dt.where(mask).dropna())/len(dt)

	if x_o==0:
		x_o=m_estimate(5,p_o,'Featurex')

	if y_o==0:
		y_o=m_estimate(5,p_o,'Featurey')

	if z_o==0:
		z_o=m_estimate(5,p_o,'Featurez')
	return p_o*z_o*y_o*x_o



		
def prediction(lst):
	if lst[0]>lst[1] and lst[0]>lst[2]:
		return 'A'
	elif lst[1]>lst[2] and lst[1]>lst[0]:
		return 'B'
	else:
		return 'C'

def findprobs(x,y,z):
	tot=x+y+z
	x=x/tot
	y=y/tot
	z=z/tot
	return [x,y,z]
def naivebayes(x,y,z):
	l_a=find_likelihood_probs(x,y,z,'A')
	l_b=find_likelihood_probs(x,y,z,'B')
	l_c=find_likelihood_probs(x,y,z,'C')
	probs=findprobs(l_a,l_b,l_c)
	lk_probs="L_probs{A="+str(round(l_a,5))+",B="+str(round(l_b,5))+",C="+str(round(l_c,5))+"}"
	pred="prediction::class "+prediction([l_a,l_b,l_c])
	
	probss="Probs={A="+str(round(probs[0],5))+",B="+str(round(probs[1],5))+",C="+str(round(probs[2],5))+"}"

	return [lk_probs,pred,probss]

def click():
	fx=int(xentry.get())
	fy=int(yentry.get())
	fz=int(zentry.get())
	output.delete(0.0,END)
	output1.delete(0.0,END)
	output2.delete(0.0,END)
	result=naivebayes(fx,fy,fz)
	out=result[0]
	output.insert(END,out)
	out1=result[1]
	output1.insert(END,out1)
	out2=result[2]
	output2.insert(END,out2)
	








window=Tk()
window.title("Naive Bayse Assignment 1")
window.configure(background="black")
pic=PhotoImage(file="Naive.png")
Label(window,image=pic,bg="black").grid(row=0,column=3,sticky=W)
Label(window,text="Enter Feature x:",bg="black",fg="red",font="none 12 bold").grid(row=1,column=1,sticky=W)
xentry=Entry(window,width=15,bg="grey")
xentry.grid(row=2,column=1)
Label(window,text="Enter Feature y:",bg="black",fg="red",font="none 12 bold").grid(row=3,column=1,sticky=W)
yentry=Entry(window,width=15,bg="grey")
yentry.grid(row=4,column=1)
Label(window,text="Enter Feature z:",bg="black",fg="red",font="none 12 bold").grid(row=5,column=1,sticky=W)
zentry=Entry(window,width=15,bg="grey")
zentry.grid(row=6,column=1,pady=2)
Button(window,text="Enter",width=6,command=click).grid(row=7,column=1,sticky=W)
output=Text(window,width=50,height=1,wrap=WORD,background="grey")
output.grid(row=5,column=3)
output1=Text(window,width=50,height=1,wrap=WORD,background="grey")
output1.grid(row=6,column=3)
output2=Text(window,width=50,height=1,wrap=WORD,background="grey")
output2.grid(row=7,column=3)

window.mainloop()
