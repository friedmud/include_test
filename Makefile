include_dirs := $(shell find projects/*/include -type d)
include_flags := $(foreach i, $(include_dirs), -I$(i))

CPPFLAGS := -std=c++14 $(include_flags)

srcfiles  := $(shell find projects -name "*.C")

objects	:= $(patsubst %.C, %.o, $(srcfiles))

main: main.C $(objects)

clean:
	$(foreach i, $(objects), $(shell rm -f $(i)))
	rm -f main
