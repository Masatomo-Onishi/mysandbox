############################################
## Author: Masatomo Onishi
## Created on: Octo. 18th 2014
## Brief:
## If build for debug, add DEBUG=1 behind make.
## Also can clean products for debug with DEBUG=1.
############################################
CXX = g++
RM = rm -rf

##### Set up for Compile
DEBUG = 0

ifeq ($(DEBUG), 1)
	BUILD_TYPE = Debug
	CFLAGS = -g -Wall -O0
else
	BUILD_TYPE = Release
	CFLAGS = -Wall -O2
endif

COMPILE = $(CXX) -c $(CFLAGS) -o

SRCDIR = ./Src/
SOURCES = $(SRCDIR)main.cxx
OBJDIR = ./Bin/$(BUILD_TYPE)/Obj/
OBJECTS = $(OBJDIR)main.o

##### Set up for Link
LIBDIR =
LIBS = -lglut\
			 -lGL\
			 -lGLU\
			 -lm\

LINK_STATIC = ar rcvs
LINK_SHARE = g++ -shared $(LIBDIR) $(LIBS) -o
LINK = g++ $(LIBDIR) $(LIBS) -o

TARGET = ./Bin/$(BUILD_TYPE)/test

##### Set up for doxygen 
DOCUMENT = $(DOXYHTML)index.html
DOXYDIR = ./Doc/
DOXYCONF = $(DOXYDIR)Doxyfile
DOXYHTML = $(DOXYDIR)html/

##### Rules
.PHONY: all clean rebuild run

all: $(TARGET) $(DOCUMENT)

$(TARGET): $(OBJECTS)
	$(LINK) $(TARGET) $(OBJECTS) $(LIBS) $(OPTIONS)

$(OBJDIR)main.o: $(OBJDIR) $(SRCDIR)main.cxx
	$(COMPILE) $(OBJDIR)main.o $(SRCDIR)main.cxx

$(OBJDIR):
	mkdir $(OBJDIR)

$(DOCUMENT) : $(DOXYHTML)

$(DOXYHTML): $(SOURCES) $(DOXYCONF)
	doxygen $(DOXYCONF)

clean:
	$(RM) $(TARGET)
	$(RM) $(OBJECTS)
	$(RM) $(DOXYHTML)

rebuild: clean all

run:
	./$(TARGET)
