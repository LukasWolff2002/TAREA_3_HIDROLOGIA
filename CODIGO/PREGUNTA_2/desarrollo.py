from math import exp

#Data

U2 = {'Ene': 243.0, 'Feb': 240.0, 'Mar': 120.0, 'Abr': 118.0, 'May': 115.0, 
 'Jun': 242.0, 'Jul': 242.0, 'Ago': 121.0, 'Sep': 242.0, 'Oct': 242.0, 'Nov': 242.0, 'Dic': 242.0}

for meses in U2:
    U2[meses] = (U2[meses]*1000)/(60*60*24)

Rn = {'Ene': 25.8, 'Feb': 18.6, 'Mar': 11.4, 'Abr': 11.9, 'May': 7.9, 
 'Jun': 6.6, 'Jul': 7.6, 'Ago': 10.4, 'Sep': 11.9, 'Oct': 17.0, 'Nov': 20.2, 'Dic': 24.7}

Tmin = {'Ene': 11.6, 'Feb': 11.3, 'Mar': 9.8, 'Abr': 8.1, 'May': 7.4, 
 'Jun': 6.0, 'Jul': 5.3, 'Ago': 5.8, 'Sep': 7.0, 'Oct': 8.2, 'Nov': 9.2, 'Dic': 10.7}

Tmax = {'Ene': 26.7, 'Feb': 26.4, 'Mar': 25.6, 'Abr': 22.6, 'May': 19.2, 
 'Jun': 16.7, 'Jul': 16.7, 'Ago': 18.1, 'Sep': 19.6, 'Oct': 21.8, 'Nov': 25.4, 'Dic': 26.2}

HR = {'Ene': 71.0, 'Feb': 74.0, 'Mar': 74.0, 'Abr': 76.0, 'May': 79.0, 
 'Jun': 79.0, 'Jul': 79.0, 'Ago': 79.0, 'Sep': 79.0, 'Oct': 75.0, 'Nov': 72.0, 'Dic': 70.0}

meses = U2.keys()

#Tengo que determinar la tasa de riego

#Datos quillota
latitud = -32.88341
longitud = -71.24882
altura = 462 

#Como no pasa los 45 grados se considera una latitud media
#Para una fehca de siembra es el 01 de cotubre

Ini = 30
Des = 60
Med = 40
Fin = 80
Total = 210

#Pagina 107 del libro

Kc_ini = 0.3
Kc_med = 0.7
Kc_fin = 0.45

#Pagina 112 del libro

#Segun el metodo de perman, la evapotranspiracion de referencia se calcula como:
ETo = {}
for mes in meses:

    G = 1 #Definir comooooooo

    gamma = 0.64 
    Tmean = (Tmax[mes]+Tmin[mes])/2
    es = 0.6108*exp((17.27*Tmean)/(Tmean+237.3))
    ea = es*(HR[mes]/100)
    delta = (4098*es)/((Tmean+237.3)**2)

    num = 0.408*delta*(Rn[mes]-G)+gamma*(900/(Tmean+273))*U2[mes]*(es-ea)
    den = delta+gamma*(1+0.34*U2[mes])
    ETo[mes] = num/den   

print(ETo) #mm/dia


#Ahora definio la tasa de riego para el mes de maxima demanda
#Primero calculo ETC

#El maximo ocurre entre 90 y 120 dias despues de la siembra
#Lo que se traduce a diciembre enero y febrero
#Por lo que calculo el maximo

ET_dic = Kc_med*ETo['Dic']
ET_en = Kc_med*ETo['Ene']
ET_feb = Kc_med*ETo['Feb']

ET = max(ET_dic,ET_en,ET_feb)


#Luego la tasa de riuego es:
#SE supone Pu = 0
#H es humedad, se supone igual a 0
Pu = 0
H = 0
n = 0.95

TR = (ET - Pu - H)/n

print(TR) #mm/dia

#Son 600 HA
A = 800*10000 #m2
TR = TR/1000 #m/dia
TR = TR*A #m3/dia
TR = TR/(3600) #m3/s

print(TR, 'm3/s') #m3/s
