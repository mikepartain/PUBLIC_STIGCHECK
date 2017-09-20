# STIGCHECK
All in one file
DoD DISA STIG Check for Cisco IOS, IOS-XE, NXOS, and Brocade Devices
by Mike Partain with dependency on CiscoConfParse by Mike Pennington.

To run the StigChecker you will need to have your configs stored in a directory that is accessible
by this script.

1. Oprion 1, run all stig checks against the configs in the directory of your choice
  * python SC-Simple.pyc

2. Option 2, same as option 1 but it will generate the STIG Checklists for each device in the checklists/ folder
  * python SC-Simple.pyc -all


There is a stig options file in the includes/ directory that has some basic options you can modify.  Do this with Caution.

Each device in the configs directory is classified as a type, L3_SWITCH, L2_SWITCH, ROUTER, etc.  Each device
is additionally identified by Vendor.  This can be used to test one single device like:

1. Option 1, this will run all STIG checks for the device and save the results in results/<todays day>
  * python stigger.pyc configs/r1 CISCO ROUTER

2. Option 2, this will run a single STIG check for that device and display the results to the screen.
No report is generated.
  * python stigger.pyc configs/r3 CISCO ROUTER NET0800


# Python Module Requirements
Additionally install the below for Cryptopgraphy to build
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev

    appdirs==1.4.3
    asn1crypto==0.22.0
    bcrypt==3.1.3
    cffi==1.10.0
    cisco-decrypt==0.8.3
    ciscoconfparse==1.2.47
    colorama==0.3.7
    cryptography==1.8.1
    dnspython==1.15.0
    enum34==1.1.6
    et-xmlfile==1.0.1
    idna==2.5
    ipaddr==2.1.11
    ipaddress==1.0.18
    jdcal==1.3
    lxml==3.7.3
    netmiko==1.3.0
    openpyxl==2.4.8
    packaging==16.8
    paramiko==2.1.2
    pyasn1==0.2.3
    pycparser==2.17
    PyNaCl==1.1.2
    pyparsing==2.2.0
    PyYAML==3.12
    scp==0.10.2
    six==1.10.0
    tqdm==4.15.0


You should be able to install the dependencies with 'pip install -r requirements.txt' but some have trouble with
the cryptography.  If you have cryptography already satisfied try this from a bash shell:

bash# cat requirements.txt | while read line; do pip install $line; done

That should install all modules.  If you are not using virtualenv then run the installs as root.
