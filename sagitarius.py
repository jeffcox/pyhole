#! /usr/bin/env python3

# Core script.


# Imports
import yaml
import os

# Variables
actiontype = "allow"
url = "https://google.com"
options = "pgl.yoyo.org"
listfile = "foob"
frmat = "unbound"
lists = "Tuple of domains from config"


# File paths

# Fancy output for interactive mode


def output_mode():
    print("Detecting output")
    return


# Check the config file


def load_config():
    print("Loading config")
    if os.path.isfile("config.yml"):
        try:
            config_file = file('config.yml', r)
            yaml.safe_load(config_file)
        except:
            print("Could not load config file.")
    else:
        new_config()
    return


# First run/no config, create one


def new_config():
    print("Welcome, new config being created")
    return


# Build the individual lists defined in config, color specifies allow/block


def build_lists(actiontype):
    print("Building lists")
	for x in lists:
        dloptions(lists[x])
        get_list(lists[x], options)
    return

# Download lists


def get_list(url, options):
    print("Downloading list from ", url, " using options, ", options)
    return


# Set download options


def dl_options(url):
    print("Option has been chosed based on things")
    return


# Parse the files


def list_parser(listfile, frmat):
    print("Parsing list into format")
    return


# Combine the files


def combine_lists():
    print("Combining lists")
    return


# Sort and deduplicate the lists


def sort_dedup():
    print("Sorting and deduplicating the combined lists")
    return


# Compare the lists and take treat appropriately


def contrast(frmat):
    print("Contrasting allow and block lists, depending on format?")
    return


# Check stats


def count_list():
    print("Counting a list")
    return


# Cleanup


def bruiser():
    print("Sweeping the streets")
    return


# 3, 2, 1, let's jam


output_mode()


load_config()


build_lists()


list_parser(listfile, frmat)


combine_lists()


sort_dedup()


contrast(frmat)


count_list()


bruiser()
