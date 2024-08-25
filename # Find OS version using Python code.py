# Find OS version using Python code 
import platform
if platform.system() == 'Linux':
    linux_dist = platform.linux_distribution()
    print(linux_dist)
        