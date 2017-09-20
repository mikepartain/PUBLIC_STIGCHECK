# ALL DIRECTORIES MUST END with a /
#ZIP_FILES is the directory in which the STIG ZIP files exist
ZIP_FILES = 'ZIP_FILES/' 
STIGS = 'stigs/'

STIG_ZIP = ['U_Network_L2_Switch','U_Network_Infrastructure_Router','U_Network_Perimeter_Router_L3_Switch','U_Network_IPSec_VPN_Gateway']

# Reporting
REPORT_DIR = 'results/'
DEVICE_LIST_FILE = 'device_listing.txt'
DEVICE_LIST_XLSX = 'device_listing.xlsx'

DEVICE_LIST = REPORT_DIR+DEVICE_LIST_FILE

# Define you Management Vlan below
MGMT_INT = 'Vlan15'

# Define the ENCLAVE PERIMETER DEVICES
PERIMETER = ['r1']

# Define interfaces connecting to DISA
EXT_INTS = ["Ethernet0/0", "Ethernet0/1"]

# Define internal interfaces [Perimeter router to Firewall]
INT_INTS = ["Vlan1500", "Ethernet2/2"]

# Define external, to DISA, interface ACL names
# EXT_ACLS = ["ip access-list extended ACL_INBOUND"]
# INT_ACLS = ["ip access-list extended ACL_OUTBOUND" ]


# Define your TACACS Servers
TACACS = ['server-private 192.168.1.1','server-private 192.168.1.2']

#NEXUS Valid account     
NXOS_VALID_ACCOUNTS = ['admin']

#CAMPUS
CAMPUS = ['r2', 'r3']

# Define the Enterprise Server VLAN names below
ENT_SRVFRM_VLAN_LIST = ["interface Vlan7", "interface Vlan13", "interface Vlan14", "interface Vlan15", "interface Vlan16", "interface Vlan18", "interface Vlan69", "interface Vlan70", "interface Vlan90", "interface Vlan91"]
