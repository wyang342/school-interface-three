require_relative 'student'
require_relative 'staff'

class School
    attr_reader :name, :students, :staff

    def initialize(name, address = nil)
        @name = name 
        @address = address   
        @students = Student.all
        @staff = Staff.all  
    end   
    
    def list_students
        students.each_with_index { |s , i| puts "#{i + 1}. #{s.name} #{s.school_id}\n" }
    end 

    def find_student_by_id(id)
        students.find { |student| student.school_id == id}
    end 
end 

