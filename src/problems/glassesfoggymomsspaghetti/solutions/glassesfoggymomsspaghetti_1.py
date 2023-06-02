import math
# theta = 54
# ang = theta/2
# print(21.5*math.tan(math.radians(ang))*2)

import decimal
        
def value_to_decimal(value, decimal_places):
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP  # define rounding method
    return decimal.Decimal(str(float(value))).quantize(decimal.Decimal('1e-{}'.format(decimal_places)))

d, x, y, h = map(int, input().split())
if y == 0:
    print(format(round(h/x, 6), '.6f'))
    exit()
small_angle = math.degrees(math.atan((y - h/2)/x))
mid_angle = math.degrees(math.atan((y)/x))
big_angle = math.degrees(math.atan((y + h/2)/x))
one_ang = mid_angle - small_angle
one_b = abs(d*math.tan(math.radians(one_ang)))
two_ang = abs(big_angle - mid_angle)
two_b = abs(d*math.tan(math.radians(two_ang)))
print(format(value_to_decimal(one_b + two_b, 6), '.6f'))
