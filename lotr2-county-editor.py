#!/usr/bin/env python
# Program to edit county information for LOTR2 Save files
# Nigel Heaney - 20150118

import sys
import os
import getopt
if sys.platform == "linux" or sys.platform == "linux2":
    import be
elif sys.platform == "win32":
    import be_win as be
import struct
debug=0

class lotr2edit():
    def __init__(self):
        '''initialise class with defaults/basic information
        '''
        self.gf=""
        self.county=0
        self.counties=0
        self.county_ruler=0
        self.county_color=0
        self.county_health=0
        self.county_happiness=0
        self.county_end=0
        self.county_population=0
        self.county_tax=0
        self.county_grain=0
        self.county_cattle=0

        self.colors=["lgrey","Red","Yellow","Grey","Purple","Blue","White"]
        self.health=["Null","Plagued","Weak","Good","Perfect"]
        self.healthc=["Null","Red","yellow","green","lgreen"]
        self.rulers=["No Ruler", "You M'Lord", "The Bishop", "The Baron", "The Countess", "The Knight"]
        self.start=0x15449


    def usage(self):
        be.cprint("green","\nLords of the Realm II - County Game File Editor\n")
        be.cprint("grey","-----------------------------------------------\n\n")
        be.reset_colour()
        print " -h | --help                 Show this help"
        print " -f | --file <file>          Display current values of game file"

    def loadCounty(self,cnum):
        '''load values from file'''
        self.gf.seek(self.start + (768 * cnum) + 4)
        self.county_ruler=struct.unpack('B', self.gf.read(1))[0]
        self.gf.seek(self.start + (768 * cnum) + 6)
        self.county_color=struct.unpack('B', self.gf.read(1))[0]
        self.gf.seek(self.start + (768 * cnum) + 8)
        self.county_health=struct.unpack('B', self.gf.read(1))[0]
        self.gf.seek(self.start + (768 * cnum) + 11)
        self.county_happiness=struct.unpack('B', self.gf.read(1))[0]
        self.gf.seek(self.start + (768 * cnum) + 35)
        self.county_population=struct.unpack('H', self.gf.read(2))[0]
        self.gf.seek(self.start + (768 * cnum) + 184)
        self.county_tax=struct.unpack('B', self.gf.read(1))[0]
        self.gf.seek(self.start + (768 * cnum) + 547)
        self.county_grain=struct.unpack('H', self.gf.read(2))[0]
        self.gf.seek(self.start + (768 * cnum) + 591)
        self.county_cattle=struct.unpack('H', self.gf.read(2))[0]

    def saveCounty(self, cnum):
        '''save county to file'''
        self.gf.seek(self.start + (768 * cnum) + 4)
        self.gf.write(struct.pack('B', self.county_ruler))

        self.gf.seek(self.start + (768 * cnum) + 6)
        self.gf.write(struct.pack('B', self.county_color))

        self.gf.seek(self.start + (768 * cnum) + 8)
        self.gf.write(struct.pack('B', self.county_health))

        self.gf.seek(self.start + (768 * cnum) + 11)
        self.gf.write(struct.pack('B', self.county_happiness))

        self.gf.seek(self.start + (768 * cnum) + 35)
        self.gf.write(struct.pack('H', self.county_population))

        self.gf.seek(self.start + (768 * cnum) + 547)
        self.gf.write(struct.pack('H', self.county_grain))

        self.gf.seek(self.start + (768 * cnum) + 591)
        self.gf.write(struct.pack('H', self.county_cattle))

            
    def listCounties(self):
        count=1
        while True:
            be.cprint("green", "\nMy Lord, county {0}/{1} reports the following:\n\n".format(count, self.counties))
            be.reset_colour()
            self.loadCounty(count-1)
            print "Ruler: ",
            be.cprint(self.colors[self.county_color], "{0:}\n".format(self.rulers[self.county_ruler]))
            be.reset_colour()
            print "Tax: ",
            be.cprint("blue", "{0:}\n".format(self.county_tax))
            be.reset_colour()      
            print "Happiness: ",
            be.cprint("red", "{0:}\n".format(self.county_happiness))
            be.reset_colour()
            print "Health: ",
            be.cprint(self.healthc[self.county_health], "{0:}\n".format(self.health[self.county_health]))
            be.reset_colour()
            print "Population: ",
            be.cprint("white", "{0:}\n".format(self.county_population))
            be.reset_colour()            
            print "Grain: ",
            be.cprint("yellow", "{0:}\n".format(self.county_grain))
            be.reset_colour()      
            print "Cattle: ",
            be.cprint("white", "{0:}\n".format(self.county_cattle))
            be.reset_colour()

            be.cprint("grey", "(P)revious - (E)dit - (Q)uit - (N)ext: ")
            temp=raw_input("")
            if temp.lower() == 'p':
                count-=1
                if count < 1: count=1
            if temp.lower() == 'n':
                count+=1
                if count > self.counties: count=self.counties
            if temp.lower() == 'q':
                be.cprint("green", "\nBye!\n")
                sys.exit(0)
            if temp.lower() == 'e':
                self.editCounty(count)

    def editCounty(self, cnum):
        be.cprint("green", "My Lord, What do you desire for county {0}/{1}:\n\n".format(cnum, self.counties))
        be.reset_colour()
        while True:
            print "Ruler 0=None, 1=You, 2=Bishop, 3=Baron, 4=Countess,5=Knight: ",
            be.set_colour("blue")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 6: 
                self.county_ruler=temp
                break

        while True:
            print "Color (0=None, 1=Red, 2=Yellow, 3=Grey, 4=Pink, 5=Blue, 6=Black): ",
            be.set_colour("blue")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 7: 
                self.county_color=temp
                break

        while True:
            print "Happiness 0-100: ",
            be.set_colour("blue")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 101: 
                self.county_happiness=temp
                break
        while True:
            print "Health (1=Plagued, 2=Weak, 3=Normal, 4=Perfect): ",
            be.set_colour("green")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 6: 
                self.county_health=temp
                break
        while True:
            print "Population 0-65535: ",
            be.set_colour("blue")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 65535: 
                self.county_population=temp
                break
        while True:
            print "Grain (0-65535): ",
            be.set_colour("yellow")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 65535: 
                self.county_grain=temp
                break
        while True:
            print "Cattle (0-65535): ",
            be.set_colour("white")
            temp=int(raw_input())
            be.reset_colour()
            if temp > -1 and temp < 65535: 
                self.county_cattle=temp
                break

        self.saveCounty(cnum-1)

    def countCounties(self):
        '''Count the number of counties in gamefile.'''
        count=0
        temp=0
        while True:
            self.gf.seek(self.start + (768 * count) + 16)
            temp=struct.unpack('B', self.gf.read(1))[0]
            if temp != 248:
                count+=1
            else:
                return count

    
#Main
gamefile=lotr2edit()
opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "file"])
if debug: print "Options:", opts
if debug: print "Args:",args
for o,a in opts:
    if debug: print "O:", o
    if o in ("-h", "--help"):
        gamefile.usage()
        sys.exit()
    elif o in ("-f", "--file"):
        if len(args) > 0: 
            if os.path.isfile(args[0]):
                gamefile.gf=open(args[0],"r+b")
            gamefile.counties=gamefile.countCounties()
            gamefile.listCounties()
            sys.exit()
    else:
        be.cprint("red", "ERROR: Unknown, please read the help page")
        be.reset_colour()
        
