#!/usr/bin/env python
# Author: Diyi Wang (wang.di@husky.neu.edu)
#
# Archive the notified task.

import pickle
import sys

if __name__ == '__main__':
    task_content = " ".join(sys.argv[1:])
    with open('archive_list', 'rb') as source:
        archive_list = pickle.load(source)
    archive_list.append(task_content)
    with open('archive_list', 'wb') as source:
        pickle.dump(archive_list, source)
