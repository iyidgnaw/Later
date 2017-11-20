"""This is the common lib for Later App"""

class LaterTask(object):
    """Later App Task class"""
    def __init__(self, task_id, time, content):
        self.task_id = task_id
        self.time = time
        self.content = content

    def __repr__(self):
        return '{}: {}, scheduled {}'.format(
            self.task_id, self.content, self.time)
