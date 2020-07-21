

#tkinter trial

from tkinter import *
import json

def sortDay(inrList):
    return int(inrList[0][2])

def checkered(canvas, line_distance,canvas_width,canvas_height):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#86d0db")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#86d0db")


def main():
    with open('data.json') as json_file: 
        data = json.load(json_file)
        
    master = Tk()
    master.geometry("1400x800")

    #Dynamic Date Selection

    label_start_date=Label(master,text="From")
    label_start_date.place(x=200,y=50)

    label1=Label(master,text="Day")
    label2=Label(master,text="Month")
    label3=Label(master,text="Year")

    label1.place(x=300,y=30)
    label2.place(x=400,y=30)
    label3.place(x=500,y=30)

    listbox1=Listbox(master,height=1, width=10)
    listbox2=Listbox(master,height=1, width=10)
    listbox3=Listbox(master,height=1, width=10)
    
    listbox1.place(x=300,y=50)
    listbox2.place(x=400,y=50)
    listbox3.place(x=500,y=50)
    
    for i in range(1,32,1):
        listbox1.insert(i,i)

    for i in range(1,13,1):
        listbox2.insert(i,i)
    
    listbox3.insert(1,"2018")
    listbox3.insert(2,"2019")

    label_end_date=Label(master,text="To")
    label_end_date.place(x=200,y=100)

    listbox4=Listbox(master,height=1, width=10)
    listbox5=Listbox(master,height=1, width=10)
    listbox6=Listbox(master,height=1, width=10)
    
    listbox4.place(x=300,y=100)
    listbox5.place(x=400,y=100)
    listbox6.place(x=500,y=100)
    
    for i in range(1,32,1):
        listbox4.insert(i,i)

    for i in range(1,13,1):
        listbox5.insert(i,i)
    
    listbox6.insert(1,"2018")
    listbox6.insert(2,"2019")

    #Currency

    currency_list=[]
    for i in data['rates']['2019-01-30']:
        currency_list.append(i)
        
    label4=Label(master,text="Currency")
    label4.place(x=200,y=150)    
    listbox7=Listbox(master,height=1, width=10)
    listbox7.place(x=300,y=150)

    #Creating Canvas to plot graphs
    
    canvas_width = 1100
    canvas_height = 400
    w = Canvas(master, width=canvas_width, height=canvas_height)
    
    w.place(x=200,y=200)

    #drawing grid

    checkered(w,30,canvas_width,canvas_height)

    #drawing X-axis and Y-axis

    w.create_line(60,0,60,390)
    w.create_line(30, 360, 1000, 360)

    #plotting X-Axis
    
    i=250
    j=570

    for a in range(32):
        Label(master,text=a).place(x=i,y=j)
        i=i+30

    #plotting Y-Axis
        
    a=78
    while a<=82:
        Label(master,text=a).place(x=220,y=j-50)
        j=j-30
        a=a+0.5

    inrList = []
    tmp = []
    d = []
    
    for i in data['rates']:
        d = (i.split('-'))
        if d[1] == '01':
            tmp.append(d)
            tmp.append(data['rates'][i]['INR'])
            inrList.append(tmp)
            tmp = []
    inrList.sort(key = sortDay)

    w.create_rectangle(58, 328, 62, 332,outline="#f11", fill="#1f1", width=1)
    x1 = 58
    y1 = 328
    x2 = 62
    y2 = 332

    x = int(inrList[0][0][2])
    y = inrList[0][1]
    prev = [(60),(330)]
    for i in inrList:
        y = i[1]
        x = (int(i[0][2]))
        curr = [60+(30*x),(330-(60*(y-78)))]
        w.create_rectangle((x1+(30*x)),(y1-(60*(y-78))),(x2+(30*x)),(y2-(60*(y-78))),outline="#f11", fill="#1f1", width=1)
        w.create_line(prev[0],prev[1],curr[0],curr[1])
        prev[0] = curr[0]
        prev[1] = curr[1]

if __name__=="__main__":
    main()
