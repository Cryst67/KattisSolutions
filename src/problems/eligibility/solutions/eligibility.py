for i in range(int(input())):
    name, pcs, dob, courses = input().split()
    eligible_flag = False
    petition_flag = True
    if int(pcs.split('/')[0]) >= 2010:
        eligible_flag = True
    if int(dob.split('/')[0]) >= 1991:
        eligible_flag = True
    if not eligible_flag and int(courses) >= 41:
        eligible_flag = False
        petition_flag = False
    if eligible_flag:
        print(name, 'eligible')
        continue
    if not petition_flag:
        print(name, 'ineligible')
        continue
    if petition_flag:
        print(name, 'coach petitions')