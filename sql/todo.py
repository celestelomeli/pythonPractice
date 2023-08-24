import mysql.connector

# Establish database connection
db = mysql.connector.connect(
    host='localhost',
    user='celeste',
    password='password (must change)',
    database='todo_list'
)
 # Create cursor object to interact with database
cursor = db.cursor()

# function takes one parameter representing the name of the task to be added
def add_task(task_name):
    # Insert a new task into the database 
    sql = "INSERT INTO tasks (name, completed) VALUES (%s, %s)"
    # Tuple containing data to be inserted into placeholders
    values = (task_name, False)
    # Execute sql query
    cursor.execute(sql, values)
    # Commit changes to db
    db.commit()

# Retrieves and displays tasks from the db
def view_tasks():
    # Query retrieves all columns from tasks table
    cursor.execute("SELECT * FROM tasks")
    #tasks will be tuples (task_id, task_name, completed status)
    tasks = cursor.fetchall()

    #print out the tasks, iterate through each tuple in tasks list using for loop
    print("\nTasks:")
    # Tuple unpacking to assign elements of each tuple (task_id, task_name, completed) to separate variables
    for task_id, task_name, completed in tasks:
        #sets status variable based on value of completed field in tuple
        status = "Completed" if completed else "Not Completed"
        #print formatted information
        print(f"{task_id}. {task_name} - {status}")


#function updates a specific task in the database by marking it as completed
def mark_completed(task_id):
    # Query that updates tasks table
    sql = "UPDATE tasks SET completed = True WHERE id = %s"
    # Data to be inserted into %s placeholder of query
    values = (task_id,)
    cursor.execute(sql, values)
    db.commit()

def main():
    while True: 
         # Display the choices
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

          # Get user's choice
        choice = input("Enter your choice: ")

         # Process the user's choice
        if choice == "1":
             # Add Task
            task_name = input("Enter task name: ")
            add_task(task_name)
            print("Task added successfully!")

        elif choice == "2":
             # View Tasks
            view_tasks()

        elif choice == "3":
             # Mark Task as Completed
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
            print("Task marked as completed!")

        elif choice == "4":
                # Exit the loop
            break

        else:
               # Invalid choice
            print("Invalid choice")


    # Close the cursor and the database connection when complete
    cursor.close()
    db.close()

#check if the script is being run as the main program 
if __name__ == "__main__":
    main()

