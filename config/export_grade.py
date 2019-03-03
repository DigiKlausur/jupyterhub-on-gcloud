import pandas as pd
from nbgrader.api import Gradebook, MissingEntry

# Complete list of student
complete_list = pd.read_excel('al-grundlagenvonwahrscheinlichkeitstheorieundstatistik.xls')
# Create the connection to the database

filter_grade = False
assignment_to_export = "WuS-midterm"
grader = 'ploeger'

def main():
	with Gradebook('sqlite:///midterm_gradebook/{}-gradebook.db'.format(grader)) as gb:
		grades = []
		# Loop over each assignment in the database
		for assignment in gb.assignments:
      if assignment.name == assignment_to_export:
        # Loop over each student in the database
        for student in gb.students:
          student_uid = None
          student_id = student.id.split("_")
          for split in student_id:
            if "2s" in split:
              student_uid = split
          student_matrikel_nummer = None
          for i,s_uid in enumerate(complete_list.UID):
            if s_uid == student_uid:
              student_matrikel_nummer = complete_list.Matrikel[i]		                    
              # Create a dictionary that will store information about this student's
              # submitted assignment
              # Try to find the submission in the database. If it doesn't exist, the
              # `MissingEntry` exception will be raised, which means the student
              # didn't submit anything, so we assign them a score of zero.
              score = {}
              try:
                submission = gb.find_submission(assignment.name, student.id)
              except MissingEntry:
                score['score'] = 0.0
              else:		                        
                if filter_grade:
                  score['student_matrikel'] = student_matrikel_nummer
                  score['score'] = submission.score
                  min_score = assignment.max_score / 2
                  if submission.score >= min_score:
                    #if submission.score != 0.0:
                    grades.append(score)
                else:
                  score['student'] = student.id
                  score['student_uid'] = student_uid
                  score['student_matrikel'] = student_matrikel_nummer
                  score['assignment'] = "WuS-midterm"
                  score['score'] = submission.score
                  score['max_score'] = assignment.max_score
                  grades.append(score)

		# Create a pandas dataframe with our grade information, and save it to disk
		if filter_grade:
		  grades = pd.DataFrame(grades).set_index(['student_matrikel','score']).sortlevel()
		else:
		  grades = pd.DataFrame(grades).set_index(['student','student_matrikel','student_uid', 'assignment']).sortlevel()
		
		csv_file = '{}-complete-grades.csv'.format(grader)
		grades.to_csv(csv_file)

		# Print out what the grades look like
		with open(csv_file, 'r') as fh:
		  print(fh.read())

if __name__ == '__main__':
    main()
