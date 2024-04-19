#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:23:27 2023

@author: yuchen
"""

# import required module
import os
# assign directory
directory = '___Your_folder_path_contains_all_PDFs_need_deidentified___'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
