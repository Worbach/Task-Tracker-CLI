# 📝 To-Do List CLI Tool

A simple Python command-line interface (CLI) application that helps users manage a to-do list. Users can add tasks, mark them as complete, unmark them, and view both current and completed tasks.

## 📌 Features

- ✅ Add new tasks
- ✔️ Mark tasks as completed
- ❌ Unmark completed tasks
- 📋 View current tasks
- 📁 View completed tasks
- 🚪 Quit the application

## 🛠️ Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Application

1. Save the script as `todo.py` or any filename of your choice.
2. Open your terminal or command prompt.
3. Run the script using:

```bash
python todo.py
```
## 🧑‍💻 Usage
Once the program starts, you’ll be prompted with a menu of actions:

====== To-Do-List CLI tool ======
1. Add task
2. Mark task complete
3. Un-mark task complete
4. View current tasks
5. View completed tasks
6. Quit
Just enter the number corresponding to the action you want to perform.

### Example
Enter a number corresponding to your choice: 1
Enter a new task: buy groceries
'buy groceries' added successfully

## 🗂️ File Structure

todo.py         # Main Python script containing the CLI logic

### 🧾 Notes
All task inputs are converted to lowercase for consistency.

There is no data persistence — tasks are lost once the program exits.

## 🚀 Possible Future Improvements
Add file-based or database persistence

Include due dates and priorities

Improve task selection (e.g., via number/index instead of name)

Add edit and delete functionality