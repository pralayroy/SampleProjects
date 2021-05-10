# Used regex to get the status code from the access.log


"""
import re
import  sys
counter_200 = 0
counter_300 = 0
logfiles = open("D:\\PyProjects\\logParser\\logs\\access.log", "r")
log = logfiles.readlines()
for line in log.split('\n'):
    if line:
        regex = re.search(r'\s\d{3}\s', line)
        #if regex == '200':
        if regex.group().strip() == '200':
            counter_200 += 1
        if regex.group().strip() == '300':
            counter_300 += 1

print('Status-200:  ', counter_200)
print('Status-300:  ', counter_300)
"""

# Here used lars.apache. Lars provides a wrapper for Apache log files, typically in common or combined format

from lars.apache import ApacheSource
count_200 = 0
count_300 = 0
with open('D:\\PyProjects\\logParser\\logs\\access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            if row.status == 200:
                count_200 += 1
            if row.status == 300:
                count_300 += 1
        print(f'200 status code {count_200}')
        print(f'300 status code {count_300}')

f.close()
