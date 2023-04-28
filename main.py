import psutil

for i in range(10):
    print('The CPU usage is: ', psutil.disk_partitions())
