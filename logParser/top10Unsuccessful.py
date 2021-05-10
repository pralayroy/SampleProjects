"""
from lars.apache import ApacheSource
with open('ssl_access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            if row.status == 404:
                print(row.request.url.path_str)
"""

import collections

logfiles = open("D:\\PyProjects\\logParser\\logs\\access.log", "r")

clean_log = []
for line in logfiles:
    try:
        clean_log.append(line[line.index("GET") + 4:line.index("404")])
    except:
        pass
counter = collections.Counter(clean_log)
#Top 10 unsuccessful requests which returns 404 with no of requests
for count in counter.most_common(10):
    print(str(count[1]) + " " + str(count[0]))

logfiles.close()
