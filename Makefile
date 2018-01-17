include_dirs := $(shell find projects/*/include -type d)
CPPFLAGS := $(foreach i, $(include_dirs), -I$(i)) -std=c++14

srcfiles  := $(shell find projects -name "*.C")

objects	:= $(patsubst %.C, %.o, $(srcfiles))

main: main.C $(objects)
