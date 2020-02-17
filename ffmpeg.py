import os
import subprocess
import random
import re
from time import time
import funciones as ff
import ftplib
clear=lambda:os.system('cls')
clear() #borra la pantalla
print("recortar audios")
path=os.getcwd()
patho=os.getcwd()

os.chdir(path)
#path='C:/Users/luis/Documents/GitHub/cortarMp3' #path
files =[]
tiempo_inicial=time()
print("empezando a leer archivos")
i=0 #contador de archivos
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            output=0
            files.append([file,output])
            i=i+1
 #termina lectura de la carpeta      
numeroArchivos=i
tiempo_final=time()
tiempo_ejecución=tiempo_final-tiempo_inicial
print("terminado de leer archivos tardo:"+str(tiempo_ejecución)+" en segundos un total de "+ str(i))
tiempo_inicial=time()
i=0 
#cuanto tiempo tardo en realizar el proceso 
print("empezando a cortar inicial") 
inicial=30
tiempo=30   
for f in files:
    i=i+1
    #subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-sseof',str(final),'-t',str(tiempo),'-c','copy',str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
    subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-c','copy',"./transformados/"+str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
#-ss specifies the start time, e.g. 00:01:23.000 or 83 (in seconds)
#-t specifies the duration of the clip (same format).
#Recent ffmpeg also has a flag to supply the end time with -to.
#-c copy copies the first video, audio, and subtitle bitstream from the input to the output file without re-encoding them. This won't harm the quality and make the command run within seconds.
tiempo_final=time()
tiempo_ejecución=tiempo_final-tiempo_inicial+tiempo_ejecución
print("terminado de leer archivos tardo:"+str(tiempo_ejecución)+ " en segundos")
#termino de quitar los 30 segundos del inicio


path=path+"/transformados"
os.chdir(path)
files =[]
tiempo_inicial=time()
print("empezando a leer archivos transformados")
i=0#contador de archivos
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            args=("ffprobe","-show_entries", "format=duration","-i",file,'-hide_banner','-loglevel','panic',)
            popen=subprocess.Popen(args,stdout =subprocess.PIPE)
            popen.wait()
            output=popen.stdout.read()
            files.append([file,output])
            i=i+1
 #termina lectura de la carpeta      
numeroArchivos=i
tiempo_final=time()
tiempo_ejecución2=tiempo_final-tiempo_inicial
print("terminado de leer archivos tardo:"+str(tiempo_ejecución2)+" en segundos un total de "+ str(i))
tiempo_inicial=time()
i=0 
#cuanto tiempo tardo en realizar el proceso 
print("empezando a cortar de los 30 final") 
final=-30
tiempo=30   
for f in files:
#print(f)
    i=i+1
    try:
        tiempoCadena=f[1].decode("utf-8")
        duracion=tiempoCadena.split("=")
        duracion=duracion[1]
        duracion2=duracion.split('\r')
        duracion=duracion2[0]
        duracion=re.sub('[^A-Za-z0-9]+', '', duracion)
        duracion=int(duracion)/1000000
        duracion_real=duracion-30

        #subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-sseof',str(final),'-t',str(tiempo),'-c','copy',str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
        subprocess.call(['ffmpeg','-y','-t',str(duracion_real) ,'-i',f[0],'-c','copy',"../transformados2/"+str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
    except:
        print("error con archivo "+str(f[0]))
tiempo_final=time()
tiempo_ejecución2=tiempo_final-tiempo_inicial+tiempo_ejecución2
print("terminado de leer archivos tardo:"+str(tiempo_ejecución)+" en segundos")



#ahora al azar
path=path+"2"
os.chdir(path)
#path='C:/Users/luis/Documents/GitHub/cortarMp3/transformados2' #path
files =[]
tiempo_inicial=time()
print("empezando a leer archivos transformados2")
i=0#contador de archivos
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            args=("ffprobe","-show_entries", "format=duration","-i",file,'-hide_banner','-loglevel','panic',)
            popen=subprocess.Popen(args,stdout =subprocess.PIPE)
            popen.wait()
            output=popen.stdout.read()
            files.append([file,output])
            i=i+1
 #termina lectura de la carpeta      
numeroArchivos=i
tiempo_final=time()
tiempo_ejecución3=tiempo_final-tiempo_inicial
print("terminado de leer archivos tardo:"+str(tiempo_ejecución3)+" en segundos un total de "+ str(i))
tiempo_inicial=time()
i=0 
#cuanto tiempo tardo en realizar el proceso 
print("empezando a cortar final") 
inicial=30
tiempo=30   
for f in files:
#print(f)
    i=i+1
    try:
        tiempoCadena=f[1].decode("utf-8")
        duracion=tiempoCadena.split("=")
        duracion=duracion[1]
        duracion2=duracion.split('\r')
        duracion=duracion2[0]
        duracion=re.sub('[^A-Za-z0-9]+', '', duracion)
        duracion=int(duracion)/1000000
        duracion_real=duracion-30
        inicial=random.randint(1,int(duracion_real))
        #subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-sseof',str(final),'-t',str(tiempo),'-c','copy',str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
        subprocess.call(['ffmpeg','-y', '-ss',str(inicial),'-i',f[0],'-c','copy','-t', '30',"../final/"+str(i)+"-"+f[0],'-hide_banner','-loglevel','panic',])
    except:
        print("error con archivo " + str(f[0]))
tiempo_final=time()
tiempo_ejecución3=tiempo_final-tiempo_inicial+tiempo_ejecución3
print("terminado de leer archivos tardo:"+str(tiempo_ejecución)+" en segundos")
tiempo_total= tiempo_ejecución+tiempo_ejecución2+tiempo_ejecución3
print("listo en "+str(tiempo_total))

path=""
print(path)
path=patho
print(path)
path=path+"\\transformados"
print(path)
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        pass#print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        #print('borrando ' + folderName + ': '+ filename)
        os.unlink(folderName+'\\' +filename)
    print('BORRANDO transformado')
path=""
print(path)
path=patho
print(path)
path=path+"\\transformados2"
print(path)
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        pass#print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        #print('BORRANDO ' + folderName + ': '+ filename)
        os.unlink(folderName+'\\' +filename)
    print('borrado transformados 2')

    # preparar archivos

path=patho+"\\final"
      # subir archivos procesados
print("iniciando ftp")
ff.upFTP(path)
print("finalizando ftp")