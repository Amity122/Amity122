from . import auth
from flask import render_template
from WebApp.models import Colleges, Students, Courses


@auth.route('/')
def home_page():
    college_table = Colleges.query_filter(
        all=True, order_by='college_code', order='DESC')
    course_table = Courses.query_filter(
        all=True, order_by='course_code', order='DESC')
    student_table = Students.query_filter(
        all=True, order_by='id', order='DESC')
    return render_template('home/home.html', college_table=college_table, course_table=course_table, student_table=student_table)
