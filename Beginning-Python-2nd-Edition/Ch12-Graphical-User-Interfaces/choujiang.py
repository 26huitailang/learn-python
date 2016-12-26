#!/usr/bin/python
# coding: utf-8

import csv
import sys

with open('namelist.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for line in csv_reader:
        print line
