from tkinter import *
from tkinter.font import Font


def printInfo():
    Selection = wellLocations.curselection()[0]

    locationInfoVar.set(location_list[Selection])
    wellInfoVar.set(type_list[Selection])
    depthVar.set(depth_list[Selection])
    gpmVar.set(gpm_list[Selection])
    soils = soil_list[Selection]

    
    listboxList = [clayVar,gravelVar, loamVar, limestoneVar, sandVar, shaleVar]
    count = 0

    for set0 in range(0,6):
        listboxList[set0].set(0)
            
    for index in soils:

        if index == 'T':
            cool = listboxList[count].set(1)
        count+= 1

    depthColour("remove")
    gpmColour("remove")
def deleteWell():
    
   listIndex = wellLocations.curselection()[0]

   location_list.pop(listIndex)
   type_list.pop(listIndex)
   depth_list.pop(listIndex)
   gpm_list.pop(listIndex)
   soil_list.pop(listIndex)
   location_var.set(location_list)
   if listIndex - 1 >= 0:
       listIndex -= 1
       
   locationInfoVar.set(location_list[listIndex])
   wellInfoVar.set(type_list[listIndex])
   depthVar.set(depth_list[listIndex])
   gpmVar.set(gpm_list[listIndex])
   soils = soil_list[listIndex]
   location_var.set(location_list)
       
   listboxList = [clayVar,gravelVar, loamVar, limestoneVar, sandVar, shaleVar]
   count = 0

   for set0 in range(0,6):
       listboxList[set0].set(0)

   for index in soils:
       if index == 'T':
           cool = listboxList[count].set(1)
           count+= 1
       depthColour("remove")
       gpmColour("remove")
       
   
def clearInfo():
    if locationInfoVar.get() == location_list[wellLocations.curselection()[0]]:
    
        Selection = wellLocations.curselection()[0]

        locationInfoVar.set(location_list[Selection])
        wellInfoVar.set(type_list[Selection])
        depthVar.set(depth_list[Selection])
        gpmVar.set(gpm_list[Selection])
        soils = soil_list[Selection]

    
        listboxList = [clayVar,gravelVar, loamVar, limestoneVar, sandVar, shaleVar]
        count = 0

        for set0 in range(0,6):
            listboxList[set0].set(0)
            
        for index in soils:
            if index == 'T':
                cool = listboxList[count].set(1)
            count+= 1
        depthColour("remove")
        gpmColour("remove")
def addWell():
    #Getting Code from Soil Choices
    choiceSoil = [0, 1, 2, 3, 4, 5]
    listCode = ['F','F','F','F','F','F']
    soilAdd = soilAddListbox.curselection()
    trueLong = len(soilAdd)
    for i in soilAdd:
        listCode[i] = 'T'

    newCode = ""
    for i in listCode:
        newCode += i

    #Updating Lists with user choices
    locationChoice = locationAdd_var.get()


    if locationChoice not in location_list:
        location_list.append(locationChoice)
        type_list.append(wellAdd_var.get())
        depth_list.append(depthAddVar.get())
        gpm_list.append(gpmAddVar.get())
        soil_list.append(newCode)


    location_var.set(location_list)


    

def depthColour(remove):
    if depthVar.get() <= 50:
        depthScale.config(bg="#71bcf5")
    elif depthVar.get() <= 100:
        depthScale.config(bg="#00fa4f")
    elif depthVar.get() <= 150:
        depthScale.config(bg="#630ac9")
    elif depthVar.get() <= 200:
        depthScale.config(bg="#ffe908")
    elif depthVar.get() <= 250:
        depthScale.config(bg="#f5a505")
    elif depthVar.get() <= 300:
        depthScale.config(bg="#f50d05")


def gpmColour(remove):
    if gpmVar.get() <= 100:
        gpmScale.config(bg="#71bcf5")
    elif gpmVar.get() <= 200:
        gpmScale.config(bg="#00fa4f")
    elif gpmVar.get() <= 300:
        gpmScale.config(bg="#630ac9")
    elif gpmVar.get() <= 400:
        gpmScale.config(bg="#ffe908")
    elif gpmVar.get() <= 500:
        gpmScale.config(bg="#f5a505")
    elif gpmVar.get() <= 600:
        gpmScale.config(bg="#f50d05")
#MAIN

global location_list, type_list, depth_list, gpm_list, soil_list
location_list = ['GUELPH CITY', 'GUELPH DIV E01 005', 'SCUGOG 08 022', 'TORONTO 121 Industry', 'Halton NS01 005', 'SOUTH DUMFRIES 02 017', 'BINBROOK BL303 004']
type_list = ['Municipal', 'Municipal', 'Domestic', 'Industrial', 'Domestic', 'Domestic', 'Domestic']
individualtype_list = ['Domestic', 'Agricultural', 'Industrial', 'Commercial', 'Municipal', 'Dewatering']
depth_list = [241, 265, 224, 11, 52, 152, 80]
gpm_list = [541, 151, 10, 0, 15, 20, 3]
#soil legend: Clay, Gravel, Loam, Limestone, Sand, Shale
soilType_list = ["Clay", "Gravel", "Loam", "Limestone", "Sand", "Shale"]
soil_list = ['FTTFTT', 'TTTTFF', 'TTTFTF', 'FFTFTF', 'TTFFFF', 'TFTFFF', 'TFFTFF']


#Create widgets
root = Tk()
mainframe = Frame(root)




#Create custom frames
customFrame = LabelFrame(mainframe, text="Customize",font=("Moonbeam"))
infoFrame = LabelFrame(mainframe, text="Information",font=("Moonbeam"))
addFrame = LabelFrame(mainframe, text="Add", height=5,font=("Moonbeam"))
introFrame = LabelFrame(mainframe)
gpmAddFrame = LabelFrame(addFrame, text="GPM",font=("Moonbeam"))
depthAddFrame = LabelFrame(addFrame, text="Depth",font=("Moonbeam"))



intro= Label(introFrame, text="Ontario Water Well Supply Information",font=("Moonbeam",30))


#Customize box widgets
location_var = StringVar()
location_var.set(location_list)
wellLocations = Listbox(customFrame, listvariable= location_var, selectmode=SINGLE)

printButton = Button(customFrame,text="Print", command= printInfo,height=2,width=6)
deleteButton = Button(customFrame,text="Delete", command= deleteWell,height=2,width=6)
clearButton = Button(customFrame,text="Clear", command= clearInfo,height=2,width=6)

#Information box widgets

entryFrame = Frame(infoFrame)

locationInfoVar = StringVar()
locationInfoVar.set("Well Location")
locationEntry = Entry(entryFrame, textvariable= locationInfoVar,width = 40)

wellInfoVar = StringVar()
wellInfoVar.set("Well Type")
wellEntry = Entry(entryFrame, textvariable= wellInfoVar, width=40)

depthFrame = LabelFrame(infoFrame, text="Depth",font=("Moonbeam", 10))
gpmFrame = LabelFrame(infoFrame, text="GPM",font=("Moonbeam", 10))
soilFrame = LabelFrame(infoFrame, text="Soil Type",font=("Moonbeam",10))

        
depthVar = IntVar()
depthEntry = Entry(depthFrame, textvariable= str(depthVar))
depthEntry.bind("<Enter>", depthColour)

depthScale = Scale(depthFrame, from_=0, to=300, variable=depthVar,width=100,length=160,showvalue=0, command = depthColour)

gpmVar = IntVar()
gpmEntry = Entry(gpmFrame, textvariable= str(gpmVar))
gpmEntry.bind("<Enter>", gpmColour)

gpmScale = Scale(gpmFrame, from_=0, to=600, variable=gpmVar, width=100,length=160,showvalue=0, command = gpmColour)




clayVar = StringVar()
clayCheck = Checkbutton(soilFrame, text = "Clay", variable = clayVar, onvalue = 1, offvalue = 0)

gravelVar = StringVar()
gravelCheck = Checkbutton(soilFrame, text = "Gravel", variable = gravelVar, onvalue = 1, offvalue = 0)

loamVar = StringVar()
loamCheck = Checkbutton(soilFrame, text = "Loam", variable = loamVar, onvalue = 1, offvalue = 0)

limestoneVar = StringVar()
limestoneCheck = Checkbutton(soilFrame, text = "Limestone", variable = limestoneVar, onvalue = 1, offvalue = 0)

sandVar = StringVar()
sandCheck = Checkbutton(soilFrame, text = "Sand", variable = sandVar, onvalue = 1, offvalue = 0)

shaleVar = StringVar()
shaleCheck = Checkbutton(soilFrame, text = "Shale", variable = shaleVar, onvalue = 1, offvalue = 0)



#Add box widgets
addButton = Button(addFrame,text="Add", command=addWell,width=13, height= 5)

locationAdd_var = StringVar()
locationAdd_var.set("Location")
locationAddEntry = Entry(addFrame,textvariable= locationAdd_var, width=18)


wellAdd_var = StringVar()
wellAddSpinbox = Spinbox(addFrame, textvariable=wellAdd_var, values=individualtype_list, width= 16)

depthAddVar = IntVar()
depthAddScale = Scale(depthAddFrame, from_=0, to=300, variable=depthAddVar,width=20,length=280,orient=HORIZONTAL)


gpmAddVar = IntVar()
gpmAddScale = Scale(gpmAddFrame, from_=0, to=600, variable=gpmAddVar, width=20,length=280, orient=HORIZONTAL)
                    
soilAddVar = StringVar()
soilAddVar.set(soilType_list)
soilAddListbox = Listbox(addFrame, listvariable= soilAddVar, selectmode=MULTIPLE, height=8, width = 25)



#colouring
root.config(bg = "#F0F8FF")
mainframe.config(bg = "#F0F8FF")


customFrame.config(bg = "#F0F8FF")
intro.config(bg = "#F0F8FF")
infoFrame.config(bg = "#F0F8FF")
addFrame.config(bg = "#F0F8FF")
introFrame.config(bg = "#F0F8FF" )
gpmAddFrame.config(bg = "#F0F8FF")
depthAddFrame.config(bg = "#F0F8FF")
depthFrame.config(bg = "#F0F8FF")
gpmFrame.config(bg = "#F0F8FF")
soilFrame.config(bg = "#F0F8FF")
entryFrame.config(bg = "#F0F8FF")
gpmAddScale.config(bg = "#F0F8FF")
gpmScale.config(bg = "#F0F8FF")
depthAddScale.config(bg = "#F0F8FF")
depthScale.config(bg = "#F0F8FF", fg = "#F0F8FF")
clayCheck.config(bg = "#F0F8FF")
gravelCheck.config(bg = "#F0F8FF")
loamCheck.config(bg = "#F0F8FF")
limestoneCheck.config(bg = "#F0F8FF")
sandCheck.config(bg = "#F0F8FF")
shaleCheck.config(bg = "#F0F8FF")
depthEntry.config(bg = "#F0F8FF")
gpmEntry.config(bg = "#F0F8FF")

printButton.config(bg = "#DBECF4")
deleteButton.config(bg = "#DBECF4")
clearButton.config(bg = "#DBECF4")
addButton.config(bg = "#DBECF4")
soilAddListbox.config(bg = "#DBECF4")
wellAddSpinbox.config(bg = "#DBECF4")

wellLocations.config(bg = "#DBECF4")
locationAddEntry.config(bg = "#DBECF4")
wellEntry.config(bg = "#DBECF4")
locationEntry.config(bg = "#DBECF4")


#Grid widgets
mainframe.grid(padx=100, pady=60)
introFrame.grid(row=1,column=1,columnspan=2,sticky=EW)
customFrame.grid(row=2,column=1,sticky=W)
infoFrame.grid(row=2, column=2, sticky=NS, padx = 10)
addFrame.grid(row=3,column=1, columnspan=2, sticky=EW)

intro.grid(row=1,column=1,padx = 120)

#Customize Gridding
wellLocations.grid(row=1,column=1, columnspan=3,padx=10,pady=6, ipadx=15)
printButton.grid(row=2,column=1,pady=10)
deleteButton.grid(row=2,column=2, pady= 7)
clearButton.grid(row=2,column=3,pady=7)



#Information Gridding
entryFrame.grid(row=1,column=1, columnspan = 3, pady = 5)
locationEntry.grid(row=1,column=1, padx = 15)
wellEntry.grid(row=1, column=2)

depthFrame.grid(row=2, column=1, padx = 55)
depthEntry.grid(row=1,column=1)
depthScale.grid(row=2, column=1,sticky=EW, padx = 15)

gpmFrame.grid(row=2,column=2)
gpmEntry.grid(row=1,column=1)
gpmScale.grid(row=2, column=1, sticky=EW, padx = 15)

soilFrame.grid(row=2,column=3, ipadx = 15, ipady = 18, padx = 55, sticky = E)


clayCheck.grid(row=1,column=1, sticky = W)
gravelCheck.grid(row=2,column=1, sticky = W)
loamCheck.grid(row=3,column=1, sticky = W)
limestoneCheck.grid(row=4,column=1, sticky = W)
sandCheck.grid(row=5,column=1, sticky = W)
shaleCheck.grid(row=6,column=1, sticky = W)



#Adding Gridding
addButton.grid(row=1,column=1,rowspan=2, padx = 10, pady = 8)
locationAddEntry.grid(row=1,column=2, padx = 15, sticky = S, pady = 20 )
wellAddSpinbox.grid(row=2,column=2, padx = 15, sticky = N, pady = 25)

gpmAddFrame.grid(row=1,column=3, ipadx = 10, sticky= S, pady=6)
depthAddFrame.grid(row=2,column=3, ipadx = 10,pady = 6)

gpmAddScale.grid(row=1,column=2)

depthAddScale.grid(row=1,column=2)

soilAddListbox.grid(row=1,column=4,rowspan=2, pady=18, padx=40, sticky=S)


#for some students
root.mainloop()
