def reformatDate(date: str) -> str:
    output = ''
    month_dict = {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12',
    }

    date_sep = date.split(' ')
    output += date_sep[2]
    output += '-'
    output += month_dict[date_sep[1]]
    output += '-'
    day = date_sep[0][:-2]
    if len(day) < 2:
        output += '0'
    output += day

    return output

# Testcases
print('Testcase 1: 20th Oct 2052')
print(reformatDate("20th Oct 2052"))

print('Testcase 2: 6th Jun 1933')
print(reformatDate("6th Jun 1933"))

print('Testcase 3: 26th May 1960')
print(reformatDate("26th May 1960"))
