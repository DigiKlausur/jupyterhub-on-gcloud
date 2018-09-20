import grp
import pwd
import os
import argparse
from distutils import dir_util

#from "/etc/jupyter/nbgrader_config.py" import *

parser = argparse.ArgumentParser()
parser.add_argument('--assignment_id', default='', help='Assignment id')
parser.add_argument('--student_id', default='', help='Student id')
parser.add_argument('--student_group', default='mrc-student-group', help='Student group name')
parser.add_argument('--student_fb_dir', default='feedback', help='Student feeback directory')

FLAGS = parser.parse_args()
ASSIGNMENT_ID = FLAGS.assignment_id
STUDENT_ID = FLAGS.student_id
STUDENT_GROUP = FLAGS.student_group
STUDENT_FB_DIR = FLAGS.student_fb_dir

course_name = "mrc"
course_id = "mrc-ws1819"
course_root = "/home/mrc-grader/mrc/mrc-ws1819"
submitted_dir = "submitted"
autograded_dir = "autograded"
release_dir = "release"

def add_group(group_name, system_group=False, gid=None):
    """Add a group to the system

    Will log but otherwise succeed if the group already exists.

    :param str group_name: group to create
    :param bool system_group: Create system group
    :param int gid: GID for user being created

    :returns: The password database entry struct, as returned by `grp.getgrnam`
    """
    try:
        group_info = grp.getgrnam(group_name)
        log('group {0} already exists!'.format(group_name))
        if gid:
            group_info = grp.getgrgid(gid)
            log('group with gid {0} already exists!'.format(gid))
    except KeyError:
        log('creating group {0}'.format(group_name))
        add_new_group(group_name, system_group, gid)
        group_info = grp.getgrnam(group_name)
    return group_info 


# Check whether directory existance for submitted, autograded and feedback
# e.g. check if all student submitted assigments: check_dir_exist(submitted_dir, assignment_id)
# e.g. check if all student autograded assigments: check_dir_exist(autograded_dir, assignment_id)
def check_dir_exist(directory, assignment_id):
    print "Checking all submissions..."
    for student in group.gr_mem:    
        if not os.path.exists(os.path.join(course_root, directory, student, assignment_id)):
            print directory,"or", assignment_id, " does not exist"
            return False
        else:
            print os.path.join(course_root, directory, student, assignment_id), " exist..."
            return True

# Check feedback
# input: path to feedback directory
def check_and_release_feedback(course_root, feedback_dir, student, assignment_id):
    if os.path.exists(os.path.join(course_root, feedback_dir, student, assignment_id)):
        assignment_fb_dir = os.path.join(course_root, feedback_dir, student, assignment_id)
        # copy feedback to /home/student/feedback/assignment_id
        dir_util.copy_tree(assignment_fb_dir,
               os.path.join("/home", student, feedback_dir, assignment_id))
    else:
        print "Feedback not available for ", student
        print "Do nbgrader feedback assignment_id in terminal, check if the student submitted the assignment"	

# dir_util makes sure the folder copied to dst
# if dst does not exist, it will create one
# Perform a recursive copy from src to dst
def release_feedback(assignment_id, student_id, feedback_dir, student_group):  
    if student_id == "":
        for student in student_group:
            # feedback
            # TODO
            # Check and release all feedback present in the course feedback dir
            check_and_release_feedback(course_root, feedback_dir, student, assignment_id) 
    else:
        # TODO
        # release fb to student_id only
        check_and_release_feedback(course_root, feedback_dir, student_id, assignment_id)

def main():
    if ASSIGNMENT_ID == "":
	    print "Please specify assignment id"
	    return
    
    if STUDENT_ID == "":
	    print "No student_id specified, will be applied to all students if the feedbacks exist in the course dir"
    
    if STUDENT_GROUP == "":
	    print "No student group specified" 
    group = grp.getgrnam('mrc-student-group')
    #print "Group data: ", group
    student_group = group.gr_mem
    release_feedback(ASSIGNMENT_ID, STUDENT_ID, STUDENT_FB_DIR, student_group)
    
if __name__ == '__main__':
    main()    
#release_feedback()

#check_dir_exist(feedback_dir, "ps1")

#print get_course_detail()
