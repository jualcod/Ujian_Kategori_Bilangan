num1 = float(input('Ketik angka :'))
num1rd = round(num1)
num = int(num1)

# Menentukan Bulat
def Bul(num1,num1rd):
    if num1 == 0 or num1/num1rd == 1:
        return('bulat')
    elif num1/num1rd != 1:
        return('pecahan')

# Menentukan Negatif atau Cacah
def NegCah(num):
    if Bul(num1,num1rd) == 'bulat':
        if num < 0:
            return('negatif')
        elif num >= 0:
            return('cacah')

# Menentukan Nol atau Asli
def NolAs(num):
    if NegCah(num) == 'cacah':
        if num == 0:
            return('nol')
        elif num > 0:
            return('asli')

# Menentukan Ganjil atau Genap
def GanGen(num):
    if NolAs(num) == 'asli':
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

def kategori_bilangan(num):
    return([Bul(num1,num1rd),NegCah(num), NolAs(num), GanGen(num), PriKom(num)] )
print(kategori_bilangan(num))

# Ekspektasi
# Ketik angka : 2
# ['bulat', 'cacah', 'asli', 'genap', 'prima']

# Ketik angka : 15
# ['bulat', 'cacah', 'asli', 'ganjil', 'komposit']

# Ketik angka : 1.5 or -1.5
# ['pecahan', None, None, None, None]