require_relative './classes/school.rb' 

school = School.new('Ridgemont High', '1212 Main st.')

mode = nil 
until mode == '5'
    puts "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit"

    mode = gets.chomp
    puts '' 
    case mode 
    when '1'
        school.list_students
    when '2'
        puts 'Enter student id:'
        puts school.find_student_by_id(gets.chomp)          
    when '5' 
        return 
    end  
end 