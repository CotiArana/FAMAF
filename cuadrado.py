#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graficos.py
#  
#  Copyright 2018 Costanza Arana <cotiarana@gmail.com>
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

from turtle import *
from Cuadrados import cuadrado
from Cuadrados import triangulo

def casa():
	for repetir in range (5):
		triangulo()
		right(90)
		cuadrado()
		forward(20)
		left(90)
		forward(20)
		left(90)
		forward(20)
		right(90)
def barrio():
	casa()
	penup()
	left(180)
	forward(100)
	right(90)
	forward(40)
	right(90)
	pendown()
	casa()

for a in range (3):
	barrio()
	penup()
	left(180)
	forward(100)
	right(90)
	forward(40)
	right(90)
	pendown()
exitonclick()
