

#importing files

from tkinter import *
import json 
   

def checkered(canvas, line_distance,canvas_width,canvas_height):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#86d0db")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#86d0db")

def sortDay(inrList):
    return int(inrList[0][2])

def main():

   # Opening JSON file
   
    with open('data.json') as json_file: 
        data = json.load(json_file)

    gbpList = []
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
            tmp.append(d)
            tmp.append(data['rates'][i]['GBP'])
            gbpList.append(tmp)
            tmp = []
            
    #sorting the inr and gbp lists based on dates in january month       

    inrList.sort(key = sortDay)
    gbpList.sort(key = sortDay)

    master = Tk()
    master.geometry("1400x800") 
    canvas_width = 1100
    canvas_height = 1000
    interval=30
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.place(x=50,y=50)

    checkered(w,30,canvas_width,canvas_height)
    
    w.create_line(60,0,60,750)
    w.create_line(30, 690, 1000, 690)

    i=100
    j=420

    for a in range(32):
        Label(master,text=a).place(x=i,y=750)
        i=i+30

    #labeling y axis for inr
    a=78
    while a<=82:
        Label(master,text=a).place(x=70,y=j-50)
        j=j-30
        a=a+0.5

    #labeling y axis for gbp
    a = 0.86
    j = 750
    while a <= 0.90:
        Label(master,text=a).place(x=40,y=j-50)
        j = j - 30
        a = a + 0.005
    
        
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

    w.create_rectangle(58, 658, 62, 662,outline="#f11", fill="#1f1", width=1)
    x1 = 58
    y1 = 658
    x2 = 62
    y2 = 662

    prev = [60,650]
    for i in gbpList:
        y = i[1]
        x = (int(i[0][2]))
        curr = [60+(30*x),(660-(6000*(y-0.86)))]
        w.create_rectangle((x1+(30*x)),(y1-(6000*(y-0.86))),(x2+(30*x)),(y2-(6000*(y-0.86))),outline="#f11", fill="#1f1", width=1)
        w.create_line(prev[0],prev[1],curr[0],curr[1])
        prev[0] = curr[0]
        prev[1] = curr[1]
    Label(master,text="Graph for INR").place(x=950,y=100)
    Label(master,text="Graph for GBP").place(x=950,y=450)
    Label(master,text="Exchange Rate with respect to EUR").place(x=50,y=50)

    print(inrList)
if __name__=="__main__":
    main()
