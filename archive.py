#!/usr/bin/env python
# Author: Diyi Wang (wang.di@husky.neu.edu)
#
# Archive the notified task.

import pickle
import sys

from util import add_to_list 
ARCHIVE = './archive_list'

if __name__ == '__main__':
    task_content = " ".join(sys.argv[1:])
    add_to_list(task_content, ARCHIVE)
