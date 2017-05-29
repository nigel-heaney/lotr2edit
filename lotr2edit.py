#!/usr/bin/env python
# Program to edit LOTR2 Save files
# Nigel Heaney - 20120310

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
        '''initialise with some details which set will use
        '''
        self.gf_gold=100000000
        self.gf_gold_addr=0x14B80
        self.gf_iron=60000
        self.gf_iron_addr=0x14B88
        self.gf_stone=60000
        self.gf_stone_addr=0x14B90
        self.gf_wood=60000
        self.gf_wood_addr=0x14B98
        #Im not interested in all weapons because Knights are the bomb! when cheating :)
        self.gf_armor=9000
        self.gf_armor_addr=0x14BBC
        self.gf_bows=9000
        self.gf_bows_addr=0x14BB8
        self.gf_xbows=9000
        self.gf_xbows_addr=0x14BA8
        self.gf_swords=9000
        self.gf_swords_addr=0x14BB0



    def usage(self):
        be.cprint("green","\nLords of the Realm II - Game File Editor\n")
        be.cprint("grey","----------------------------------------\n\n")
        be.reset_colour()
        print " -h | --help             Show this help"
        print " -l | --list <file>          Display current values of game file"
        print " -e | --edit <file>          Edit current values of game file"
        print " -s | --set <file>           Update game file with defaults"

    def loadvalues(self,filename):
        '''load values from file'''
        if os.path.isfile(filename):
            self.gf=open(filename,"rb")
            #Gold
            self.gf.seek(self.gf_gold_addr)
            self.gf_gold=struct.unpack('I', self.gf.read(4))[0]
            #Resources
            self.gf.seek(self.gf_iron_addr)
            self.gf_iron=struct.unpack('H', self.gf.read(2))[0]
            self.gf.seek(self.gf_stone_addr)
            self.gf_stone=struct.unpack('H', self.gf.read(2))[0]
            self.gf.seek(self.gf_wood_addr)
            self.gf_wood=struct.unpack('H', self.gf.read(2))[0]
            #Weapons
            self.gf.seek(self.gf_armor_addr)
            self.gf_armor=struct.unpack('H', self.gf.read(2))[0]
            self.gf.seek(self.gf_bows_addr)
            self.gf_bows=struct.unpack('H', self.gf.read(2))[0]
            self.gf.seek(self.gf_xbows_addr)
            self.gf_xbows=struct.unpack('H', self.gf.read(2))[0]
            self.gf.seek(self.gf_swords_addr)
            self.gf_swords=struct.unpack('H', self.gf.read(2))[0]
            self.gf.close()
        else:
            be.cprint("red","ERROR: Cannot open game file!")
            sys.exit(1)

    def savevalues(self, filename):
        '''save values from file'''
        if os.path.isfile(filename):
            self.gf=open(filename, 'rb+')
            #Gold
            self.gf.seek(self.gf_gold_addr)
            self.gf.write(struct.pack('I', self.gf_gold))
            #Resources
            self.gf.seek(self.gf_iron_addr)
            self.gf.write(struct.pack('H',self.gf_iron))
            self.gf.seek(self.gf_stone_addr)
            self.gf.write(struct.pack('H',self.gf_stone))
            self.gf.seek(self.gf_wood_addr)
            self.gf.write(struct.pack('H',self.gf_wood))
            #Weapons
            self.gf.seek(self.gf_armor_addr)
            self.gf.write(struct.pack('H',self.gf_armor))
            self.gf.seek(self.gf_bows_addr)
            self.gf.write(struct.pack('H',self.gf_bows))
            self.gf.seek(self.gf_xbows_addr)
            self.gf.write(struct.pack('H',self.gf_xbows))
            self.gf.seek(self.gf_swords_addr)
            self.gf.write(struct.pack('H',self.gf_swords))
            self.gf.close()
        else:
            be.cprint("red","ERROR: Cannot open game file!")
            sys.exit(1)

            
    def listfile(self, filename):
        #validate file exists
        self.loadvalues(filename)
        be.cprint("green", "My Lord, the treasury reports the following:\n\n")
        be.reset_colour()
        print "     Gold: ",
        be.set_colour("yellow")
        print "{0:,}".format(self.gf_gold)
        be.reset_colour()
        print "     Iron: ",
        be.set_colour("brown")
        print "{0:,}".format(self.gf_iron)
        be.reset_colour()
        print "    Stone: ",
        be.set_colour("grey")
        print "{0:,}".format(self.gf_stone)
        be.reset_colour()
        print "     Wood: ",
        be.set_colour("green")
        print "{0:,}".format(self.gf_wood)
        be.reset_colour()
        print "    Armor: ",
        be.set_colour("red")
        print "{0:,}".format(self.gf_armor)
        be.reset_colour()
        print "     Bows: ",
        be.set_colour("red")
        print "{0:,}".format(self.gf_bows)
        be.reset_colour()
        print "Crossbows: ",
        be.set_colour("red")
        print "{0:,}".format(self.gf_xbows)
        be.reset_colour()
        print "   Swords: ",
        be.set_colour("red")
        print "{0:,}".format(self.gf_swords)
        be.reset_colour()
        
    def editfile(self, filename):
        self.loadvalues(filename)
        be.cprint("green", "My Lord, Please supply your desired values:\n\n")
        be.reset_colour()
        #Gold
        print "{0:11}{1:10}({2:,})".format("     Gold: ", " ", self.gf_gold),
        print "\r     Gold: ".format(self.gf_gold),
        be.set_colour("yellow")
        self.gf_gold=int(raw_input())
        be.reset_colour()

        #Resources
        print "{0:11}{1:10}({2:,}/65535)".format("     Iron: ", " ", self.gf_iron),
        print "\r     Iron: ".format(self.gf_iron),
        be.set_colour("brown")
        self.gf_iron=int(raw_input(''))
        be.reset_colour()

        print "{0:11}{1:10}({2:,}/65535)".format("    Stone: ", " ", self.gf_stone),
        print "\r    Stone: ".format(self.gf_stone),
        be.set_colour("grey")
        self.gf_stone=int(raw_input(""))
        be.reset_colour()

        print "{0:11}{1:10}({2:,}/65535)".format("     Wood: ", " ", self.gf_wood),
        print "\r     Wood: ".format(self.gf_wood),
        be.set_colour("green")
        self.gf_wood=int(raw_input(''))
        be.reset_colour()

        #Weapons
        print "{0:11}{1:10}({2:,}/65535)".format("    Armor: ", " ", self.gf_armor),
        print "\r    Armor: ".format(self.gf_armor),
        be.set_colour("red")
        self.gf_armor=int(raw_input(''))
        be.reset_colour()

        print "{0:11}{1:10}({2:,}/65535)".format("     Bows: ", " ", self.gf_bows),
        print "\r     Bows: ".format(self.gf_bows),
        be.set_colour("red")
        self.gf_bows=int(raw_input(''))
        be.reset_colour()

        print "{0:11}{1:10}({2:,}/65535)".format("Crossbows: ", " ", self.gf_xbows),
        print "\rCrossbows: ".format(self.gf_xbows),
        be.set_colour("red")
        self.gf_xbows=int(raw_input(''))
        be.reset_colour()

        print "{0:11}{1:10}({2:,}/65535)".format("   Swords: ", " ", self.gf_bows),
        print "\r   Swords: ".format(self.gf_swords),
        be.set_colour("red")
        self.gf_swords=int(raw_input(''))
        be.reset_colour()
        
        self.savevalues(filename)


    
#Main
gamefile=lotr2edit()
opts, args = getopt.getopt(sys.argv[1:], "hles", ["help", "list","edit","set"])
if debug: print "Options:", opts
if debug: print "Args:",args
for o,a in opts:
    if debug: print "O:", o
    if o in ("-h", "--help"):
        gamefile.usage()
        sys.exit()
    elif o in ("-l", "--list"):
        if len(args) > 0: 
            #list
            gamefile.listfile(args[0])
            sys.exit()
    elif o in ("-e", "--edit"):
        if len(args) > 0: 
            #edit
            gamefile.editfile(args[0])
            sys.exit()
    elif o in ("-s", "--set"):
        if len(args) > 0: 
            #Set good default values into game file
            gamefile.savevalues(args[0])
            be.cprint("green", "T'is done my lord...\n")
            be.reset_colour()
            sys.exit()
    else:
        #assume garbage so exit
        be.cprint("red", "ERROR: Unknown, please read the help page")
        be.reset_colour()
        
