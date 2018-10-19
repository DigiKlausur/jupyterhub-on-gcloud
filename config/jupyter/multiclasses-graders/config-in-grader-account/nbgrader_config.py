# Configuration file for nbgrader.
c = get_config()
course_account = 'wus'
course_name = 'WahrscheinlichkeitstheorieUndStatistik'
course_id = 'WuS-Notebooks'
c.CourseDirectory.root = '/home/{}/{}/{}'.format(course_account, course_name, course_id)
c.Exchange.course_id = course_id
c.Exchange.root = '/srv/nbgrader/exchange'

