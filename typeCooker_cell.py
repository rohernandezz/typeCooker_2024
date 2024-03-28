from importlib import reload

###Imports, etc =================================
from drawBot import *
from drawbotlab.color import *
import random

import tkColor
reload(tkColor)
from tkColor import *

###CONFIG===============================================
demoOn = False
saveOn = False
###===============================================

defaultFont = 'Asadera-regular'
texts_ejemplo = {
    
        'Letra'       :'A',
        'Fecha'       :'1 de Abril',
        'Diseña1'     :"",
        'D!_Social'   :"",
        'Diseña2'     :'',
        'D2_Social'   :'',
        'Autorx'      : 'Andrea Buendía',
        'autorxPaís'  : 'México',
        'autorxSocial':"@AndreaEjemploRedes",
        'ES_Receta'   : "Vamos a canalizar a nuetro Cyrus Highsmith interior. Está será una /g minúscula de doble piso, en una hoja muy grande con una herramienta de trazo grueso/ancho, primero dibujaremos la forma completamente negra y después con corrector blanco vamos a añadir la contraforma. Tiene que ser relativamente ancha (extra puntos si abarca toda la hoja), de alto contraste y con formas coquetas* (*receta en proceso)",
        
        'EN_Receta' : """Let's channel our inner Cyrus Highsmith. This will be a double-storey lowercase "g", on a very large sheet with a thick stroke tool. First, we'll draw the shape completely in black, and then with white correction fluid, we'll add the counter form. It should be relatively wide (bonus points if it covers the entire sheet), high-contrast, and with playful shapes (*recipe in progress).""",
        }

tkGeneralDict = {
'Hashtags' : "#28DaysOfTypecooker #Letrastica"
,}


def addZeroCoord(position, zeroCoord):
    posX, posY = position[0],position[1]
    newPos = posX, posY + zeroCoord
    return newPos

def doText(_text, _font, _fill, position, 
           _tracking=0,
           align='left',
           textSize=12,
           xStart=420,
           zeroCoord=0 ):
    
    newPosition = addZeroCoord(position, zeroCoord)
               
    with savedState():
        fillColor(_fill)
        font(_font, textSize)
        tracking(_tracking)
        text(_text,newPosition,align=align)
#------------------------------------------

def doTextBox(_text, _font, _fill, _rect, 
              _tracking=0,
              _align='left',
              textSize=12,
              zeroCoord= 0 ):
                  
    newRect = (_rect[0], _rect[1]+zeroCoord,_rect[2],_rect[3])
    
    with savedState():
        fillColor(_fill)
        font(_font, textSize)
        tracking(_tracking)
        textBox(_text, newRect,align=_align)
#------------------------------------------

def doTextMisprint(text, font, fill, position, 
                   align='left',
                   bkFill=tkWhite,
                   textSize=12,
                   _tracking=0,
                   xOffset=(-10,10),
                   yOffset=(-5,15),
                   blending='multiply',
                   zeroCoord= 0 ):
                       
    def randRange(a,b):
        return random.uniform(a,b)
    #-----------------------------
    newPosition = addZeroCoord(position, zeroCoord)        
        
    doText(text, font, bkFill, newPosition, align=align, _tracking=_tracking, textSize=textSize)

    posX, posY = newPosition[0], newPosition[1]
    
    xOffset = randRange(yOffset[0], yOffset[1])
    newPositionX = posX + xOffset
    yOffset = randRange(yOffset[0], yOffset[1])
    newPositionY = posY + yOffset

    offsetPosition = (newPositionX, newPositionY)
    
    with savedState():
        blendMode(blending)
        doText(text, font, fill, offsetPosition, align=align, _tracking=_tracking, textSize=textSize)
    
    return (xOffset,yOffset)
#------------------------------------------>>>>>    

def drawTypeCookerCell(textsDict, 
                       anchoCell= 1080,
                       altoCell = 1080,
                       bk_Color = tkPink,
                       colorA   = tkBlue,
                       colorB   = tkOrange,
                       language = 'ES',
                       draw     = True,
                       debug    = False,
                       zeroCoord= 0):    
    
    zeroCoord = (altoCell-anchoCell)/2
    
    defaultFont = 'Asadera-regular'
    font2 = 'Chango-Regular'
        
    #==Background===========
    fillColor(bk_Color)
    rect(0,0,anchoCell, altoCell)

    #==Texts=================
    
    socialTextSize = 33
    headTextSize   = 28
    bodyTextSize   = 28

    #==LANGUAGE SHIT:    
    #if language == 'ES':
    RecetaTXT = textsDict["ES_Receta"]
    recipeByTXT = "RECETA POR :"

    # print(language)           
    if language == "EN":
       RecetaTXT = textsDict["EN_Receta"]
       recipeByTXT = "RECIPE BY :"       
    elif language  != 'ES':
        print('👾 language Error')
    #------------------------------------------
    
       
    #==LETRA:
    bothCases_letra = f'{textsDict["Letra"].upper()}{textsDict["Letra"].lower()}'
    #--drawLetra:
    doTextMisprint(bothCases_letra, 
                   font2, colorB, (15, 150),
                   #align='left',
                   textSize=520,
                   xOffset=(-8,10),
                   yOffset=(-10,12),
                   _tracking=-25,
                   blending='multiply',
                   zeroCoord=zeroCoord
                   )
    #==AUTORX:      
    
    #--Receta x:
    doText(recipeByTXT, defaultFont, tkWhite, (100,970), 
           textSize=headTextSize,align='left',zeroCoord=zeroCoord)
          
    autorxTXT = textsDict["Autorx"]
   
    if autorxTXT == '':
       autorxTXT = '👉🏼--MISSING--⚠️'   
       
    colorA_offset = doTextMisprint(autorxTXT, 
                   font2, colorA, (95, 900),
                   #align='left',
                   textSize=72,
                   xOffset=(-2,3),
                   yOffset=(-4,2),
                   blending='multiply',
                   zeroCoord=zeroCoord
                   )

    #--AutorSocial    
    autorSocial_String = f'@{textsDict["autorxSocial"].strip("@")}'
    if autorSocial_String == "@":
       autorSocial_String = '👉🏼 MISSING' 
       
    doText(autorSocial_String , defaultFont, tkWhite, (100,850),
          textSize=socialTextSize,zeroCoord=zeroCoord)    
          
    #--AutorPaís
    doText(f'–{textsDict["autorxPaís"]}', defaultFont, tkBlack, (100,800),
               textSize=32, zeroCoord=zeroCoord)    

    #===👠 Footer
    #--Hashtag
    doText(tkGeneralDict['Hashtags'], defaultFont, tkWhite, (941,80),
           textSize=headTextSize,zeroCoord=zeroCoord, align='right')   
    #--Fecha
    
    colorA_X_offset =(colorA_offset[0],colorA_offset[0])
    colorA_Y_offset =(colorA_offset[1],colorA_offset[1])
    #print(colorA_Y_offset)
    
    doTextMisprint(textsDict["Fecha"] , font2, colorA, (100, 80),
                   xOffset=colorA_X_offset, yOffset=colorA_Y_offset,
                   textSize=headTextSize*1.15,align='left',zeroCoord=zeroCoord)    

#DESCRIPTION:    
    descriptionBox = [510,330,450,470]
    descriptionBox[1]+=zeroCoord
    
    with savedState():
        pass
        #stroke(1,1,1)
        #fill(None)
        #rect(*descriptionBox)
            
    doTextBox(RecetaTXT, defaultFont, tkBlack, descriptionBox, textSize=28)
    
    #fontSize(150)
    #text(txtLetra,(100,900))
#------------------------------------------>>>
    
if demoOn:
    anchoCell= 1080
    altoCell = 1920
#    altoCell= 1080    
    
    newPage(anchoCell, altoCell)
    drawTypeCookerCell(texts_ejemplo,
                       anchoCell= anchoCell,
                       altoCell = altoCell,
                       draw=True, debug=True,
                       language='ES'
                       )
    if saveOn:
        saveImage('~/Desktop/TEST.png')        