cls
echo bienvenido este programa copia 300 veces el archivo 7.mp3

SET original =7mp3
for /L %%i IN (10,1,9) do copy %original% copy%%i.mp3
for /L %%i IN (10,1,18000) do copy 7.mp3 copy0%%i.mp3
copy 7.mp3 copy.mp3