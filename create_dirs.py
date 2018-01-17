import os
from string import Template
from random import randint

num_apps = 10
num_systems = 30
num_files = 10
num_includes = 5
num_header_includes = 2

top_dir = 'projects'

app_dirs = ['app' + str(i) for i in xrange(num_apps)]

system_dirs = ['system' + str(i) for i in xrange(num_systems)]


header_template = """#ifndef ${classname}_h
#define ${classname}_h

$includes

class $classname
{
public:
  int dumb = 1;
};

#endif
"""

source_template = """#include"$headerfile"

$includes

void ${classname}_func()
{
  $classname stuff;
  stuff.dumb = 4;
}
"""

for adir in app_dirs:
    for sdir in system_dirs:
        include_path = os.path.join(top_dir, adir, 'include', sdir)
        source_path = os.path.join(top_dir, adir, 'src', sdir)

        try:
            os.makedirs(include_path)
            os.makedirs(source_path)
        except:
            pass

        classnames = [adir + sdir + 'class' + str(i) for i in xrange(num_files)]

        for classname in classnames:
            header_filename = classname + '.h'
            source_filename = classname + '.C'

            num_header_include = randint(0,num_header_includes)

            random_header_includes = ['#include"' + 'app' + str(randint(0, num_apps-1)) + 'system' + str(randint(0, num_systems-1)) + 'class' + str(randint(0, num_files-1)) + '.h"' for i in xrange(num_header_include)]
            random_includes = ['#include"' + 'app' + str(randint(0, num_apps-1)) + 'system' + str(randint(0, num_systems-1)) + 'class' + str(randint(0, num_files-1)) + '.h"' for i in xrange(num_includes)]

            header_includes = '\n'.join(random_header_includes)
            includes = '\n'.join(random_includes)

            header_content = Template(header_template).substitute(classname=classname, includes=header_includes)

            source_content = Template(source_template).substitute(headerfile=header_filename, classname=classname, includes=includes);

            header_file = open(os.path.join(include_path, header_filename), 'w')
            header_file.write(header_content)
            header_file.close()

            source_file = open(os.path.join(source_path, source_filename), 'w')
            source_file.write(source_content)
            source_file.close()
