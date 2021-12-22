PPM = 1000
FPS = 60
dt = 1 / FPS
g = 9.8 / PPM
W, H = 1920, 1078
FG = 255, 255, 255
tile_size = 90
level_map = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX             XX   ',
    ' XX P                       ',
    ' XXXX        XX          XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  '
]
speed = 250


def level():
    return level_map