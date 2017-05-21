#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  be - Bash colour Enhancer
#  
#  Copyright 2012 Nigel Heaney <nigel.heaney(__a_t__)gmail.com>
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
Bash colour Enhancer

A module that will set the colour of text in bash (well that was my scope).
"""
  
import sys
__version__='v0.1'
#define COlour constants
_colour_={}
_colour_['RESET']     = "\033[39m\033[49m"
_colour_['BLACK']     = "\033[30m"
_colour_['GREY']      = "\033[90m"
_colour_['BLUE']      = "\033[34m"
_colour_['LBLUE']     = "\033[94m"
_colour_['GREEN']     = "\033[32m"
_colour_['LGREEN']    = "\033[92m"
_colour_['CYAN']      = "\033[36m"
_colour_['LCYAN']     = "\033[96m"
_colour_['RED']       = "\033[31m" 
_colour_['LRED']      = "\033[91m"
_colour_['PURPLE']    = "\033[35m"
_colour_['LPURPLE']   = "\033[95m"
_colour_['BROWN']     = "\033[33m"
_colour_['YELLOW']    = "\033[93m"
_colour_['LGREY']     = "\033[37m"
_colour_['WHITE']     = "\033[97m"
_colour_['BG_BLACK']  = "\033[40m"
_colour_['BG_RED']    = "\033[41m"
_colour_['BG_GREEN']  = "\033[42m"
_colour_['BG_BROWN']  = "\033[43m"
_colour_['BG_BLUE']   = "\033[44m"
_colour_['BG_PURPLE'] = "\033[45m"
_colour_['BG_CYAN']   = "\033[46m"
_colour_['BG_GREY']   = "\033[47m"

def cprint(colour, printString):
	""" This function will merely print a string in the selected colour. usage:

		import be
		cprint("Green", "this is some text in green")
	"""
	sys.stdout.write(_colour_[colour.upper()] + printString)
	sys.stdout.write(_colour_['RESET'])
	return None

def set_colour(colour):
	""" Use this function to set both foreground and background colours - although seperately to simplify
		usage:
			import be
			set_colour('red')
			set_colour('bg_blue')
			print "print some red text on a blue background ... yuck!"
	"""
	sys.stdout.write(_colour_[colour.upper()])
	return None

def reset_colour():
	""" Use this function to reset colours back to default ... for your terminal """
	sys.stdout.write(_colour_['RESET'])
        return None

def main():
	cprint("Green","Bash Colour Enhancer " + __version__ + "\n")
	cprint("lgreen","=========================\n")
	cprint("grey", "Colour Codes Available:\n")
	for cnames in _colour_:
		sys.stdout.write("   ")
		set_colour(cnames)
		print cnames.upper()
		set_colour('RESET')
	print "\n"
	set_colour('BG_BLUE')
	set_colour('white')
	print "***************"
	print "* Testing 123 *"
	print "***************"
	set_colour('RESET')
	return 0

if __name__ == '__main__':
	main()
