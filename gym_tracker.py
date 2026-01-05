#Import tkinter
import tkinter as tk

#Welcome the user to program on the console 
print("Thank you for choosing STAR FITNESS!")
print("Every member of our gym has the advantage to use this new gym software with NO ADDITIONAL FEES!")
print("\n*WELCOME TO STAR FITNESS*")

#Class GymGui 
#A class acts as a blurptint in order to create objects. It defines attributes & methods 
class GymGui:
  #Constructor 
  #The constructor is automatically called when a new object of a class is created 
  #self is the first argument when defining methods. It specifies the instance on which you call the method
  def __init__(self):
    #create main_window for the first set of questions using widgets to get user input
    self.main_window = tk.Tk()
    
    #Set title of the main_window - helps ensure user knows what the window's purpose 
    self.main_window.title("Star Fitness - User Portal")

    #Label to display promotional text for gym program (It is based off a software for an actual gym)
    self.starfitness_label = tk.Label(self.main_window,text="Welcome to Star Fitness!\n*All gym members can use this new software for free!*")
    
    #Place label in the main window at row 0 and column 2 
    #columnspan will make the widget cover 2 columns of grid 
    #pady adds 10 pixels of padding at the top & 20 at the bottom
    self.starfitness_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    #Create label widget in the main window for name of user
    self.name_label = tk.Label(self.main_window, text="Full Name:")
    #sticky refers to the side of the cell which the widget resides in. In this case, it would be east - right side of cell
    self.name_label.grid(row=1, column=0, sticky='e', pady=5) 

    #Create entry widget for user's name in main window 
    self.name_entry = tk.Entry(self.main_window, width=20)
    self.name_entry.grid(row=1, column=1, sticky='w', pady=5) #sticky w =left alignment of entry in cell

    #Create label widget in the main window for age of user
    self.age_label = tk.Label(self.main_window, text="Age:")
    self.age_label.grid(row=2, column=0, sticky='e', pady=5) #sticky e = right alignment of label widget in cell

    #Create entry widget for user's age in main window 
    self.age_entry = tk.Entry(self.main_window, width=5)
    self.age_entry.grid(row=2, column=1, sticky='w', pady=5) #sticky w = left alignment of entry widget in cell

    #Create label widget in the main window for height of user
    self.height_label = tk.Label(self.main_window, text="Height(cm):")
    self.height_label.grid(row=3, column=0, sticky='e', pady=5) #sticky e = right alignment of label widget in cell

    #Create entry widget for height of user in main window 
    self.height_entry = tk.Entry(self.main_window, width=5)
    self.height_entry.grid(row=3, column=1, sticky='w', pady=5) #sticky w = left alignment of entry widget in cell

    #Create label widget in the main window for weight of user
    self.weight_label = tk.Label(self.main_window, text="Weight:")
    self.weight_label.grid(row=4, column=0, sticky='e', pady=5) #sticky e = right alignment of label widget in cell

     #Create entry widget in the main window for weight of user
    self.weight_entry = tk.Entry(self.main_window, width=5)
    self.weight_entry.grid(row=4, column=1, sticky='w', pady=5, padx=0) #sticky w = left alignment of entry widget in cell

    #Initialize a StringVar to store the selected weight unit for radio button
    #special variable since it can be linked to other widgets(radiobuttons)
    self.weight_unit_var = tk.StringVar()
    self.weight_unit_var.set("lbs")  # Default selection of lbs

    #Create a radio button for lbs option for user's weight
    self.lbs_rbutton = tk.Radiobutton(self.main_window, text="lbs", variable=self.weight_unit_var, value="lbs")
    self.lbs_rbutton.grid(row=4, column=3, sticky='w', pady=5, padx=1) #sticky w = left alignment of radiobutton widget in cell

    #Create a radio button for kg option for user's weight
    self.kg_rbutton = tk.Radiobutton(self.main_window, text="kg", variable=self.weight_unit_var, value="kg")
    self.kg_rbutton.grid(row=4, column=2, sticky='w', pady=5, padx=2) #sticky w = left alignment of radiobutton widget in cell

    #Create label widget in the main window for name of user
    self.goals_label = tk.Label(self.main_window, text="Fitness Goals:")
    self.goals_label.grid(row=5, column=0, sticky='e', pady=5)#sticky e = right alignment of label widget in cell
    
    self.goals_entry = tk.Entry(self.main_window, width=20)
    self.goals_entry.grid(row=5, column=1, sticky='w', pady=5)#sticky w = left alignment of entry widget in cell

    #add a button for user to enter information which leads to the command enter
    self.enter_button = tk.Button(self.main_window, text="Enter", width=8, command=self.enter)
    self.enter_button.grid(row=6, column=0, columnspan=2, pady=(10, 20)) #pady adds 10 pixels of padding at the top & 20 at the bottom

  #Method/command for enter button
  def enter(self):
    
    # Create a new window for displaying workout information
    self.workout_window = tk.Tk()
    self.workout_window.title("Workout Information Portal")#title of new window 

    #Create label for introduction of gym appilcation - implemented to make code more user friendly 
    self.program_label = tk.Label(self.workout_window, text="Make your own workout program!\nCongratulations on taking the first step towards a healthy lifestyle! ")
    self.program_label.grid(row=0, column=0, columnspan=2, pady=(10, 20)) #label alignment on grid 

    #Create label widget in the workout window for name of user
    self.workout_name_label = tk.Label(self.workout_window, text="Name of Workout File:")
    self.workout_name_label.grid(row=1, column=0, sticky='e', pady=5)#label alignment on grid

    #Create entry widget in the workout window for name of user
    self.workout_name_entry = tk.Entry(self.workout_window, width=15)
    self.workout_name_entry.grid(row=1, column=1, sticky='w', pady=5)#entry widget alignment on grid

    #Create label widget in the workout window for date of workout
    self.date_label = tk.Label(self.workout_window, text="Date of Workout (d-m-y):")
    self.date_label.grid(row=2, column=0, sticky='e', pady=5)#label widget alignment on grid

    #Create label widget in the workout window for date of workout
    self.date_entry = tk.Entry(self.workout_window, width=15)
    self.date_entry.grid(row=2, column=1, sticky='w', pady=5)#entry widget alignment on grid

    #Create exercise frame in the workout window 
    self.exercise_frame = tk.Frame(self.workout_window)
    self.exercise_frame.grid(row=3, column=0, columnspan=2, pady=5)#frame alignment on grid

    #Create label widget in the workout window for name of user
    self.exercises_label = tk.Label(self.exercise_frame, text="Exercises:")
    self.exercises_label.grid(row=0, column=0, sticky='e', pady=5)#label alignment on grid

    #make a list for the entries of exercises 
    self.exercise_entries = []

    #create button to add exercise on the window for user to enter more input
    self.add_exercise_button = tk.Button(self.exercise_frame, text="Add Exercise", command=self.add_exercise)
    self.add_exercise_button.grid(row=0, column=2, pady=5)#alignment of button on grid

    #create button to add workout to the file for user
    # The parameter of command uses a lambda function to pass the result of max_weight_used and get_best_set_ratio as arguments to get_input
    self.add_to_file = tk.Button(self.workout_window, text="Add to File", command=lambda:self.get_input(self.max_weight_used(),*self.get_best_set_ratio()))
    self.add_to_file.grid(row=4, column=0, columnspan=2, pady=(10, 20))#alignment of button on grid

    #Create done button to go to the summary window and command for done button is done function
    self.done_btn = tk.Button(self.workout_window, text="Done", command=self.done)
    self.done_btn.grid(row=5, column=0, columnspan=2, pady=(10, 20))#alignment of button on grid

    #Hide main window when workout window is created 
    #The withdraw() method is a part of tkinter library 
    self.main_window.withdraw()

  #Method for done button 
  def done(self):
    #Create summary window 
    self.summary_window = tk.Tk()
    #Make the title of window 
    self.summary_window.title("Workout Summary Portal")

    #Get all the user input form the GUI widgets 
    full_name = self.name_entry.get() #Get full name of user 
    age = self.age_entry.get() #Get age of user 
    height = self.height_entry.get() #Get height of user 
    fitness_goals = self.goals_entry.get() #Get fitness goals of user 
    workout_name = self.workout_name_entry.get() #Get workout file name 
    date = self.date_entry.get()#get date of workout
    exercises_list = self.get_exercises()#get list of exercises added by user 

    #store the output to user in a variable called output 
    output = "\nName: "+ full_name+ "\nAge:"+age+"\nHeight:" + height+"\nGoals:" + fitness_goals
    #Summary label to display output based on user's input 
    summary_label = tk.Label(self.summary_window, text=("Your Workout Summary"+output))
    summary_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))#alignment of label widget on grid 

    #Hide workout window when workout window is created 
    #The withdraw() method is a part of tkinter library 
    #I haven't tried using withdraw method before which is why i used it here, it also retains its state for potential use if I wanted to remake the GUI window
    self.workout_window.withdraw()

  #Method to add exercises to window when user requires (good for control over how many exercises user is inputting)
  def add_exercise(self):
    exercise_frame = tk.Frame(self.exercise_frame) #create frame for exercises 
    exercise_frame.grid(row=len(self.exercise_entries) + 1, column=0, columnspan=2, pady=5) #grid for the alignemnt of future widgets 

    #Create label for exercise name 
    exercise_name_label = tk.Label(exercise_frame, text="Exercise Name:")
    exercise_name_label.grid(row=0, column=0, sticky='e', pady=5) #sticky e = right alignment of widget in cell
    
   #Create entry for exercise name 
    exercise_name_entry = tk.Entry(exercise_frame, width=15)
    exercise_name_entry.grid(row=0, column=1, sticky='w', pady=5)#sticky w = left alignment of widget in cell
    
    #Create label for reps
    sets_reps_label = tk.Label(exercise_frame, text="Sets/Reps:")
    sets_reps_label.grid(row=0, column=2, sticky='e', pady=5)#sticky e = right alignment of widget in cell

    #Create entry for reps
    sets_reps_entry = tk.Entry(exercise_frame, width=10)
    sets_reps_entry.grid(row=0, column=3, sticky='w', pady=5)#sticky w = left alignment of widget in cell

    #Create label for weight of exercise used
    weight_label = tk.Label(exercise_frame, text="Weight(lbs):")
    weight_label.grid(row=0, column=4, sticky='e', pady=5)#sticky e = right alignment of widget in cell
    
    #Create entry for weight of exercise used 
    weight_entry = tk.Entry(exercise_frame, width=5)
    weight_entry.grid(row=0, column=5, sticky='w', pady=5)#sticky w = left alignment of widget in cell

    #to append is it add an element/data at the end of a data structure (in this case it is a dictionary)
    #A dictionary is a collection of key value pairs, it lets us store & retrive data by using a key (similar to index in a list). 
    #Dictionaries are an efficient way to organize, retrieve and manipulate data
    self.exercise_entries.append({
      'exercise_name': exercise_name_entry, 
      'sets_reps': sets_reps_entry,
      'weight': weight_entry }) #exercise_name, sets_reps and weight are keys and beside them are the values (user input)

  #Method to check to convert lbs into kg for user's weight 
  #The weight for exercises are not converted because they are most of the time used in the unit lbs 
  def to_kg(self, weight):
    if self.weight_unit_var.get() == "lbs": #check if weight unit var
      updated_weight = weight * 0.453592 #updated weight is the lbs * the conversion needed to be kg
      return updated_weight #return if radio button's value is lbs 
    else:
      return weight #return initial value of user's input for weight since it is kg already

  #Method to get the inputs of user and write them into the gym program file
  def get_input(self, max_weight, best_exercise, best_ratio):
    #Get user's input in the specific widgets 
    full_name = self.name_entry.get()#Get user's input for their name
    workout_name = self.workout_name_entry.get()#Get user's input for file name 
    date = self.date_entry.get()# Get user's input for date of workout
    exercises_list = self.get_exercises()# Get user's input for exercises

    # Get the entered weight from the user
    entered_weight = int(self.weight_entry.get())

    # Convert the entered weight to kg if the unit is in lbs
    weight = self.to_kg(entered_weight)

    #open a file using the name the user entered 
    with open(workout_name, 'a') as file:
      #Write user info to file and append content 
      file.write("Name: "f"{full_name}\n") #write user's full name into first line of file
      file.write("Weight of User: "f"{weight} kg\n")  # Added 'kg' to indicate the unit, add weight to 2nd line of file 
      file.write("Date of Workout: "f"{date}\n") #write date into thrid line of file
      file.write("Exercises: "f"{exercises_list}\n") #write exercises into fouth line of file
      file.write("Max Weight Used: "f"{max_weight}\n") #write max weight into file (method was used to get this)
      file.write("Best Ratio: "f"{best_ratio}\n") #write best ratio of file (method was used to get this)
      file.write("Best Exercise: "f"{best_exercise}") #write best exercise of file (method was used to get this)

  #Method to get the max weight used the the set of exercises entered by user 
  def max_weight_used(self):
    #initialize the variable to store max weight
    max_weight = 0
    #iterate through exercises enteried by user in the list
    for exercise in self.exercise_entries:
        #retrieve weight as string from entry
        weight_str = exercise['weight'].get()
        #Convert the weight string to an integer, default will be 0 if it cannot be convertible 
        weight = int(weight_str) if weight_str else 0
        #Check if current weight is greater than max weight 
        if weight > max_weight:
          #update it it is
            max_weight = weight
    return max_weight #return max weight (updated)

  #Method to get the best set ratio
  def get_best_set_ratio(self):
    #Initialize variables for best exercise & ratio
    best_exercise = None
    best_ratio = 0
    #go through/iterate each entry in the list of exercise inputs 
    for entry in self.exercise_entries:
        #retrieve sets & reps as string from exercise entry 
        sets_reps = entry['sets_reps'].get()
        #split sets and reps if "/" is present 
        #The map() function helps you apply a function to each item in a list and collect the results. 
        sets, reps = map(int, sets_reps.split('/')) if '/' in sets_reps else (sets_reps, '')
        #calculate ratio and aviod division by 0
        # If reps is not zero, it calculates the ratio normally. otherwise, it sets ratio to 0 to avoid errors.
        ratio = sets / reps if reps != 0 else 0
        #if ratio is greater than best_ration
        if ratio > best_ratio:
           #make that ratio the best
            best_ratio = ratio
            #best exercise is determined bt the best ratio method
            best_exercise = entry['exercise_name'].get()
    #return both values
    return best_exercise, best_ratio

  #Method to get exercises 
  def get_exercises(self):
    #initialize list to store details of exercises
    exercises_list = []
    #Iterate through entries in the list of exercises (inputted by user)
    for entry in self.exercise_entries:
      #Get the data from entries for exercise names
      exercise_name = entry['exercise_name'].get()
      #Get the data from entries for exercise sets & reps
      sets_reps = entry['sets_reps'].get()
      #Get the data from entries for exercise weight
      weight = entry['weight'].get()
      #split sets and reps if "/" is present 
      #The map() function helps you apply a function to each item in a list and collect the results. 
      # If the '/' is present in the string, it converts the split parts to integers and assigns them to the variables sets and reps
      #If there is no '/', it assigns the entire string to sets and an empty string to reps.
      sets, reps = map(int, sets_reps.split('/')) if '/' in sets_reps else (sets_reps, '')
      #append info to exercises list
      exercises_list.append({
        'exercise_name': exercise_name, #key & values for name
        'sets': sets, # key & value for sets
        'reps': reps, #key & value for reps
        'weight': weight}) #key & value for weight
    return exercises_list  # Moved the return statement outside the loop

#create an instance of GymGui class
#an instance is a concrete implementation of a class gui = GymGui()
#start tkinter main event loop 
tk.mainloop()
