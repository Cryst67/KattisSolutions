import math
def round_decimals_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor


n=input()
if int(n) < 100:
    print(99)
    exit()
if n[len(n)-2:] == '49' or n[-1]=='0':
    print(int(round_decimals_up(float(n)/10**len(n), len(n)-2)*10**len(n)-1))
else: print(int(round(float(n)/10**len(n), len(n)-2)*10**len(n)-1))
