for _ in range(int(input())):
    day, month = input().split()
    day = int(day)
    if month == 'Mar':
        print('Pisces' if day < 21 else 'Aries')
    elif month == 'Apr':
        print('Aries' if day < 21 else 'Taurus')
    elif month == 'May':
        print('Taurus' if day < 21 else 'Gemini')
    elif month == 'Jun':
        print('Gemini' if day < 22 else 'Cancer')
    elif month == 'Jul':
        print('Cancer' if day < 23 else 'Leo')
    elif month == 'Aug':
        print('Leo' if day < 23 else 'Virgo')
    elif month == 'Sep':
        print('Virgo' if day < 22 else 'Libra')
    elif month == 'Oct':
        print('Libra' if day < 23 else 'Scorpio')
    elif month == 'Nov':
        print('Scorpio' if day < 23 else 'Sagittarius')
    elif month == 'Dec':
        print('Sagittarius' if day < 22 else 'Capricorn')
    elif month == 'Jan':
        print('Capricorn' if day < 21 else 'Aquarius')
    elif month == 'Feb':
        print('Aquarius' if day < 20 else 'Pisces')
