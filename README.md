# School Interface Three

## Release 0: Adding A Student 

Let's make it so our user can add student information to our database. We'll need to do a few things here. First, we'll have to add a new case to our case statement. 

```Ruby
# runner.rb

case mode 
when '1'
    school.list_students
when '2'
    puts 'Enter student id:'
    puts school.find_student_by_id(gets.chomp)          
when '3'
     school.add_student(student_data)
when '5' 
    return 
end  
```

Just like before we call a method that we have not defined yet. This method should take a hash containing all the data to make a new student object. From here we need to do two things. First, we need to ask the user for the student's name, age, student_id number, and password. We need to put those values in a hash and then pass that hash to our method. We can do this with multiple `gets.chomp` calls. 

```Ruby
# runner.rb

when '3'
    new_student = {role: 'Student'}
        
    puts "Enter name:\n"
    new_student[:name] = gets.chomp 
    puts "Enter age:\n"
    new_student[:age] = gets.chomp 
    puts "Enter school_id:\n"
    new_student[:school_id] = gets.chomp 
    puts "Enter password:\n"
    new_student[:password] = gets.chomp 

    school.add_student(new_student)
when '5' 
```
Wow, our switch statement is getting pretty crowded. We'll refactor it in release 3. For now, let's finish up the functionality for this feature by going into our school class and writing our `add_student` method. This method will need to create a new instance of a student object and add it to `@students` instance variable. When you're done, run the program. Enter some test data when prompted. Next, choose the option to list all the students. You should see the test student you entered listed at the bottom. 


## Release 1: Saving Data 

You may have noticed a huge problem with our program. Yes, we can add students, but once we exit, all that data is lost! We need to write a separate method in our school class that saves all instances of `Student` in our `@students` variable for us. Then we can call it at the end of `add_student`. 

```Ruby
# school.rb 
def add_student 
    # your code to add a student to instance of the class... 
    save_students 
end 
```
Write a method `save_students` in the school class that loops through `@students` and saves each object as a row in the `CSV` file.

##### Note: 
You may be asking, why are we re-saving every single object instead of just the new one we created. If so, read on. If you don't care, skip to the next section. There are a few reasons. One, yes we can append a line to a `CSV` file, but later, when we want to delete rows, removing a line from say, the middle of the file, is a little trickier. It involves getting a little deeper into the `CSV` class than is necessary for this tutorial. By writing our method this way will allow us to reuse it when we implement our `delete_student` method. 

Check out the `CSV` module in the Ruby docs. Make sure you are saving the file with headers. HINT(The headers are just the first row of data in the `CSV` file.) I recommend making a copy of the `student.csv` file to use while you test as it is very easy to erase all the data while you are working out your method. 

When you are done, make sure you add the method call to the end of `add_student`. Now every time a new student is added to the `@students` array, it will also get saved to our `CSV` file. Test this feature by adding a new student, exiting the program, and then running it again to see if the data persisted. You can also see the row get added in your `CSV` file. 

## Release 2: Deleting Records  

The last feature we need to implement is the ability to delete a student record. Follow the same procedure as before. First, add a case to the case statement. What information will you need from the user in order to delete a record? How will you get it and pass it to your method? Then, in `school.rb` define a method `delete_student`. How can you use the `save_student` method to help you out here? 




