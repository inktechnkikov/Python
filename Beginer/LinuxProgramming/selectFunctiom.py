import subprocess

ch = 1
if(ch == '1'):
    def disk_func():
        diskpace = "fdisk"
        argument = "-l"
        subprocess.call([diskpace,argument],shell=True)
