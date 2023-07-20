# ALURK - Poor AUR helper alternative for Alpine linux
## Usage:
`alurk <command> <args>`
| Commands:                |           Description:       |
|--------------------------|------------------------------|
|`alurk add <package name>`|download and install package  |
|`alurk del <package name>`|remove package from system    |
|`alurk update`            |update remote repository index|
|`alurk upgrade`           |upgrade local packages        |
## Installation:
### **alurk requires root access to perform any manipulation!**
Copy whole repository into `~/.local/bin` , make ipm.py executable, add to PATH, add alias if you want, later i will fix executable name.
## WIP:
- **Subpackages support**
- **Support other non-hardcoded repositories**
- **Develop a unified ALUR packages format**
# WHY:
I was searching for a way to have upstream utilities on my PCs with Alpine Linux setup, and it is possible with .apk package format (not without dirty tricks), but keeping repository locally is a pain, so i decided to make centralized package storage and program small wrapper around Alpine's package manager and build system.