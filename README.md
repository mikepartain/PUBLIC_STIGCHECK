# STIGCHECK
DoD DISA STIG Check for Cisco IOS, IOS-XE, NXOS, IOS-XR and Brocade Devices
by Mike Partain with dependency on CiscoConfParse by Mike Pennington.

## StigCheck.py
To run the StigChecker you will need to have your configs stored in a directory that is accessible
by this script.

1. Option 1, run all stig checks against the configs in the directory of your choice.  All results will be stored
   in results/today/hostname.results.txt (results/2017-09-15/r1.results.txt)
  * python StigCheck.pyc

2. Option 2, same as option 1 but it will generate the STIG Checklists for each device in the checklists/ folder
  * python StigCheck.pyc -all


## stigger.pyc
Each device in the configs directory is classified as a type, L3_SWITCH, L2_SWITCH, ROUTER, etc.  Each device
is additionally identified by Vendor.  This can be used to test one single device like:

1. Option 1, this will run all STIG checks for the device and save the results in 
   results/today/hostname.results.txt (results/2017-09-15/r1.results.txt)
  * python stigger.pyc configs/r1 CISCO ROUTER

2. Option 2, this will run a single STIG check for that device and display the results to the screen.
No report is generated.
  * python stigger.pyc configs/r3 CISCO ROUTER NET0800

***There is a stig options file in the includes/ directory that has some basic options you can modify.  Do this with Caution.


# Python Module Requirements
    ciscoconfparse==1.2.47
    lxml==3.7.3
    netmiko==1.3.0
    openpyxl==2.4.8
    tqdm==4.15.0
    


You should be able to install the dependencies with 'pip install -r requirements.txt' but some have trouble with
the cryptography.  If you have cryptography already satisfied try this from a bash shell:

bash# cat requirements.txt | while read line; do pip install $line; done

That should install all modules.  If you are not using virtualenv then run the installs as root.

## VENDOR
  * Cisco
  * Brocade
  * Juniper (Coming soon... Hopefully)
  
## Device Types
  * L3_SWITCH
  * L2_SWITCH
  * ROUTER
  * IOS_XR
  * NXOS_L2_SWITCH
  * IPSEC
  * PERIMETER
