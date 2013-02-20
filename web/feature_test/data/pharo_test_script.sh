#!/bin/bash

# I must first build the copy of the pharo enviroment to run the test
# Fill it in
workdir='/usr/local/lib/pharo/pharo-wk'
# Relocate the delivered .st file to where it should be
st_to_be_tested=`ls|grep '\.st'`

for file in $st_to_be_tested; do
	cp $st_to_be_tested $workdir/pharo-2.0/
done

# To generate the test file y change to the directory where the image should be
cd $workdir/pharo-2.0/

# generate test.st file
echo "|unaSecuencia|" > test.st

echo "\"7507 - 2C2012 - TP0 - Enunciado 1\"" >> test.st

echo "\"Agregamos un par de metodos a filestream para que tenga la misma interface que Transcript\"" >> test.st
echo "FileStream class compile: 'show:data self stdout lf; nextPutAll: data'." >> test.st
echo "FileStream class compile: 'clear self stdout lf.'." >> test.st
echo "FileStream class compile: 'cr self stdout lf.'." >> test.st

echo "\"Reemplazamos el Transcript por nuestro FileStream\"" >> test.st
echo "Smalltalk at: #Transcript put: FileStream. " >> test.st

echo "Transcript clear." >> test.st
echo "Transcript show: '7507 - 2C2012 - TP0 - Enunciado 1'." >> test.st
echo "Transcript cr." >> test.st

echo "unaSecuencia := Secuencia new." >> test.st

echo "(unaSecuencia estaVacia) ifTrue: [Transcript show: 'Prueba 1 OK']." >> test.st
echo "Transcript cr." >> test.st

echo "unaSecuencia agregar: 1." >> test.st
echo "unaSecuencia agregar: 10." >> test.st
echo "unaSecuencia agregar: 100." >> test.st

echo "unaSecuencia estaOrdenadaAscendente ifTrue: [Transcript show: 'Prueba 2 OK']." >> test.st
echo "Transcript cr." >> test.st

echo "(unaSecuencia obtenerUltimo = 100) ifTrue: [Transcript show: 'Prueba 3 OK']." >> test.st
echo "Transcript cr." >> test.st

echo "unaSecuencia estaVacia ifFalse: [Transcript show: 'Prueba 4 OK']." >> test.st
echo "Transcript cr." >> test.st

echo "unaSecuencia vaciar." >> test.st
echo "unaSecuencia estaVacia ifTrue: [Transcript show: 'Prueba 5 OK']." >> test.st
echo "Transcript cr." >> test.st
echo "Transcript cr." >> test.st

echo "\"Al finalizar de ejecutar las pruebas simplemente salimos\"" >> test.st
echo "Smalltalk exitSucess" >> test.st
echo "" >> test.st
# file generated


files_list=`ls|grep '\.st'`
concatenated_list=""
for i in $files_list; do
	concatenated_list="$concatenated_list $i"
done

# Now I move back to where the pharo cog is located
cd ..

# I build the command
command="./NBCog -vm-display-null ./pharo-2.0/Pharo-2.0.image $concatenated_list"
# And the invoke it
$command

# Capturo el resultado
exit_value=$?

# Cleanup
cd $workdir/pharo-2.0/
rm $concatenated_list

# Finally exit with the returned value
exit $exit_value

