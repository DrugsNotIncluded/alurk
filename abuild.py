#!/usr/bin/python
import os
import sys
import re
        
class ApkbuildUtils:
    def get_quoted_param(string, param):
        regex = f"{param}=([\"'])(?:(?=(\\?))\\2.)*?\\1"
        print(regex)
        pattern = re.compile(regex, re.S|re.MULTILINE)
        return(pattern.findall(string))
    
    def abuild(repodest = '', srcdest = '', description = '', cmd='', *options):
        if repodest:
            repodest = f"-P {repodest}"
        if srcdest:
            srcdest = f"-s {srcdest}"
        if description:
            description = f"-D {description}"

        options_list = " ".join(options) + spart_options_list
        command = f"abuild {options_list} {repodest} {srcdest} {description} {cmd}"



hcpath = "/home/coffeemeow/Repo/alur/emacs-pgtk-git/APKBUILD"
f = open(hcpath, "r+")
text = f.read()

plist = ApkbuildUtils.get_quoted_param(text, "makedepends")

#print(text)
print(plist)
