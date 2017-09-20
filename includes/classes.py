import gc, os
class Device(object):
    def __init__(self, type, hostname, stig, vendor):
        self.type = type
        self.hostname = hostname
        self.stig = stig
        self.aor = aor
        self.vendor = vendor



class dev_host(object):
    def __init__(self, hostname, type, STIG, VENDOR):
        self.hostname = hostname
        self.type = type
        self.VENDOR = VENDOR
        self.STIG = STIG

    def getName(self):
        return self.hostname

    def __str__(self):
        return "%s is a %s" % (self.hostname)

class net_id(object):
    def __init__(self, stig_name, netid, severity):
        self.stig_name = stig_name
        self.netid = netid
        self.severity = severity

    def getName(self):
        return self.stig_name

    def __str__(self):
        return "%s is a %s" % (self.stig_name)





class Host(object):
    def __init__(self, hostname, type):
        self.hostname = hostname
        self.type = type

    def getName(self):
        return self.hostname

    def getType(self):
        return self.type

    def __str__(self):
        return "%s is a %s" % (self.hostname, self.type)


