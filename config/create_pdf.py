import subprocess
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--assignment', default='all', help='Specify which assignment, otherwise all will be generatd')
FLAGS = parser.parse_args()
ASSIGNMENT = FLAGS.assignment

fb_dir = './feedback'
students = os.listdir(fb_dir)

def generate_pdf(fb_dir, student, assignment):
    html_file = os.path.join(fb_dir, student, assignment, assignment)
    if os.path.exists(html_file+".html"):
        print (html_file+".html")
        subprocess.call(["xvfb-run", "wkhtmltopdf", html_file+".html", html_file+".pdf"])
        print ("pdf for", student, assignment, "created")
    else:
        print ("ERROR")
        print ("html feedback does not exist, ",student," might not submit ", assignment," or feedback has not been generated")

def main():
    if ASSIGNMENT=="all":
        print ("Assignment id not specified, will generate pdfs for all ssignments")
    
    for student in students:
        assignments = os.listdir(os.path.join(fb_dir, student))
        #print (assignments)
        for assignment in assignments:
            if ASSIGNMENT == "all":
                generate_pdf(fb_dir, student, assignment)
            else:
                generate_pdf(fb_dir, student, ASSIGNMENT)

if __name__ == '__main__':
    main()
