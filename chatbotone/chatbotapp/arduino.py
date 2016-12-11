#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Alejandro Gonzalez Barrera <alejandrok5@gmail.com>
# More info: http://alejandrok5.wordpress.com/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
from threading import Thread
from firmata import *

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext



a = Arduino('/dev/ttyACM0')
a.pin_mode(13, firmata.OUTPUT)

def dot():
    a.digital_write(13, firmata.HIGH)
    a.delay(0.5)
    a.digital_write(13, firmata.LOW)
    a.delay(0.5)
def slash():
    a.digital_write(13, firmata.HIGH)
    a.delay(1.5)
    a.digital_write(13, firmata.LOW)
    a.delay(0.5)
def spaceL():
    a.delay(1)
def spaceW():
    a.delay(4)



#
#
# class ArduinoMorse (Thread):
#     def __init__(self, text):
#         Thread.__init__(self)
#         self.text=text
#
#     def run(self):
#             for x in self.text :
#                 if x=='a' or x=='A':
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='b' or x=='B':
#                     slash()
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='c' or x=='C':
#                     slash()
#                     dot()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x=='d' or x=='D':
#                     slash()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='e' or x=='E':
#                     dot()
#                     spaceL()
#                 elif x=='f' or x=='F':
#                    dot()
#                    dot()
#                    slash()
#                    dot()
#                    spaceL()
#                 elif x=='g' or x=='G':
#                     slash()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x=='h' or x=='H':
#                     dot()
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='i' or x=='I':
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='j' or x=='J':
#                     dot()
#                     slash()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='k' or x=='K':
#                     slash()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='l' or x=='L':
#                     dot()
#                     slash()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='m' or x=='M':
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='n' or x=='N':
#                     slash()
#                     dot()
#                     spaceL()
# #                elif x=='ñ' or x=='Ñ':
# #                    slash()
# #                    slash()
# #                    dot()
# #                    slash()
# #                    slash()
# #                    spaceL()
#                 elif x=='o' or x=='O':
#                     slash()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='p' or x=='P':
#                     dot()
#                     slash()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x=='q' or x=='Q':
#                     slash()
#                     slash()
#                     dot()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='r' or x=='R':
#                     dot()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x=='s' or x=='S':
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='t' or x=='T':
#                     slash()
#                     spaceL()
#                 elif x=='u' or x=='U':
#                     dot()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='v' or x=='V':
#                     dot()
#                     dot()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='w' or x=='W':
#                     dot()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='x' or x=='X':
#                     slash()
#                     dot()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='y' or x=='Y':
#                     slash()
#                     dot()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='z' or x=='Z':
#                     slash()
#                     slash()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='0':
#                     slash()
#                     slash()
#                     slash()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='1':
#                     dot()
#                     slash()
#                     slash()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='2':
#                     dot()
#                     dot()
#                     slash()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='3':
#                     dot()
#                     dot()
#                     dot()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='4':
#                     dot()
#                     dot()
#                     dot()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x=='5':
#                     dot()
#                     dot()
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='6':
#                     slash()
#                     dot()
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='7':
#                     slash()
#                     slash()
#                     dot()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='8':
#                     slash()
#                     slash()
#                     slash()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='9':
#                     slash()
#                     slash()
#                     slash()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x=='.':
#                     dot()
#                     slash()
#                     dot()
#                     slash()
#                     dot()
#                     slash()
#                     spaceL()
#                 elif x==',':
#                     slash()
#                     slash()
#                     dot()
#                     dot()
#                     slash()
#                     slash()
#                     spaceL()
#                 elif x=='?':
#                     dot()
#                     dot()
#                     slash()
#                     slash()
#                     dot()
#                     dot()
#                     spaceL()
#                 elif x=='"':
#                     dot()
#                     slash()
#                     dot()
#                     dot()
#                     slash()
#                     dot()
#                     spaceL()
#                 elif x==' ':
#                     spaceW()
#                 else:
#                     pass











#
# def encode(request):
#     text=""
#     morse=[]
#     if request.method == 'GET':
#         # form = SearchForm(request.GET)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             arduino=ArduinoMorse(text)
#             arduino.start()
#             for x in text :
#                 if x=='a' or x=='A':
#                     morse.append('.-')
#                 elif x=='b' or x=='B':
#                     morse.append('-...')
#                 elif x=='c' or x=='C':
#                     morse.append('-.-.')
#                 elif x=='d' or x=='D':
#                     morse.append('-..')
#                 elif x=='e' or x=='E':
#                     morse.append('.')
#                 elif x=='f' or x=='F':
#                    morse.append('..-.')
#                 elif x=='g' or x=='G':
#                     morse.append('--.')
#                 elif x=='h' or x=='H':
#                     morse.append('....')
#                 elif x=='i' or x=='I':
#                     morse.append('..')
#                 elif x=='j' or x=='J':
#                     morse.append('.---')
#                 elif x=='k' or x=='K':
#                     morse.append('-.-')
#                 elif x=='l' or x=='L':
#                     morse.append('.-..')
#                 elif x=='m' or x=='M':
#                     morse.append('--')
#                 elif x=='n' or x=='N':
#                     morse.append('-.')
# #                elif x=='ñ' or x=='Ñ':
# #                    morse.append('--.--')
#                 elif x=='o' or x=='O':
#                     morse.append('---')
#                 elif x=='p' or x=='P':
#                     morse.append('.--.')
#                 elif x=='q' or x=='Q':
#                     morse.append('--.--')
#                 elif x=='r' or x=='R':
#                     morse.append('.-.')
#                 elif x=='s' or x=='S':
#                     morse.append('...')
#                 elif x=='t' or x=='T':
#                     morse.append('-')
#                 elif x=='u' or x=='U':
#                     morse.append('..-')
#                 elif x=='v' or x=='V':
#                     morse.append('...-')
#                 elif x=='w' or x=='W':
#                     morse.append('.--')
#                 elif x=='x' or x=='X':
#                     morse.append('-..-')
#                 elif x=='y' or x=='Y':
#                     morse.append('-.--')
#                 elif x=='z' or x=='Z':
#                     morse.append('--..')
#                 elif x=='0':
#                     morse.append('-----')
#                 elif x=='1':
#                     morse.append('.----')
#                 elif x=='2':
#                     morse.append('..---')
#                 elif x=='3':
#                     morse.append('...--')
#                 elif x=='4':
#                     morse.append('....-')
#                 elif x=='5':
#                     morse.append('.....')
#                 elif x=='6':
#                     morse.append('-....')
#                 elif x=='7':
#                     morse.append('--...')
#                 elif x=='8':
#                     morse.append('---..')
#                 elif x=='9':
#                     morse.append('----.')
#                 elif x=='.':
#                     morse.append('.-.-.-')
#                 elif x==',':
#                     morse.append('--..--')
#                 elif x=='?':
#                     morse.append('..--..')
#                 elif x=='"':
#                     morse.append('.-..-.')
#                 elif x==' ':
#                     morse.append(' ')
#         else:
#             queryset = []
#
#     return render_to_response("arduino/index.html", {'form': form, "text": text, "morse": morse})