from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dictionary variable
students = {}

class Student(BaseModel):
    name: str
    age: int
    course: str

@app.post("/student")
async def create_student(student: Student):

    students[student.name] = {
        "age": student.age,
        "course": student.course
    }

    return {
        "message": "Student Created Successfully",
        "students": students
    }