# -*- coding: utf-8 -*-

import os
#Copy this file to one of the following locations, then rename it to conf.py:
#/etc/staticDHCPd/, ./conf/

#For a full overview of what these parameters mean, and to further customise
#your system, please consult the configuration and scripting guides in the
#standard documentation


# Whether to daemonise on startup (you don't want this during initial setup)
DAEMON = False

#WARNING: The default UID and GID are those of root. THIS IS NOT GOOD!
#If testing, set them to your id, which you can find using `id` in a terminal.
#If going into production, if no standard exists in your environment, use the
#values of "nobody": `id nobody`
#The UID this server will use after initial setup
UID = 0
#The GID this server will use after initial setup
GID = 0

#The IP of the interface to use for DHCP traffic
DHCP_SERVER_IP = '127.0.0.1'

#The database-engine to use
#For details, see the configuration guide in the documentation.
CASE_INSENSITIVE_MACS = True
SQLITE_FILE = '/tmp/dhcp.sqlite'
DATABASE_ENGINE = 'SQLite'


DEBUG = True

#PID_FILE = os.path.realpath(__file__) + '/../run/process.pid'


# web settings
WEB_PORT = 8080


# Logging
# LOG_FILE : text, None : default=None
# 
#     The path to which logs should be written
#     The specified file must be writeable if it already exists, or containing directory must allow file-creation
#     '/var/log/staticDHCPd/staticDHCPd.log' is a good choice, but you must create the directory and set appropriate permissions first
# 
# LOG_FILE_HISTORY : integer, None : default=7
# 
#     If logging to a file, this will cause logs to rotate once per day, with retention up to the specified number of days
#     If None, which is not recommended, the specified file will grow indefinitely
# 
# LOG_FILE_SEVERITY : text : default=’WARN’
# 
#     Controls how much information appears in the log-file: only events at least this important
#     One of 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'
# 
# LOG_CONSOLE_SEVERITY : text : default=’INFO’
# 
#     Controls how much information appears in the console: only events at least this important
#     Console-based logging is disabled when running as a daemon
#     One of 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'
# 
#
#
# Database:SQLite
# CASE_INSENSITIVE_MACS : boolean : default=False
# 
#     Forces case-insensitive comparisons for MACs
#     If this matters to you, you should create a NOCASE index over maps:mac instead, for greater efficiency
# 
# USE_CACHE : boolean : default=False
# 
#     Causes data retrieved from the database to be stored in memory until the cache is flushed via reinitialisation
#     For SQLite, this should normally be False
# 
# EXTRA_MAPS : list : default=None
# 
#     Any non-standard fields to read from the maps table, which will be provided in definition.extra, keyed as maps.$COLUMN
# 
# EXTRA_SUBNETS : list : default=None
# 
#     Any non-standard fields to read from the subnets table, which will be provided in definition.extra, keyed as subnets.$COLUMN
# 
# SQLITE_FILE : text : MUST BE SPECIFIED if using SQLite
# 
#     The path to the file that contains your SQLite database
# 
# 
# Server behaviour
# ALLOW_LOCAL_DHCP : boolean : default=True
# 
#     Whether link-local DHCP requests will be handled
# 
# ALLOW_DHCP_RELAYS : boolean : default=False
# 
#     Whether relayed DHCP requests will be handled
# 
# ALLOWED_DHCP_RELAYS : list : default=[]
# 
#     If relayed requests are allowed, providing a list of IPs, like ['192.168.1.1', '192.168.2.1'], will limit which ones will be accepted
#     If empty, all relays are considered acceptable
# 
# ENABLE_RAPIDCOMMIT : boolean : default=True
# 
#     Whether rapid-commit (RFC 4039) semantics should be processed for supporting clients.
#     If this causes problems, please report it as a bug and provide details.
# 
# AUTHORITATIVE : boolean : default=False
# 
#     Controls whether unknown MACs should be NAKed instead of ignored
#     If you are likely to run multiple DHCP servers that do not share the same lease-status information, this should be False, or else clients will experience intermittent stability issues, as one server contradicts the other instead of staying silent
# 
# NAK_RENEWALS : boolean : default=False
# 
#     Whether REBIND and RENEW requests should be NAKed when received, forcing clients to either wait out their lease or return to the DISCOVER phase
#     This is good if you expect that you will be changing your configuration in the near future
# 
# UNAUTHORIZED_CLIENT_TIMEOUT : integer : default=60
# 
#     The number of seconds for which unknown MACs should be ignored, to avoid wasting processing resources unnecessarily
# 
# MISBEHAVING_CLIENT_TIMEOUT : integer : default=150
# 
#     The number of seconds for which MACs that are sending invalid requests should be ignored; with dynamic servers, these could be trying to trigger a DoS scenario, so there’s no point in wasting resources on them
# 
# ENABLE_SUSPEND : boolean : default=True
# 
#     Whether MACs that are flooding the server will be considered as misbehaving
# 
# SUSPEND_THRESHOLD : integer : default=10
# 
#     The number of times a well-behaved MAC can interact with the server before being being considered as misbehaving
#     The number of interactions in memory is reduced by one per second
# 
# 