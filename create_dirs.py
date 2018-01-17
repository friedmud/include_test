import os
from string import Template

top_dir = 'projects'

main_dirs = ['moose','misc','phase_field','chemical_reactions','fluid_properties','module_loader','porous_flow','solid_mechanics','water_steam_eos','combined','heat_conduction','rdg','stochastic_tools','xfem','contact','level_set','navier_stokes','richards','tensor_mechanics']

sub_dirs = ['actions','dampers','geomsearch','materials','parser','samplers','utils','auxkernels','dgkernels','ics','mesh','partitioner','splits','vectorpostprocessors','base','dirackernels','indicators','meshmodifiers','postprocessors','timeintegrators','bcs','distributions','interfacekernels','multiapps','preconditioners','timesteppers','constraints','executioners','kernels','nodalkernels','predictors','transfers','controls','functions','markers','outputs','restart','userobject']

num_files = 20

header_template = """#ifndef ${classname}_h
#define ${classname}_h

class $classname
{
public:
  int dumb = 1;
};

#endif
"""

source_template = """#include"$headerfile"
namespace
{
  $classname stuff;
  stuff.dumb = 4;
}
"""

for mdir in main_dirs:
    for sdir in sub_dirs:
        include_path = os.path.join(top_dir, mdir, 'include', sdir)
        source_path = os.path.join(top_dir, mdir, 'src', sdir)

        try:
            os.makedirs(include_path)
            os.makedirs(source_path)
        except:
            pass

        for i in xrange(num_files):
            classname = sdir + str(i)
            header_filename = classname + '.h'
            source_filename = classname + '.C'

            header_content = Template(header_template).substitute(classname=classname)

            source_content = Template(source_template).substitute(headerfile=header_filename, classname=classname);

            header_file = open(os.path.join(include_path, header_filename), 'w')
            header_file.write(header_content)
            header_file.close()

            source_file = open(os.path.join(source_path, source_filename), 'w')
            source_file.write(source_content)
            source_file.close()
