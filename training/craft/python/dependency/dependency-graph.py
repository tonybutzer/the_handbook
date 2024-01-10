import sys
import pkg_resources

def dependencies_for(project_name):
    dist = pkg_resources.get_distribution(project_name)
    return [r.project_name for r in dist.requires()]

printed_dependencies = {}
lib_dependencies = []
def print_dependencies(lib_name):
    global lib_dependencies
    printed_dependencies[lib_name] = True
    deps = dependencies_for(lib_name)

    for dep in deps:
        lib_dependency = '  "%s" -> "%s";' % (lib_name, dep)
        if not lib_dependency in lib_dependencies:
            print (lib_dependency)
            if not dep in printed_dependencies: # avoid circular dependencies
                print_dependencies(dep)
            lib_dependencies.append(lib_dependency)

def print_digraph(libs):
    print ('digraph ipy_dependencies {')
    print ('  rankdir=LR;')
    print ('  truecolor=true;')
    for lib in libs:
        print_dependencies(lib)
    print ('}')

if __name__ == '__main__':
    print_digraph(sys.argv[1:])

