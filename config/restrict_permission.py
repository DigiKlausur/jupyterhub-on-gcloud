import subprocess
import grp
import pwd
import os

#subprocess.call(["rm", "test.txt"])

# limit user access in a group to their own home dir
def restric_group_from_dirs(group_name, parent_dir):
    group = grp.getgrnam('mrc-student-group')
    print group.gr_name
    print group.gr_mem
    users = os.listdir(parent_dir)
    for student in group.gr_mem:
	for user in users:
	    if student == user:
		print student, user
	    else:
		subprocess.call(["setfacl", "--modify", "group:{}:0".format(group_name),os.path.join(parent_dir, user)])
    		print group_name, " is restricted from accessing ", os.path.join(parent_dir, user)

#def main():
#    restric_group_from_dirs("mrc-student-group", ["/etc"])

if __name__ == '__main__':
    # make these all params as args
    parent_dir = "/home"
    group_name = "mrc-student-group"
    restric_group_from_dirs(group_name, parent_dir)  



