import grp
import pwd
import os
#from "/etc/jupyter/nbgrader_config.py" import *

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

course_name = "mrc"
course_id = "mrc-ws1819"
course_root = "/home/mrc-grader/mrc/mrc-ws1819"
feedback_dir = "feedback"
submitted_dir = "submitted"
autograded_dir = "autograded"
release_dir = "release"
assignment_id = "ps1"
group = grp.getgrnam('mrc-student-group')
print "Group data: ", group
print group.gr_name
print group.gr_mem

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

# dir_util makes sure the folder copied to dst
# if dst does not exist, it will create one
from distutils import dir_util
# Perform a recursive copy from src to dst
def release_feedback():
    for student in group.gr_mem:
	# feedback
	if os.path.exists(os.path.join(course_root, feedback_dir, student, assignment_id)):
	    assignment_fb_dir = os.path.join(course_root, feedback_dir, student, assignment_id)
	    # copy feedback to /home/student/feedback/assignment_id
	    dir_util.copy_tree(assignment_fb_dir,
			   os.path.join("/home", student, feedback_dir, assignment_id))	
	
        # check the existance of student feedback
	#if os.path.exists(os.path.join("/home", student, course_id, assignment_id, feedback_dir)):
	#    print "fb folder exist"
	#else:
	#    print "fb folder doesnot exist"

release_feedback()

#check_dir_exist(feedback_dir, "ps1")

#print get_course_detail()
