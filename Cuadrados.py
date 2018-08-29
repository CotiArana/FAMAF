#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ej1.py
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

def cuadrado():
	speed(0)
	for lados in range (4):
		forward(20)
		left(360/4)

def triangulo():
	speed(0)
	for lados in range (3):
		forward(20)
		left(360/3)
