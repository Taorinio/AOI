from needle import *

"""
COL = fragColor
CRD = fragCoord
TME = iTime
CHN[n] = iChannel..n
"""

#--------- Set up this thing ---------

RES = (120, 30)
COL = (0, 0, 0)
TME = 0
CHN = [Image.open("image.png")]
SPD = 0.2

#-------------------------------------

_ROW_ARRAY = []
_COL_ARRAY = []
_PIXEL = "@"
_INIT_TIME = time()

def TEXTURE(image, array):
    return tuple([j / 255 for j in image.getpixel([int(array[i] * image.size[i]) for i in range(2)])])

while True:
    sleep(SPD)
    TME = time() - _INIT_TIME
    _COL_ARRAY.clear()

    for _Y in range(RES[1] - 1):
        for _X in range(RES[0]):
            
            CRD = (_X, _Y)
            
            #--------- Your program goes here. ---------
            
            
            
            #----------------------------------------------------------------------
            
            _ROW_ARRAY.append(COL)
            
        _COL_ARRAY.append(_ROW_ARRAY.copy())
        _ROW_ARRAY.clear()
        
    for _Y in _COL_ARRAY:
        for _X in _Y:
            print(fgn(_PIXEL, [int(i * 255) for i in _X]), end = "")
        print()
    
input()
