from importlib import reload

import tkCSV_Reader
reload(tkCSV_Reader)
from tkCSV_Reader import csvDict

import typeCooker_cell
reload(typeCooker_cell)
from typeCooker_cell import *

#######
debug = False
saveOn = False
########

#-Setup:
#👇🏼
tkDataDict = tkCSV_Reader.csvDict
###########

if debug:
    pass
    #for key in tkDataDict.keys():
        #print(tkDataDict[key])
        #print("")
    
#-------


az = 'abcdefghijklmnopqrstuvwxyz'
az = 'abg'

def colorSet(seed):
    if seed == 1:
        bkColor = tkPink    
        colorA  = tkBlue
        colorB  = tkOrange
    if seed == 2:
        bkColor = tkBlue    
        colorA  = tkPink
        colorB  = tkYellow
    if seed == 3:
        bkColor = tkYellow    
        colorA  = tkBlue
        colorB  = tkOrange
    if seed == 4:
        bkColor = tkPink
        colorA  = tkOrange
        colorB  = tkBlue
    if seed == 5:
        bkColor = tkBlue    
        colorA  = tkYellow
        colorB  = tkPink
    if seed == 6:
        bkColor = tkYellow    
        colorA  = tkOrange
        colorB  = tkBlue       
        
    return bkColor, colorA, colorB

#CONFIG:
anchoPost= 1080
altoPost = 1920
#altoPost = 1080
###############

for altoPost in (1080, 1920):
    #for lang in ('ES','EN'):
    for lang in ('ES',):
        for i, letra in enumerate(tkDataDict.keys()):
            newPage(anchoPost, altoPost)
            
            #colors:						
            _bkColor, _colorA, _colorB = colorSet((i  % 6) + 1)
        
            drawTypeCookerCell(tkDataDict[letra],
                           anchoCell= anchoPost,
                           altoCell = altoPost,
                           bk_Color = _bkColor,
                           colorA   = _colorA,
                           colorB   = _colorB,
                           language = lang,
                           #draw=True,
                           debug=False)
            if saveOn:                       
                saveImage(f'/~/Desktop/TypeCookerImgs/{altoPost}/{i}_{lang}_TypeCooker_{letra}.png')