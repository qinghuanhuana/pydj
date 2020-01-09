import psutil
import datetime

# print(psutil.cpu_count(), psutil.cpu_count(logical=False))
# print(psutil.cpu_percent(), psutil.cpu_percent(1),psutil.cpu_percent(2))
# print(psutil.virtual_memory())
# print(psutil.disk_partitions(), psutil.disk_usage('/'))
# print(psutil.disk_io_counters(), psutil.disk_io_counters(perdisk=True))
# print(psutil.net_io_counters(), psutil.net_io_counters(pernic=True))
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H: %M: %S'))
# print(psutil.pids())
print(psutil.Process(3766))
