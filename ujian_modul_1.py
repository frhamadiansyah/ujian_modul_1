# Soal 1
print ('Soal 1:')
def calculate_years(principal,interest,tax,desired):
    year = 0
    while principal < desired:
        bunga = principal*interest
        bunga = bunga - (bunga*tax)
        principal = principal + bunga
        year += 1
    return print(year)

calculate_years(1000,0.05,0.18,1100)
calculate_years(1200.00, 0.17, 0.05, 2000.00)
calculate_years(1500.00, 0.07, 0.6, 5000.00)





# Soal 2
print ('Soal 2:')
def expandedForm(num):
    breakdown = []
    while num // 10 > 0:
        angka = num % 10
        breakdown.append(angka)
        num = num // 10
        if num < 10:
            num += 10
            angka = num % 10
            breakdown.append(angka)
            break
    z = ''
    for i in range(len(breakdown)-1,-1,-1):
        if i == len(breakdown)-1:
            z += str(breakdown[i]*(10**i))
        elif breakdown[i]*(10**i) == 0:
            continue
        else:
            z += ' + '
            z += str(breakdown[i]*(10**i))
        
    return print (z)


expandedForm(12)
expandedForm(42)
expandedForm(70304)





# Soal 3
print ('Soal 3:')
def tower_builder(n_floors,block_size):
    w,h = block_size
    z = ''
    for i,j in zip(range(n_floors*h),range(n_floors*h-1,-1,-1)):
        for a in range((j//h)):
            for c in range(w):
                z += ' '
        for b in range(((i//h)*2)+1):
            for d in range(w):
                z += '*'
        z += '\n'
    return print (z)


tower_builder(6, (2,1))
tower_builder(3, (2,3))
tower_builder(6, (3,3))

