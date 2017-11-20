#! /usr/bin/env python
import argparse 
import pickle
import subprocess
import sys

TASK_LIST = './later_task_list'
ARCHIVE = './archive_list'
def parserCmd(argv):
    """Argparser function.

       {ls, new, delete}
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    sp = parser.add_subparsers(
        dest='cmd',
        title='commands',
        description='Supported Commands.',
        help='Valid Commands, run <command> -h for detail.')

    ls = sp.add_parser(
        'ls',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help='List all tasks.')

    ls.add_argument(
        '--archive', action='store_true',
        help='Show all archived tasks.')

    sp.add_parser(
        'new',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help='Add new task')

    args = parser.parse_args(argv[1:])
    return args


def listAll(archive=False):
    """Print everything in queue."""
    if archive:
        with open('archive_list', 'rb') as source:
            lst = pickle.load(source)
        print 'Good job! You have finished {} tasks'.format(len(lst))
        for i,c in enumerate(lst, 1):
            print i,c
    else:
        with open('later_task_list', 'rb') as source:
            lst = pickle.load(source)
        if not len(lst):
            print 'Bingo! No task pending right now. Enjoy your life.'
            return 
        print 'You gotta do:'
        for task in lst:
            print task


def scheduleTask(user_option, task_content):
    """Schedule task and return the at output.

       Schedule a task using at command.
    """
    # TODO: Delete option 0 after test.
    legal_options = {0: 'now + 1 minute',
                     1: 'now + 2 hour',
                     2: 'tomorrow',
                     3: 'noon tomorrow',
                     4: '8:00 PM tomorrow'}
    cmd = './notify.sh,{},{},{}'
    task_cmd = cmd.format(legal_options[user_option], task_content, 'Diyi')
    proc = subprocess.Popen(task_cmd.split(','),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    _, stderr = proc.communicate()
    info = stderr.split('\n')[1].split()
    job_id = int(info[1])
    schedule_time = " ".join(info[2:])
    return job_id, schedule_time


def createNewTask():
    """Create a new task

       1. Interact with user to grab the task content
       2. Schedule the task
       3. Put the task record in file.
    """
    #TODO: Now the task content is not allowed to contain any coma
    # since I'm using coma as delimeter in schdule_task().
    # This need to be imporved.
    task_content = raw_input('Please input task:')
    options = {1: '2 Hours later',
               2: 'Tomorrow Evening',
               3: 'Tomorrow Morning',
               4: 'Tomorrow Afternoon'}

    print 'Please select task scheduled time:'
    for i, option in options.items():
        print '{}. {}'.format(i, option)
    while True:
        user_option = int(raw_input('Your Option:'))
        #TODO: Rerange schedule time from 1-4
        if not 0 <= user_option < 4:
            print 'Invalid Option'
            continue
        break

    task_id, schedule_time = scheduleTask(user_option, task_content)

    #TODO: Create an LaterTask object and put it in the queue.
    print('[{}] will be scheduled at {}'.format(task_content,
                                                schedule_time))
    task_list = pickle.load(TASK_LIST)


if __name__ == '__main__':
    args = parserCmd(sys.argv)
    if args.cmd == 'ls':
        listAll(args.archive)

    elif args.cmd == 'new':
        createNewTask()
    #TODO: Add a reset function with double check
