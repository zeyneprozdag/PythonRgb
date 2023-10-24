import sys
import stdio


r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
    stdio.writeln('the range should be 0-255')
    sys.exit(1)

c = m = y = 0.0
k = 1.0

if r != 0 or g != 0 or b != 0:
    w = max(r / 255, g / 255, b / 255)
    c = (w - r / 255) / w
    m = (w - g / 255) / w
    y = (w - b / 255) / w
    k = 1 - w

stdio.writeln("cyan    = " + str(c))
stdio.writeln("magenta = " + str(m))
stdio.writeln("yellow  = " + str(y))
stdio.writeln("black   = " + str(k))