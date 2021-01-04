#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  preProcessor.py
#  
#  Copyright 2021 William Martinez Bas <metfar@gmail.com>
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
#  THIS IS A PREPROCESSOR FOR HACK ASSEMBLER. 

#  THE FIRST FUNCTION IS TO REMOVE ANY EXTRA COMMENT OR VOID LINE.

#  THE SECOND IS TO SUBSTITUTE ANY # 


#  THIS IS A WORK IN PROGRESS. TAKE IT AS IT IS.
#  

def IN(where,what):
	out=len(where)+1;
	for f in what:
		if f in where:
			return(True);
	return(False);

def INDEXOF(where,what):
	out=len(where)+1;
	for f in what:
		if(f in where) and where.index(f)<out:
			out=where.index(f);
	return(out);

ON=on=TRUE=true=True;
OFF=off=FALSE=false=False;

OPS=['0', '1', '-1', 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A', 'M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M'];


def main(args):
	LABELS=[];
	argv=list(args);
	#argv.append("-l");
	#argv.append("init.asm");
	
	if(len(argv)<2):
		print("\n",argv[0],""" requires at least one parameter:

"""+argv[0]+""" init.asm     It will process the code and return to STDOUT

"""+argv[0]+""" -l init.asm  Do the same but showing memory positions

		""");
		return(1);
	if(argv[1]=="-l"):
		LINENUMBER=ON;
		argv.pop(1);
	else:
		LINENUMBER=OFF;
	try:
		f=open(argv[1],"rt");
	except:
		print("File "+argv[1]+" could not be processed");
	txt=f.readlines();
	lin=list();
	PC=0;
	for f in txt:
		if(len(f.strip())>0):
			a=INDEXOF(f,["//","#"])
			line=f[:a].strip();
			if(a<len(f) and f[a]=="#"):
				line+=str(PC+1);
			if(len(line)>0):
				if(line[0]=="("):
					LABELS.append({PC+1,line[1:line.index(")")]});
				else:
					PC+=1;
					lin.append(line);
					if(LINENUMBER):
						line=("%03d: "%PC)+line;
					print(line);
	print(LABELS);
	return(0);
	
if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
