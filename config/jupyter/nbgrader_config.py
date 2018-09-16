# Some functions

def get_db_students():    
    db = [dict(id="student1", first_name="Ben", last_name="Bitdiddle"),
    dict(id="student2", first_name="Alyssa", last_name="Hacker"),
    dict(id="student3", first_name="Louis", last_name="Reasoner")]
    return db

# create a function for sharing course detail
def get_course_detail():
    return [course_name, course_id] 


# Configuration file for nbgrader.
c = get_config()
course_name = 'mrc'
course_id = 'mrc-ws1819'
c.CourseDirectory.root = '/home/mrc-grader/{}/{}'.format(course_name, course_id)
c.Exchange.course_id = course_id
c.Exchange.root = '/srv/nbgrader/exchange'

# config for multiple classes
#c.Exchange.path_includes_course = True

c.CourseDirectory.feedback_directory = 'feedback'

# add student database here
c.CourseDirectory.db_students = get_db_students()


