# fungsi untuk mengubah suhu dari celcius ke kelvin
def celciusKeKelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin


# fungsi untuk mengubah suhu dari kelvin ke celcius
def kelvinKeCelcius(kelvin):
    celcius = kelvin - 273.15
    return celcius


# fungsi untuk mengubah suhu dari kelvin atau celcius ke fahrenheit
def keFahrenheit(suhuAwal, satuanSuhu):
    if satuanSuhu == 'celcius':
        fahrenheit = 9/5 * suhuAwal + 32
    elif satuanSuhu == 'kelvin':
        fahrenheit = suhuAwal * 9/5 - 459.67
    else:
        return "masukkan parameter \'celcius\' atau \'kelvin\'"
    return fahrenheit


# fungsi untuk mengubah suhu dari fahrenheit ke celcius atau kelvin
def dariFahrenheit(fahrenheit, satuanSuhu):
    if satuanSuhu == 'celcius':
        suhu = (fahrenheit-32) * 5/9
    elif satuanSuhu == 'kelvin':
        suhu = (fahrenheit + 459.67) * 5/9
    else:
        return "masukkan parameter \'celcius\' atau \'kelvin\'"
    return suhu 