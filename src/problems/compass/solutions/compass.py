phone_dir = int(input())
actual_dir = int(input())
forward = backward = -1
if actual_dir < phone_dir:
    forward = 360 - phone_dir + actual_dir
    backward = actual_dir - phone_dir
elif actual_dir > phone_dir:
    forward = actual_dir - phone_dir
    backward = -(360 - actual_dir + phone_dir)
else:
    forward = 0
    backward = 0
if forward <= abs(backward):
    print(forward)
else: print(backward)
