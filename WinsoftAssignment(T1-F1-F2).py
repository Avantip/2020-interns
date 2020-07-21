

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
    Label(master,text="Exchange Rate with respect to EUR").place(x=50,y=50)

    #Dynamic Date Selection
    

    start_date=['2019','01','01']
    end_date=['2019','01','31']
    '''
    print("Enter the range of data dynamically")
    print("Enter the start_date:")

    day=input("Enter Day:")
    month=input("Enter Month:")
    year=input("Enter Year:")

    start_date.append(year)
    start_date.append(month)
    start_date.append(day)

    print("Enter the range of data dynamically")
    print("Enter the start_date:")

    day=input("Enter Day:")
    month=input("Enter Month:")
    year=input("Enter Year:")

    end_date.append(year)
    end_date.append(month)
    end_date.append(day)

    '''
    #Currency

    currency_list=[]
    for i in data['rates']['2019-01-30']:
        currency_list.append(i)
    print(currency_list)
    cur=input("Enter currency from the above list:")
    cur.upper()
    
    
    #Creating Canvas to plot graphs
    
    canvas_width = 1000
    canvas_height = 400
    w = Canvas(master, width=canvas_width, height=canvas_height)
    
    w.place(x=100,y=100)

    #drawing grid

    checkered(w,30,canvas_width,canvas_height)

    #drawing X-axis and Y-axis

    w.create_line(60,0,60,390)
    w.create_line(30, 360, 1000, 360)
    w.create_line(60,337,70,340)
    w.create_line(70,340,50,345)
    w.create_line(50,345,65,350)
    w.create_line(65,350,60,355)

    #plotting X-Axis
    
    i=150
    j=470

    for a in range(32):
        Label(master,text=a).place(x=i,y=j)
        i=i+30

    #plotting Y-Axis
        
    a=78
    while a<=82:
        Label(master,text=a).place(x=130,y=j-50)
        j=j-30
        a=a+0.5

    cur_list = []
    tmp_date = []
    d = []
    
    for i in data['rates']:
        d = (i.split('-'))
        if d[1]==start_date[1]:
            if d[2]>=start_date[2] and d[2]<=end_date[2]:
                tmp_date.append(d)
                tmp_date.append(data['rates'][i][cur])
                cur_list.append(tmp_date)
                tmp_date = []
    print(tmp_date)
                
    cur_list.sort(key = sortDay)

    w.create_rectangle(58, 328, 62, 332,outline="#f11", fill="#1f1", width=1)
    x1 = 58
    y1 = 328
    x2 = 62
    y2 = 332

    x = int(cur_list[0][0][2])
    y = cur_list[0][1]
    prev = [(60),(330)]
    for i in cur_list:
        y = i[1]
        x = (int(i[0][2]))
        curr = [60+(30*x),(330-(60*(y-78)))]
        w.create_rectangle((x1+(30*x)),(y1-(60*(y-78))),(x2+(30*x)),(y2-(60*(y-78))),outline="#f11", fill="#1f1", width=1)
        w.create_line(prev[0],prev[1],curr[0],curr[1])
        prev[0] = curr[0]
        prev[1] = curr[1]

if __name__=="__main__":
    main()
