"""This is the util lib for Later App"""
import pickle

class LaterTask(object):
    """Later App Task class"""
    def __init__(self, task_id, time, content):
        self.task_id = task_id
        self.time = time
        self.content = content

    def __repr__(self):
        return '{}: {}, scheduled {}'.format(
            self.task_id, self.content, self.time)

def load_from_file(filename):
    """Helper function combines the open and pickle.load"""
    return pickle.load(open(filename, 'rb'))


def save_to_file(target_obj, filename):
    """Helper function combines the open and pickle.dump"""
    pickle.dump(target_obj, open(filename, 'wb'))


def add_to_list(list_item, filename):
    """Helper function to add an item to pickled list"""
    lst = load_from_file(filename)
    lst.append(list_item)
    save_to_file(lst, filename)
