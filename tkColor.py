from drawbotlab.color import RGBColor, CMYKColor
    
#### Convertir colores Hex a floatas
def hex2FloatsRGB(hexC, kwargs=False):

    # Convert the hexadecimal color to RGB values
    r = int(hexC[0:2], 16) / 255.0
    g = int(hexC[2:4], 16) / 255.0
    b = int(hexC[4:6], 16) / 255.0
    
    color = [r,g,b]
    # print(f"{color}")
    
    if kwargs:
        return(dict(zip('rgb', color))) #make dictionary for kwargs
    else:
        return color

#print(**hex2FloatsRGB(0xFF3131)) 


tkPink   = RGBColor(**hex2FloatsRGB('FAA7C4' ,kwargs=True))
tkBlue   = RGBColor(**hex2FloatsRGB('3f93d0' ,kwargs=True))
tkOrange = RGBColor(**hex2FloatsRGB('f76100' ,kwargs=True))
tkYellow = RGBColor(**hex2FloatsRGB('ffcb21' ,kwargs=True))
tkBlack  = RGBColor(**hex2FloatsRGB('191918' ,kwargs=True))
tkWhite  = RGBColor(**hex2FloatsRGB('fff5f1' ,kwargs=True))


pkRed    = RGBColor(**hex2FloatsRGB('FF3131' ,kwargs=True))
pkOrange = RGBColor(**hex2FloatsRGB('FE9833' ,kwargs=True))
pkYellow = RGBColor(**hex2FloatsRGB('FFE100' ,kwargs=True))
pkGreen  = RGBColor(**hex2FloatsRGB('00C26E' ,kwargs=True)) 
pkBlue   = RGBColor(**hex2FloatsRGB('0894FF' ,kwargs=True)) 
pkViolet = RGBColor(**hex2FloatsRGB('9749E5' ,kwargs=True))
pkPurple = pkViolet
pkBlue   = RGBColor(**hex2FloatsRGB('0894FF' ,kwargs=True)) 

pkWhite  = RGBColor(**hex2FloatsRGB('EEF0EF' ,kwargs=True)) 
pkTBlue  = RGBColor(**hex2FloatsRGB('62E2FF' ,kwargs=True)) 
pkTPink  = RGBColor(**hex2FloatsRGB('FFB0E5' ,kwargs=True)) 
pkTBrown = RGBColor(**hex2FloatsRGB('7D3230' ,kwargs=True)) 

pkBrown = pkTBrown
pkWhite = RGBColor(**hex2FloatsRGB('EEEFEE' ,kwargs=True)) 
#pkWhite = RGBColor(1,1,1) #used for 11 through 1_3

#Color pallettes=============================================

pkC_Trans = [pkTBlue, pkTPink, pkWhite]
pkC_Q     = [pkTBrown]

##Flags=======================================================
pkFlag_Trans = [pkTBlue, pkTPink, pkWhite, pkTPink, pkTBlue]
pkFlag_LGBT  = [pkRed, pkOrange, pkYellow, pkGreen, pkBlue, pkViolet, pkBlue]
pkFlag_LGBTQ = pkC_Trans + [pkTBrown] + pkFlag_LGBT

