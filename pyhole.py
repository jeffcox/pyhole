#!/usr/bin/env python3

# Imports
import sys
import logging
import requests

# Hard codes, maybe a config file someday
allow_url = "https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt"
meta_block_url = "https://v.firebog.net/hosts/lists.php?type=tick"

install_dir = "/usr/local/etc/pyhole"
dns_server = "unbound"

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Try to update the curated white list from github

# Nope, this should be a function or class or object of some kind
# Make it generic for downloading lists
# It should accept n URLs to concatenate
# It can then be reused to fetch the list of lists, and the contents of each list

def downloader(url):
	# Downbload requests and return results

	# download the url and handle errors
	r = requests.get(url)
	if r.status_code == requests.codes.ok:
		logging.debug('Looks good, proceeding')
		return r.text
	else
		logging.error('Looks bad, stopping')
		sys.exit("Fatal error with downloading")

def parser():
	# Take the various meta lists and lists and concatenate and deduplicate

	# Download the meta lists
	downloader(meta_block_url)
	if meta_allow_url:
		downloader(meta_allow_url)
	elif allow_url:
		# skip to list processor?
	# Download from the list
	for entry in list:
		# Grab the contents and shove them into a list object
		downloader(entry)

def processor(output):
	# Turn the list objects from the various URLs into output useable by DNS
	# 


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
