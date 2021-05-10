import collections
logfiles = open("D:\\PyProjects\\logParser\\logs\\access.log", "r")

clean_log = []
for line in logfiles:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass
counter = collections.Counter(clean_log)
# get the Top 10 requested pages and the number of requests made for each
for count in counter.most_common(10):
    print(str(count[1]) + " " + str(count[0]))


logfiles.close()

