CXX = g++
SWIG = swig
SWIGFLAGS = -Isrc/nre -c++ -v -python  
CXXFLAGS = -fPIC -c 
LDFLAGS = -shared
INCLUDE = -I/usr/include/python2.7 -I/home/ubuntu/DocxFactory/include
OBJS = NavalLetter_wrap.o NavalLetter.o 
LIBS = -L/home/ubuntu/DocxFactory/lib -l:libDocxFactory.so

all:
	swig -Isrc/nre -c++ -v -python NavalLetter.swig
	g++ -fPIC -c NavalLetter.cpp NavalLetter_wrap.cxx -I/usr/include/python2.7/ -I/home/ubuntu/DocxFactory/include
	g++ NavalLetter_wrap.o NavalLetter.o -shared -o _NavalLetter.so -L/home/ubuntu/DocxFactory/lib -l:libDocxFactory.so


clean:
	rm -f NavalLetter.py NavalLetterFinal.docx *.pyc *.o *.so *.cxx 










