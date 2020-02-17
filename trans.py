import os
from time import time
import subprocess
import random
import re

os.chdir('C:/Users/luis/Documents/GitHub/cortarMp3/transformados ')
path = 'C:/Users/luis/Documents/GitHub/cortarMp3/transformados'  # path
files = []
tiempo_inicial = time()
print("empezando a leer archivos transformados")
i = 0  # contador de archivos
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            args = ("ffprobe", "-show_entries", "format=duration", "-i", file, '-hide_banner', '-loglevel', 'panic',)
            popen = subprocess.Popen(args, stdout=subprocess.PIPE)
            popen.wait()
            output = popen.stdout.read()
            files.append([file, output])
            i = i + 1
# termina lectura de la carpeta
numeroArchivos = i
tiempo_final = time()
tiempo_ejecucion2 = tiempo_final - tiempo_inicial
print("terminado de leer archivos tardo:" + str(tiempo_ejecucion2) + " en segundos un total de " + str(i))
tiempo_inicial = time()
i = 0
# cuanto tiempo tardo en realizar el proceso
print("empezando a cortar de los 30 final")
final = -30
tiempo = 30
for f in files:
    # print(f)
    i = i + 1
    tiempoCadena = f[1].decode("utf-8")
    duracion = tiempoCadena.split("=")
    try:
        duracion = duracion[1]
        duracion2 = duracion.split('\r')
        duracion = duracion2[0]
        duracion = re.sub('[^A-Za-z0-9]+', '', duracion)
        duracion = int(duracion) / 1000000
        duracion_real = duracion - 30
    # subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-sseof',str(final),'-t',str(tiempo),'-c','copy',str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
        subprocess.call(
            ['ffmpeg', '-y', '-t', str(duracion_real), '-i', f[0], '-c', 'copy', "../transformados2/" + str(i) + "-" + f[0],
            '-hide_banner', '-loglevel', 'panic', ])
    except:
        print("archivo vacio "+ f[0])
        pass
    
tiempo_final = time()
tiempo_ejecucion2 = tiempo_final - tiempo_inicial + tiempo_ejecucion2
print("terminado de leer archivos tardo:" + str(tiempo_ejecucion2) + " en segundos")