num1 = float(input('Ketik angka :'))
num1rd = round(num1)
num = int(num1)

# Menentukan Bulat
def Bul(num1,num1rd):
    if num1/num1rd == 1:
        return('bulat')
    elif num1/num1rd != 1:
        return('pecahan')

# Menentukan Negatif atau Cacah
def NegCah(num):
    if num < 0:
        return('negatif')
    elif num >=0:
        return('cacah')

# Menentukan Nol atau Asli
def NolAs(num):
    if num == 0:
        return('nol')
    elif num >0:
        return('asli')

# Menentukan Ganjil atau Genap
def GanGen(num):
    if num % 2 == 0:
        return('genap')
    else:
        return('ganjil')

# Menentukan Prima atau Komposit
def PriKom(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return('komposit')
        else:
            return('prima')


# print([NegCah(num), NolAs(num), GanGen(num), PriKom(num)])

print([Bul(num1,num1rd), NegCah(num), NolAs(num), GanGen(num), PriKom(num)])


# Ketik angka : 2
# ['bulat', 'cacah', 'asli', 'genap', 'prima']

# Ketik angka : 15
# ['bulat', 'cacah', 'asli', 'ganjil', 'komposit']