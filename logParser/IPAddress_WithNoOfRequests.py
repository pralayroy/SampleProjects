# This task I have created a function and created a CSV file to display the same
# Used regex to get the IP address
# Then save the IP addressed into a CSV file with number of requests made on each addressed

import collections
import csv
import re


def ipAddressWithNoOfReq(filename):
    with open(filename) as rd:
        log = rd.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regexp, log)
        return ip_list


def countReq(ip_list):
    return collections.Counter(ip_list)


def write_csv(counter):
    with open('D:\\PyProjects\\logParser\\logs\\ipAddress.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IPAddress', 'NoOfRequest']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == '__main__':
    write_csv(countReq(ipAddressWithNoOfReq('D:\\PyProjects\\logParser\\logs\\access.log')))

