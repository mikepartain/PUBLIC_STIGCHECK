import os, sys, shutil, argparse, zipfile, re, io, datetime, subprocess, gc, time
from datetime import datetime
from xml.dom import minidom
from openpyxl import *

from openpyxl.styles import *
from ciscoconfparse import *
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetMikoTimeoutException
from collections import Counter
from time import *
from datetime import *


COUNT = 0
FAIL = 0
PASS = 0
NA = 0
DIR = ''
NR = 0

#######STATUS AND RESULTS############
def fwteam(FNAME, NET_ID, SEVERITY, DIR):
    comment(FNAME, NET_ID, 'CHECK', SEVERITY.ljust(30) + 'FWTEAM This needs to be validated', DIR)

# This section is what writes the results to the file named HOSTNAME.results
def write_results(HOSTNAME, NET_ID, RESULTS, SEVERITY, COMMENT, DIR):
    f = open('results/' + DIR + '/' + HOSTNAME + '.results.txt', 'a')
    f.write(HOSTNAME.ljust(40) + NET_ID.ljust(20) + RESULTS.ljust(20) + SEVERITY.ljust(20) + COMMENT.ljust(20) +"\n")
    f.close()

# This sections is what displays the results to the screen
def display_results(HOSTNAME, NET_ID, RESULTS, SEVERITY, COMMENTS):
    print HOSTNAME.ljust(40) + NET_ID.ljust(20) + RESULTS.ljust(20) + SEVERITY.ljust(20) + COMMENTS

def comment(HOSTNAME, NET_ID, FIELD1, FIELD2, FIELD3, DIR):
    # display_results(HOSTNAME, NET_ID, FIELD1, FIELD2, FIELD3)
    write_results(HOSTNAME, NET_ID, FIELD1, FIELD2, FIELD3, DIR)

# Timer to calculate the time it takes to run a STIG Check.
def start_device_timer(DIR, HOSTNAME):
    print 'Starting STIG Checks on ' + DIR + ' device ' + HOSTNAME + ' at ' + str(datetime.now())
    global start_time
    start_time = datetime.now()
    comment(HOSTNAME, 'START', 'TIME', str(datetime.now()), DIR)

def stop_device_timer(DIR, HOSTNAME):
    et_time = datetime.now() - start_time
    comment(HOSTNAME, 'COMPLETE', "TIME", str(datetime.now()).ljust(30) + 'Total Time ' + str(et_time), DIR)
    # print 'Completed Infrastructure Router STIG Check on '+HOSTNAME+' at ' + str(datetime.now()) + ' Total Time ' + str(et_time)

def start_all_timer(DIR):
    print 'Starting STIG Checks on All ' + DIR + ' Devices at ' + str(datetime.now())
    global start_time
    start_time = datetime.now()
    # comment(DIR, 'START', 'TIME', str(datetime.now()), DIR)

def stop_all_timer(DIR):
    et_time = datetime.now() - start_time
    # comment(DIR, 'COMPLETE', "TIME", str(datetime.now()).ljust(30)+'Total Time '+str(et_time), DIR)
    print 'Completed STIG Check on all devices at ' + str(datetime.now()) + ' Total Time ' + str(et_time)

## Stop Timer Functions


# Cleanup removes a specific file, or all associated files for a particular team, Campus, TLA.
def cleanup(HOSTNAME, DIR):
    results = ('results/' + DIR + '/' + HOSTNAME + '.results.txt')
    if os.path.exists(results):
        os.remove(results)

def clean_all(DIR):
    directory = ('configs/' + DIR + '/')
    for file in os.listdir(directory):
        try:
            os.remove('results/' + DIR + '/' + file + '.results.txt')
        except OSError, e:
            pass

## End CLEAUP

# General use functions
def get_acl(ext_int):
    acls = parse.find_children_w_parents(ext_int, "access-group")
    #print len(acls)
    for acl in acls:
        acl = acl.lstrip()
        acl = acl.rsplit(' ',1)[0]
        acl = re.sub('group', 'list extended', acl)
        #print 'ACL:', acl
        return acl

def get_in_acl(ext_int):
    acls = parse.find_children_w_parents(ext_int, "access-group.*in$")
    #print len(acls)
    for acl in acls:
        acl = acl.lstrip()
        acl = acl.rsplit(' ',1)[0]
        acl = re.sub('group', 'list extended', acl)
        #print 'ACL:', acl
        return acl

def get_out_acl(ext_int):
    acls = parse.find_children_w_parents(ext_int, "access-group.*out$")
    #print len(acls)
    for acl in acls:
        acl = acl.lstrip()
        acl = acl.rsplit(' ',1)[0]
        acl = re.sub('group', 'list extended', acl)
        #print 'ACL:', acl
        return acl

def get_native_vlan(HOSTNAME):
    native_vlans = []
    native = parse.find_lines('switchport trunk native vlan')
    for vlan in native:
        native_vlan = vlan.strip().split()[4]
        if native_vlan not in native_vlans:
            native_vlans.append(native_vlan)
    #print native_vlans
    return native_vlans




native_trunk = (r'^\s*(switchport\s+trunk\s+native\s+vlan\s+(\d+))\s*$')
