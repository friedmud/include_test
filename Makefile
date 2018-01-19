#include_dirs := $(shell find projects/*/include -type d)
include_dirs := $(realpath projects/include)
include_flags := $(foreach i, $(include_dirs), -I$(i))

CPPFLAGS = -I/opt/moose/mpich-3.2/clang-5.0.0/include -std=c++14 $(include_flags) -MMD -MP -MF $@.d -MT $@
LDFLAGS := -Wl,-commons,use_dylibs -L/opt/moose/mpich-3.2/clang-5.0.0/lib -lmpicxx -lmpi -lpmpi

all: main

#srcfiles  := $(shell find projects -name "*.C")
#objects	:= $(patsubst %.C, %.o, $(srcfiles))

apps := $(shell find projects -maxdepth 1 -mindepth 1)

#$(info apps $(apps))

srcsubdirs :=

srcsubdirs := $(foreach app, $(apps), $(shell find $(app)/src -maxdepth 1 -mindepth 1))

#$(info srcsubdirs $(srcsubdirs))

# 1: the unity file to build
# 2: the source files in that unity file
define unity_file_rule
$(1): $(2)
	@echo '$$(foreach srcfile, $$^, #include"$$(notdir $$(srcfile))"\n)' > $$@
endef

$(foreach srcsubdir, $(srcsubdirs), $(eval $(call unity_file_rule, $(srcsubdir)/$(notdir $(srcsubdir))_Unity.C, $(shell find $(srcsubdir) -name "*.C"))))

unity_srcfiles := $(foreach srcsubdir, $(srcsubdirs), $(srcsubdir)/$(notdir $(srcsubdir))_Unity.C)
objects := $(patsubst %.C, %.o, $(unity_srcfiles))

# $(info object $(objects))

main: main.C $(objects)

clean:
	$(foreach i, $(objects), $(shell rm -f $(i)))
	$(foreach i, $(unity_srcfiles), $(shell rm -f $(i)))
	rm -f main
