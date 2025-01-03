from needle import *

"""
COL = fragColor
CRD = fragCoord
TME = iTime
CHN[n] = iChannel..n
"""

#--------- Set up this thing ---------

RES = (90, 40)
COL = (0, 0, 0)
TME = 0
CHN = [Image.open("image.png")]
SPD = 0.05

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
            
            uv = (CRD[0] / RES[0], CRD[1] / RES[1])

            tex = TEXTURE(CHN[0], uv)

            norm_tex = [i * 255 for i in tex]
            
            mod_tex = [i / 255 for i in hgb((hsv(norm_tex)[0] + TME * 30, hsv(norm_tex)[1], hsv(norm_tex)[2]))]
            
            COL = mod_tex
            
            #----------------------------------------------------------------------
            
            _ROW_ARRAY.append(COL)
            
        _COL_ARRAY.append(_ROW_ARRAY.copy())
        _ROW_ARRAY.clear()
        
    for _Y in _COL_ARRAY:
        for _X in _Y:
            print(fgn(_PIXEL, [int(i * 255) for i in _X]), end = "")
        print()
    
input()
