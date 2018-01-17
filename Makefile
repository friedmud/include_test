#include_dirs := $(shell find projects/*/include -type d)
include_dirs := $(realpath projects/include)
include_flags := $(foreach i, $(include_dirs), -I$(i))

CPPFLAGS = -I/opt/moose/mpich-3.2/clang-5.0.0/include -std=c++14 $(include_flags) -MMD -MP -MF $@.d -MT $@
LDFLAGS := -Wl,-commons,use_dylibs -L/opt/moose/mpich-3.2/clang-5.0.0/lib -lmpicxx -lmpi -lpmpi

srcfiles  := $(shell find projects -name "*.C")

objects	:= $(patsubst %.C, %.o, $(srcfiles))

main: main.C $(objects)

clean:
	$(foreach i, $(objects), $(shell rm -f $(i)))
	rm -f main
