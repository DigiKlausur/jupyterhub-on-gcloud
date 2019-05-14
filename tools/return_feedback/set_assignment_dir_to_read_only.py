import os
import shutil
import pwd
import argparse
import stat

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--assignment_id', default='', help='Assignment id')
parser.add_argument('--student_id', default='', help='Student id')
parser.add_argument('--username_prefix', default='', help='Username prefix used in the system i.e. wus-..')

FLAGS = parser.parse_args()
ASSIGNMENT_ID = FLAGS.assignment_id
STUDENT_ID = FLAGS.student_id
USERNAME_PREFIX = FLAGS.username_prefix

'''
    Set permission of a directory to read only
'''
def set_permissions(path, uid, gid):
    os.chown(path, uid, gid)
    if os.path.isdir(path):
        os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IXUSR | stat.S_IXGRP)
    else:
        os.chmod(path, stat.S_IRUSR | stat.S_IRGRP)

'''
    Set assignment directory in student home to read only
    Input: assignment_id
           username_prefix
           student_id
'''
def main():
    if ASSIGNMENT_ID == "":
        print ("Please specify assignment id")
        return
    
    if USERNAME_PREFIX == "":
        print ("Please specify username_prefix, i.e. wus-, nn-")
        return
    
    if STUDENT_ID == "":
        print "No student_id specified, will be applied to all students if the feedbacks exist in the course dir"
    
    if STUDENT_ID == "":
        users = os.listdir("/home")
        username_prefix = str(USERNAME_PREFIX)
        for username in users:
            if username_prefix in username:
                assignment_path = os.path.join("/home",username,ASSIGNMENT_ID)
                if os.path.isdir(assignment_path):
                    pwinfo = pwd.getpwnam(username)
                    uid = pwinfo.pw_uid
                    gid = pwinfo.pw_gid
                    # Set permission to read only
                    set_permissions(assignment_path, uid, gid)
                    for dirname, dirnames, filenames in os.walk(assignment_path):
                        for f in (dirnames + filenames):
                            path = os.path.join(dirname, f)
                            set_permissions(path, uid, gid)
                    print ("===================")
                    print (assignment_path, "is read only now")
                    print ("===================")
                else:
                    print (assignment_path, "not found")
    else:
        assignment_path = os.path.join("/home",STUDENT_ID,ASSIGNMENT_ID)
        if os.path.isdir(assignment_path):
            pwinfo = pwd.getpwnam(STUDENT_ID)
            uid = pwinfo.pw_uid
            gid = pwinfo.pw_gid
            # Set permission to read only
            set_permissions(assignment_path, uid, gid)
            for dirname, dirnames, filenames in os.walk(assignment_path):
                for f in (dirnames + filenames):
                    path = os.path.join(dirname, f)
                    set_permissions(path, uid, gid)
            print ("===================")
            print (assignment_path, "is read only now")
            print ("===================")
        else:
            print (assignment_path, "not found")

if __name__ == '__main__':
    main()    