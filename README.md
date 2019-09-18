# School Interface Three

## Release 0: Adding A Student 

Let's make it so our user can add student information to our database. We'll need to do a few things here. First, we'll have to add a new case to our if statement. 

```Python
# runner.py
if mode == '1':
    school.list_students()
elif mode == '2':
    student_id = input('Enter student id:')
    student = school.find_student_by_id(student_id)
    print(str(student))
elif mode == '3':  
    school.add_student(student_data)
elif mode == '5':
    break  
```

Just like before we call a method that we have not defined yet. This method should take a dictionary containing all the data to make a new student object. From here, we need to do two things. First, we need to ask the user for the student's name, age, student_id number, and password. Next, we need to put those values into a dictionary and then pass that dictionary to our method. We can do this with multiple `input()` calls. 

```Python
# runner.py

elif mode == '3':
    student_data = {'role':'student'}
    student_data['name']      = input('Enter student name:\n')
    student_data['age']       = input('Enter student age: \n')
    student_data['school_id'] = input('Enter student school id: \n')
    student_data['password']  = input('Enter student password: \n')
  
    school.add_student(student_data)
elif mode == '5':
    break
```
Wow, our if statement is getting pretty crowded. We'll refactor it in the next challenge. For now, let's finish up the functionality for this feature by going into our school class and writing our `add_student()` method. This method will need to create a new instance of a student object and add it to the `self.students` variable. When you're done, run the program. Enter some test data when prompted. Next, choose the option to list all the students. You should see the test student you entered listed at the bottom. 

## Release 1: Saving Data 

You may have noticed a huge problem with our program. Yes, we can add students, but once we exit, all that data is lost! We need to find a way to save that data to the `CSV` file. Write a new method `save_students()` that loops through all our student objects in `self.students` and saves them to the `CSV` file. Then we can call that method at the end of `add_student()`

```Python
# school.py 
def add_student(self):
    # your code to add a student to instance of the class... 
    self.save_students()
```

#### Note: 
You may be asking, why are we re-saving every single object instead of just the new one we created? There are a few reasons. One, yes we can append a line to a `CSV` file, but later, when we want to delete rows, removing a line from say, the middle of the file, is a little trickier. It involves getting deeper into the `CSV` module than is necessary for this tutorial. For the sake of simplicity, we are just going to write a method that overwrites the old data with the new data. It's not the most performative, but for a small app like this, it will do just fine.  

#### Write the `save_students` method 
Check out the `CSV` module in the Python 3 docs to help you. Make sure you are saving the file with headers. We are using these headers to set our keys when we read from `students.csv` to create student objects. If we don't have them, our app will break. HINT: The headers are just the first row of data in the `CSV` file. I recommend making a copy of the `students.csv` to use while you test as it is very easy to erase all the data while you are working out your method. 

When you are done, make sure you add the method call to the end of `add_student`. Now every time a new student is added to the `self.students` array, it will also get saved to our `CSV` file. Test this feature by adding a new student, exiting the program, and then running it again to see if the data persisted. You can also see the row get added in your `CSV` file. 

## Release 2: Deleting Records  

The last feature we need to implement is the ability to delete a student record. Follow the same procedure as before. First, add a condition to the if statement. What information will you need from the user in order to delete a record? How will you get it and pass it to your method? Then, in `school.py` define a method `delete_student()`. How can you use the `save_student()` method again to help you out here? 
