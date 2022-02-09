#packages shouldn't split themselves into subpackages, not supported yet.

import re
import subprocess

def abuild(repodest=None, srcdest=None, description=None, cmd=None, *options):
    if repodest:
        repodest = f'-P {repodest}'
    if srcdest:
        srcdest = f'-s {srcdest}'
    if description:
        description = f'-D {description}'
    shell_cmd = f'abuild {" ".join(options)} {repodest} {srcdest} {description} {cmd}'

    stdout = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return(stdout)

def get_quoted_var(var, APKBUILD_DATA):
    """Return any quoted variable by name from APKBUILD data given
       Useful for getting strings without additional bash variables"""
    var_len = len(var)
    pattern = f"{var}=[\"'][^\"']+[\"']"
    pattern_compiled = re.compile(pattern, re.M|re.DOTALL)
    matches = pattern_compiled.findall(APKBUILD_DATA)
    matches_list = []
    for match in matches:
        var_list = match[var_len+2:-1].split() # remove 'var=' prefix, last quote, newlines, tabs & whitespaces, split into list
        matches_list.append(var_list)
    return(matches_list)

def get_var(var, APKBUILD_FILE):
    """Return any var from APKBUILD, uses bash interpretter
       Useful for getting vars containing other vars (subpackages)"""
    cmd = f"source {APKBUILD_FILE} && echo ${var}"
    proc = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    proc.wait()
    output, errors = proc.communicate()
    return(output.rstrip())

def get_subpackages(APKBUILD_FILE):
    return(get_var("subpackages", APKBUILD_DATA))


