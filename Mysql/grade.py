from sqlalchemy import Column, Integer, String, DateTime, Float
from base import Base
import datetime


class Grade(Base):
    """ Grade info """

    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    studentID = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    grade = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, studentID, name, grade):
        """ Initializes a grade reading """
        self.studentID = studentID
        self.name = name
        self.grade = grade
        self.date_created = datetime.datetime.now()
        

    def to_dict(self):
        """ Dictionary Representation of a grade reading """
        dict = {}
        dict['id'] = self.id
        dict['studentID'] = self.studentID
        dict['name'] = self.name
        dict['grade'] = self.grade
        dict['date_created'] = self.date_created


        return dict
