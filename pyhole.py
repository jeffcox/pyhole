#!/usr/bin/env python3

# Imports
import re
import sys
import logging
import requests

# Define variables, maybe a config file someday
meta_allow_url = ''
allow_url = "https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt"
meta_block_url = "https://v.firebog.net/hosts/lists.php?type=tick"
block_list = []
block_set = set()

# This needs to be modular someday
install_dir = "/usr/local/etc/pyhole"
dns_server = "unbound"

logging.basicConfig(filename='pyhole.log', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Let's make a Regular Expression!
# https://stackoverflow.com/questions/11809631/
fqdn_regex = re.compile('(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)')

# Download text files and turn them into lists
# Works for lists of URLs and block lists
def list_downloader(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return r.text.split()
    else:
        sys.exit("Fatal error with downloading ",url)

# Download the allow list(s) and listify them for later
try:
    allowed_domains = list_downloader(allow_url)
except:
    logging.error('Could not fetch allowed domains')

# Get the list of block lists
try:
    list_of_blocks = list_downloader(meta_block_url)
except:
    logging.error('Could not fetch list of block lists')

# Iterate through the list of block lists
# Jam the entries into a list for later
for x in list_of_blocks:
    block_list.append(list_downloader(x))

# The block list is now a weird list of lists, let's strip it down
unlist_block = str(block_list)
block_list = unlist_block.split()

# Deduplicate and validate (it's later)
# regex.match returns an object, not just a bool
for u in block_list:
    m = fqdn_regex.match(u)
    if m:
        block_set.add(u)

# We need to fix entries that have 0.0.0.0 mashed together with the FQDN
# They look like this: 0.0.0.0bad.domain

# Validate the allow list and remove matching entries
for q in allowed_domains:
    m = fqdn_regex.match(q)
    if m:
        try:
            block_set.remove(q)
        except:
            print("Allowed domain ", q, " was not in the block list")
    else:
        logging.debug("Bad allow list entry")

# Format the deduplicated, allowified list into something unbound likes
# awk command from bash: awk '{print "local-zone: \""$1"\" redirect\nlocal-data: \""$1" A 0.0.0.0\""}' ${adList} > ${piholeDir}/ads4.conf

print("Made it to the end!")
print("Here's what's in block_set:")
with open('output.txt','a') as f:
    for entry in block_set:
        f.write(entry)
print(type(block_set))
