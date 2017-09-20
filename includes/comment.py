def display_results(HOSTNAME, NET_ID, RESULTS, SEVERITY, COMMENTS):
    print HOSTNAME.ljust(40) + NET_ID.ljust(20) + RESULTS.ljust(20) + SEVERITY.ljust(20) + COMMENTS

def comment(HOSTNAME, NET_ID, FIELD1, FIELD2, FIELD3, DIR):
    display_results(HOSTNAME, NET_ID, FIELD1, FIELD2, FIELD3)
