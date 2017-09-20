# STIGCHECK
DoD DISA STIG Check for Cisco IOS, IOS-XE, NXOS, IOS-XR and Brocade Devices
by Mike Partain with dependency on CiscoConfParse by Mike Pennington.

##### This was developed on RHEL 7 / CentOS 7 with Python 2.7.5

## Python Module Requirements
    ciscoconfparse==1.2.47
    lxml==3.7.3
    netmiko==1.3.0
    openpyxl==2.4.8
    tqdm==4.15.0
    
You should be able to install the dependencies with 'pip install -r requirements.txt' but some have trouble with
this.  I am looking for a fix. if the above does not work try the below in a bash shell:

`cat requirements.txt | while read line; do pip install $line; done`

That should install all modules.  If you are not using virtualenv then run the installs as root.

### Results
1.  Results are compiled and presented in a rollup spreadsheet in the results folder.  There will be an XLSX file
    generated that will provide a listing of findings by device type, open findings, not reviewed findings, percentage of
    completion of the review, etc.  Additionally there are two tabs in the worksheet that presents a breakdown by 
    device type and also a complete Rollup of all findings.  The Rollup tab can be filtered to reflect all Failed(open)
    and not reviewed NETIDs.  This can be helpful for remediating those devices with open finding.

### StigCheck.py
To run the StigChecker you will need to have your configs stored in a directory that is accessible
by this script.

1. Option 1, run all stig checks against the configs in the directory of your choice.  All results will be stored
   in results/today/hostname.results.txt (results/2017-09-15/r1.results.txt)
  * python StigCheck.pyc

2. Option 2, same as option 1 but it will generate the STIG Checklists for each device in the checklists/ folder.
   This checklist can be opened by the DISA Stigviewer and will reflect the Open, NotReviewed, and NA results as 
   determined by this script.
  * python StigCheck.pyc -all


### stigger.pyc
Each device in the configs directory is classified as a type, L3_SWITCH, L2_SWITCH, ROUTER, etc.  Each device
is additionally identified by Vendor and Device type.  This can be used to test one single device like:

1. Option 1, this will run all STIG checks for the device and save the results in 
   results/today/hostname.results.txt (results/2017-09-15/r1.results.txt)
  * python stigger.pyc configs/r1 CISCO ROUTER

2. Option 2, this will run a single STIG check for that device and display the results to the screen.
No report is generated.
  * python stigger.pyc configs/r3 CISCO ROUTER NET0800

***There is a stig options file in the includes/ directory that has some basic options you can modify.  Do this with Caution.



### VENDOR
  * Cisco
  * Brocade
  * Juniper (Coming soon... Hopefully)
  
### Device Types
  * L3_SWITCH
  * L2_SWITCH
  * ROUTER
  * IOS_XR
  * NXOS_L2_SWITCH
  * IPSEC
  * PERIMETER
