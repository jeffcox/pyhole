#!/usr/bin/env python3

# Imports
import re
import sys
import logging
import requests

# Hard codes, maybe a config file someday
meta_allow_url = ''
allow_url = "https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt"
meta_block_url = "https://v.firebog.net/hosts/lists.php?type=tick"
block_list = []
block_set = set()

install_dir = "/usr/local/etc/pyhole"
dns_server = "unbound"

logging.basicConfig(filename='pyhold.log', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Let's make a Regular Expression!
fqdn_regex = re.compile('(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)')

# Try to update the curated white list from github

# Nope, this should be a function or class or object of some kind
# Make it generic for downloading lists
# It should accept n URLs to concatenate
# It can then be reused to fetch the list of lists, and the contents of each list

def list_downloader(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.text.split()
    else:
        sys.exit("Fatal error with downloading ",url)

# Download the allow list(s) and listify them for later
try:
    allowed_domains = list_downloader(allow_url)
    print(allowed_domains)
    print(type(allowed_domains))
except:
    logging.error('Could not fetch allowed domains')

# Get the list of block lists
try:
    list_of_blocks = list_downloader(meta_block_url)
    print(list_of_blocks)
    print(type(list_of_blocks))
except:
    logging.error('Could not fetch list of block lists')

# Iterate through the list of block lists
# Jam the entries into a list for later
for x in list_of_blocks:
    block_list.append(list_downloader(x))

logging.debug(block_list)
print(type(block_list))

# Deduplicate and validate (it's later)
for u in block_list:
    if fqdn_regex.match(u):
        block_set.add(u)
    else:
        logging.debug("Skipped a domain ",u)

# Validate the allow list and remove matching entries
for q in allowed_domains:
    if fqdn_regex.match(q):
        block_set.remove(q)
    else:
        logging.debug("Bad allow list entry ",q)


# Try to update the tick_list of "safe" domains to block

# Retrieve blocklist URLs and parse domains from adlists.list

# Define options for when retrieving blocklists

# Download specified URL and perform checks on HTTP status and file content

# Parse source files into domains format

# Create (unfiltered) "Matter and Light" consolidated list

# Parse consolidated list into (filtered, unique) domains-only format

# Whitelist user-defined domains

# Output count of blacklisted domains and regex filters

# Parse list of domains into hosts format

# Create "localhost" entries into hosts format

# Create primary blacklist entries

# Create user-added blacklist entries

# Trap Ctrl-C

# Clean up after Gravity upon exit or cancellation

# Convert the contets into a format unbound can read

# Trap Ctrl-C

# Let's just fuckin do it.

# Perform when downloading blocklists, or modifying the whitelist

# Perform when downloading blocklists, or modifying the white/blacklist (not wildcards)
