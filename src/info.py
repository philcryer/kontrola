import psutil

def sysInfo():
    cpu = psutil.cpu_count()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    specs = [cpu, memory, disk]

    for c in specs:
        print specs
        print c
   # return specs

print sysInfo()
