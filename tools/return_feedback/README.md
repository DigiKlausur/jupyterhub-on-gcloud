* Return feedback
  * Copy return feedback to the root of the course directory
  * Return all feedback for WuS-01 to all users
    * sudo python return_feedback.py --assignment_id=WuS-01
  * Return a feedback for WuS-01 assignment to mwasil2s
    * sudo python return_feedback.py --assignment_id=WuS-01 --student_id=mwasil2s 
* Set permission of student home directory to read only
  * This permision setting is meant for Einsicht in elektronische Klausuren, where students are allowed to see the correct answer after the exam.
  * How to?
    * Set readonly for WuS-01 assignment for ALL wus students (wus- is the prefix of the username)
      * sudo python set_assignment_dir_to_read_only.py --assignment_id=WuS-01 --username_prefix=wus
    * Set readonly for WuS-01 assignment for a single wus student (wus-mwasil2s) --> wus- prefix is still required
      * sudo python set_assignment_dir_to_read_only.py --assignment_id=WuS-01 --username_prefix=wus --student_id=wus-mwasil2s
