import grp
import pwd
import os
import argparse
from distutils import dir_util

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

course_root = './'
submitted_dir = "submitted"
autograded_dir = "autograded"
release_dir = "release"
feedback_dir = "feedback"

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

# input: course_root, feedback_dir, student_id, assignment_id
# Copy feedback to student home directory
def check_and_release_feedback(course_root, feedback_dir, student, assignment_id):
    if os.path.exists(os.path.join(course_root, feedback_dir, student, assignment_id)):
        assignment_fb_dir = os.path.join(course_root, feedback_dir, student, assignment_id)
        student_fb_dir =  os.path.join("/home", student, feedback_dir, assignment_id)
        # copy feedback to /home/student/feedback/assignment_id
        dir_util.copy_tree(assignment_fb_dir,student_fb_dir)
        print ("src: ",assignment_fb_dir)
        print ("des: ",student_fb_dir)
        print ("======Done returning feedback to : {} ======".format(student_fb_dir))
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print "Feedback not available for ", student
        print "Do <nbgrader feedback assignment_id> in terminal and check if the student submitted the assignment"	
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# If student_id is not specified, release feedback to all students
def release_feedback(assignment_id, student_id, feedback_dir, student_uname_list):  
    if student_id == "":
        for student in student_uname_list:
            check_and_release_feedback(course_root, feedback_dir, student, assignment_id) 
    else:
        # release fb to student_id only
        check_and_release_feedback(course_root, feedback_dir, student_id, assignment_id)

def main():
    if ASSIGNMENT_ID == "":
	    print "Please specify assignment id"
	    return
    
    if STUDENT_ID == "":
	    print "No student_id specified, will be applied to all students if the feedbacks exist in the course dir"
    
    student_uname_list = os.listdir(os.path.join(course_root,feedback_dir))
    release_feedback(ASSIGNMENT_ID, STUDENT_ID, STUDENT_FB_DIR, student_uname_list)
    
if __name__ == '__main__':
    main()    
