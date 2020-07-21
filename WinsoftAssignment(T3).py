#This is the solution for t3 of assignment

#tkinter trial
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

    with open('latest-rates.json') as json_file: 
        latest_data = json.load(json_file)

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
    canvas_height = 1500
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.place(x=20,y=20)

    checkered(w,30,canvas_width,canvas_height)
    
    w.create_line(60,0,60,750)
    w.create_line(30, 720, 1000, 720)

    i=70
    j=300

    for a in range(32):
        Label(master,text=a).place(x=i,y=750)
        i=i+30

    #labeling y axis for inr
    a=75
    while a<=82:
        Label(master,text=a).place(x=40,y=j-50)
        j=j-30
        a=a+1

    #labeling y axis for gbp
    a = 0.79
    j = 750
    while a <= 0.91:
        Label(master,text=round(a,2)).place(x=40,y=j-50)
        j = j - 30
        a = a + 0.01
        


    latest_inr = latest_data['rates']['INR']
    latest_gbp = latest_data['rates']['GBP']
    
        
    #w.create_rectangle(58, 238, 62, 242,outline="#f11", fill="#1f1", width=1)
    x1 = 58
    y1 = 238
    x2 = 62
    y2 = 242

    print("Printing gbp list: ")
    print(gbpList)
    print("Printing inr list: ")
    print(inrList)
    #print("printing all i's:")
    x = int(inrList[0][0][2])
    y = inrList[0][1]
    prev = [(60),(240)]
    for i in inrList:
        #print(i)
        y = i[1]
        x = (int(i[0][2]))
        curr = [60+(30*x),(240-(30*(y-75)))]
        w.create_rectangle((x1+(30*x)),(y1-(30*(y-75))),(x2+(30*x)),(y2-(30*(y-75))),outline="#f11", fill="#f11", width=1)
        w.create_line(prev[0],prev[1],curr[0],curr[1], fill = "green", width = 2)
        prev[0] = curr[0]
        prev[1] = curr[1]

    w.create_rectangle(58, 688, 62, 692,outline="#f11", fill="#1f1", width=1)
    x1 = 58
    y1 = 688
    x2 = 62
    y2 = 692

    prev = [60,690]
    for i in gbpList:
        print(i)
        y = i[1]
        x = (int(i[0][2]))
        curr = [60+(30*x),(690-(3000*(y-0.79)))]
        w.create_rectangle((x1+(30*x)),(y1-(3000*(y-0.79))),(x2+(30*x)),(y2-(3000*(y-0.79))),outline="#f11", fill="#f11", width=1)
        w.create_line(prev[0],prev[1],curr[0],curr[1], fill = "green", width = 2)
        prev[0] = curr[0]
        prev[1] = curr[1]

    #plotting the line for latest values of inr
    x1 = 58
    y1 = 238
    x2 = 62
    y2 = 242
    x = 60
    y = latest_inr
    print(y)
    w.create_rectangle(58, 238-(30*(y-75)), 62, 242-(30*(y-75)),outline="#f11", fill="#1f1", width=1)
    w.create_line(60,240-(30*(y-75)),60*31,240-(30*(y-75)),fill = "#f11", width = 2)

    #plotting the line for latest values of gbp
    x1 = 58
    y1 = 658
    x2 = 62
    y2 = 662
    x = 60
    y = latest_gbp
    print(y)
    w.create_rectangle(58, 688-(3000*(y-0.79)), 62, 692-(3000*(y-0.79)),outline="#f11", fill="#1f1", width=1)
    w.create_line(60,690-(3000*(y-0.79)),60*31,690-(3000*(y-0.79)),fill = "#f11", width = 2)


    

    

if __name__=="__main__":
    main()
