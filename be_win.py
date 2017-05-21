#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  be - Batch colour Enhancer for windows
#  
#  Copyright 2012 Nigel Heaney <nigel.heaney__A_t__gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
Batch colour Enhancer

A module that will set the colour of text in DOS console terminals.  
"""
  
import ctypes,sys
__version__='v0.1'
#define Colour constants
_colour_={}
_colour_['BLACK']     = 0
_colour_['GREY']      = 8
_colour_['BLUE']      = 1
_colour_['LBLUE']     = 9
_colour_['GREEN']     = 2
_colour_['LGREEN']    = 10
_colour_['CYAN']      = 3
_colour_['LCYAN']     = 11
_colour_['RED']       = 4
_colour_['LRED']      = 12
_colour_['PURPLE']    = 5
_colour_['LPURPLE']   = 13
_colour_['BROWN']     = 6
_colour_['YELLOW']    = 14
_colour_['LGREY']     = 7
_colour_['WHITE']     = 15
_colour_['RESET']     = 15

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def cprint(colour, printString):
	""" This function will print a string in the selected colour. usage:

		import be-win
		cprint("Green", "this is some text in green")
	"""
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, _colour_[colour.upper()])
	sys.stdout.write(printString)
	reset_colour
	return None

def set_colour(colour):
	""" Use this function to set both foreground and background colours - although seperately to simplify
		usage:
			import be-win
			set_colour('red')
			set_colour('bg_blue')
			print "print some red text on a blue background ... yuck!"
	"""
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, _colour_[colour.upper()])
	return None

def reset_colour():
	""" Use this function to reset colours back to default ... for your terminal """
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, _colour_['RESET'])
	return None

def main():
	cprint("Green","Batch Colour Enhancer " + __version__ + "\n")
	cprint("lgreen","=========================\n")
	cprint("grey", "Colour Codes Available:\n")
	for cnames in _colour_:
		sys.stdout.write("   ")
		set_colour(cnames)
		print cnames.upper()
		set_colour('RESET')
	print "\n"
	###set_colour('BG_BLUE')
	set_colour('white')
	print "***************"
	print "* Testing 123 *"
	print "***************"
	set_colour('RESET')
	return 0

if __name__ == '__main__':
	main()



