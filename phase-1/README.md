# Python CLI Todo Application
“This project was built using Spec-Driven Development.
No manual code was written.”
A simple command-line todo list manager with in-memory storage.

## Features

- **Add tasks**: Create new tasks with descriptions
- **List tasks**: View all tasks or filter by completion status
- **Update tasks**: Modify task descriptions
- **Complete tasks**: Mark tasks as completed
- **Delete tasks**: Remove tasks from the list

## Installation

No installation required. Just ensure you have Python 3.7+ installed.

## Usage

### Basic Commands

#### Add a Task
```bash
python src/main.py add <description>
```

Example:
```bash
python src/main.py add Buy groceries
python src/main.py add "Write documentation"
```

#### List Tasks
```bash
python src/main.py list [--all]
```

- Without `--all`: Shows only pending tasks
- With `--all`: Shows all tasks including completed ones

Example:
```bash
python src/main.py list
python src/main.py list --all
```

#### Update a Task
```bash
python src/main.py update <task_id> <new_description>
```

Example:
```bash
python src/main.py update 1 "Buy groceries and cook dinner"
```

#### Complete a Task
```bash
python src/main.py complete <task_id>
```

Example:
```bash
python src/main.py complete 1
```

#### Delete a Task
```bash
python src/main.py delete <task_id>
```

Example:
```bash
python src/main.py delete 1
```

### Help
```bash
python src/main.py --help
python src/main.py <command> --help
```

## Testing

Run the comprehensive test suite:
```bash
python test_todo.py
```

This will demonstrate all features of the application in a single session.

## Implementation Details

### Architecture
- **Task Class**: Represents individual tasks with ID, description, completion status, and timestamps
- **TodoManager Class**: Manages the task collection with methods for all CRUD operations
- **CLI Interface**: Uses Python's argparse for command-line argument parsing

### Data Storage
Tasks are stored in memory (using Python dictionaries) and persist only during the execution of the application. This is intentional as per the requirements. For persistent storage, you would need to add file or database integration.

### Task Format
Tasks are displayed with the following format:
```
[X] 1. Task description  # Completed task
[ ] 2. Task description  # Pending task
```

## Project Structure
```
todo-phase-1/
├── src/
│   └── main.py          # Main application entry point
├── specs/
│   └── features/        # Feature specifications
├── test_todo.py         # Comprehensive test suite
├── CLAUDE.md            # Project instructions
└── README.md            # This file
```

## Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Features Implemented

All features from `/specs/features` have been implemented:
- ✓ add-task
- ✓ list-tasks
- ✓ update-task
- ✓ delete-task
- ✓ complete-task

## Notes

- Task IDs are automatically assigned starting from 1
- Each command runs as a separate process, so tasks are reset between CLI invocations
- Use the test script (`test_todo.py`) to see all features working together in a single session
- Error messages are sent to stderr for proper error handling
- The application uses ASCII characters for compatibility across different terminal types
