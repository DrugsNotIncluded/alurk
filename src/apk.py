import re
import subprocess

def apk(root=False,*args):
        packages_list = subprocess.Popen(f'{if root == True: return("sudo")} apk {" ".join(args)}',
                                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        converted_packages_list = []
        for element in packages_list.stdout.readlines():
            converted_packages_list.append(element.strip())
        return(converted_packages_list)

def get_available_packages():
        raw_data = apk("search")
        pattern_compiled = re.compile(r'-[^-]+-r[0-9]+')
        packages_list = []
        for string in raw_data:
        	packages_list.append(pattern_compiled.sub("", string))

        return(packages_list)

