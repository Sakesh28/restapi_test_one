from flask import Flask,jsonify

todo=Flask('__name__')

students = [
        {
            'id':1,
            'student_name': 'std1',
            'age': 20,
            'email' : 'std1@gmail.com'
        },
        {
            'id': 2,
            'student_name': 'std2',
            'age': 21,
            'email': 'hello@gmail.com'
        },
        {
            'id': 3,
            'student_name': 'std3',
            'age': 23,
            'email': 'std3@gmail.com'
        }

    ]

@todo.route('/students-list/restapi')
def students_list_restapi():
    import requests

    url = "https://demo-application-9txd.onrender.com/students-list"


    response = requests.request("GET", url)


    return response.json()

@todo.route('/student-list')
def student_list():
    return jsonify(students)



@todo.route('/student/get/<int:id>',methods=['GET'])
def student_id(id):
    student=next((student for student in students if student['id']==id),None)

    if student is None:
        return jsonify({'message': 'Student not found'}), 404

    return jsonify(student)



if __name__=='__main__':
    todo.run(
        debug=True
    )