# To render this image, install drawbot-skia: https://github.com/justvanrossum/drawbot-skia

# This script is meant to be run from the root level
# of the git repository. For example, from a Unix terminal:

# $ git clone git-repo
# $ cd git-repo
# $ python3 image1.py --output
#// optional command to compress the image:
# $ convert image2.png +dither -colors 64 -depth 4 image2.png && open image2.png

from drawbot_skia.drawbot import *
import math
import subprocess
import sys
import argparse

W, H, M, F = 2048, 2048, 256, 1
U = M/4
DOT =  19*2
AMP = 768
XPO = 0
YPO = 0
GRID_VIEW = False # Change this to "True" for a grid overlay


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = M/4, M/4
    rect(M, M, W-(M*2), H-(M*2))
    for x in range(25):
        polygon((M+STEP_X, M), (M+STEP_X, H-M))
        STEP_X += INCREMENT_X
    for y in range(25):
        polygon((M, M+STEP_Y), (W-M, M+STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((W/2, 0), (W/2, H))
    polygon((0, H/2), (W, H/2))

# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(W, H)
    fill(0)
    stroke(None)
    rect(0, 0, W, H)
    if GRID_VIEW:
        grid()
    else:
        pass
    stroke(1)
    fill(None)
    strokeWidth(4)
    #oval(M, M, W-(M*2), H-(M*2))

def draw_dot(X, Y):
    fill(0)
    oval(int(X)+(W/2), int(Y)+(W/2), DOT, DOT)

def draw_dot_two(X, Y):
    fill(0)
    oval(int(X)+(W/2), int(Y)+(W/2), DOT/2, DOT/2)


def draw_art_one():
    STP = -(math.pi/2)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * AMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * AMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * AMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * AMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * AMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * AMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        polygon((int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)),
                (int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)))
        polygon((int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)),
                (int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)))
        polygon((int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)),
                (int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)))

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi

def draw_dots_one():
    DMP = AMP/1.53
    STP = -(math.pi/2.57)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * DMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * DMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * DMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * DMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * DMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * DMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi


def draw_art_two():
    AMP2 = AMP/1.87
    STP = -(math.pi/2)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * AMP2)-DOT/2
    YPO_A = (-1 * math.sin(STP) * AMP2)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * AMP2)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * AMP2)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * AMP2)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * AMP2)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        polygon((int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)),
                (int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)))
        polygon((int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)),
                (int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)))
        polygon((int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)),
                (int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)))

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi

def draw_dots_two():
    DMP = AMP/2.86
    STP = -(math.pi/2.57)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * DMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * DMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * DMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * DMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * DMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * DMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi


def draw_art_three():
    AMP3 = AMP/3.5
    STP = -(math.pi/2)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * AMP3)-DOT/2
    YPO_A = (-1 * math.sin(STP) * AMP3)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * AMP3)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * AMP3)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * AMP3)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * AMP3)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        polygon((int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)),
                (int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)))
        polygon((int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)),
                (int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)))
        polygon((int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)),
                (int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)))

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)

        STP += (0.003) * math.pi

def draw_dots_three():
    DMP = AMP/5.35
    STP = -(math.pi/2.57)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * DMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * DMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * DMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * DMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * DMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * DMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi

def draw_dots_four():
    DMP = AMP/6.6
    STP = -(math.pi/2)
    print("STP =", STP)
    TRI_ROT = (math.pi/3)*2

    # SET DOT POS
    XPO_A = (math.cos(STP) * DMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * DMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * DMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * DMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * DMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * DMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(6)

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi


def draw_extra():
    stroke(1)
    fill(1)
    strokeWidth(6)
    draw_dot(-DOT/2, -DOT/2)



# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_art_one()
    draw_dots_one()
    draw_art_two()
    draw_dots_two()
    draw_art_three()
    draw_dots_three()
    draw_dots_four()
    draw_extra()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    saveImage("1F7D9-001.svg")
    print("DrawBot: Done")





