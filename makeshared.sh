gcc -fPIC -c test.c
gcc -shared -Wl,-soname,libtest.so.1 -o libtest.so.1.0 test.o
rm test.o
ln -s libtest.so.1.0 libtest.so.1
ln -s libtest.so.1 libtest.so

mkdir -p opt
mkdir -p opt/lib
mv libtest.so* opt/lib/
