from math import gcd

def lcm(numbers):
    def lcm_two(a, b):
        return (a * b) // gcd(a, b)

    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm_two(current_lcm, number)

    return current_lcm

while True:
    try: nums = list(map(int, input().split()))
    except EOFError: break
    print(lcm(nums))
