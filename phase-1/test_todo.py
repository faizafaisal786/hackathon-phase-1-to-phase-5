#!/usr/bin/env python3
"""
Test script to demonstrate the Todo CLI application functionality.
"""

import sys
sys.path.insert(0, 'src')

from main import TodoManager

def test_todo_app():
    """Test all todo application features."""
    print("=" * 60)
    print("Python CLI Todo Application - Test Demo")
    print("=" * 60)
    print()

    # Create a new todo manager
    todo = TodoManager()

    # Test 1: Add tasks
    print("1. ADDING TASKS")
    print("-" * 60)
    task1 = todo.add_task("Buy groceries")
    print(f"[+] Added: {task1}")

    task2 = todo.add_task("Write documentation")
    print(f"[+] Added: {task2}")

    task3 = todo.add_task("Fix bugs in the code")
    print(f"[+] Added: {task3}")
    print()

    # Test 2: List tasks
    print("2. LISTING ALL TASKS")
    print("-" * 60)
    tasks = todo.list_tasks()
    for task in tasks:
        print(f"  {task}")
    print()

    # Test 3: Complete a task
    print("3. COMPLETING TASK #1")
    print("-" * 60)
    if todo.complete_task(1):
        print(f"[+] Task 1 marked as completed")
    print()

    # Test 4: List tasks after completion
    print("4. LISTING TASKS (AFTER COMPLETION)")
    print("-" * 60)
    tasks = todo.list_tasks()
    for task in tasks:
        print(f"  {task}")
    print()

    # Test 5: Update a task
    print("5. UPDATING TASK #2")
    print("-" * 60)
    if todo.update_task(2, "Write comprehensive documentation with examples"):
        print(f"[+] Task 2 updated successfully")
        updated_task = todo.get_task(2)
        print(f"  New description: {updated_task.description}")
    print()

    # Test 6: List tasks after update
    print("6. LISTING TASKS (AFTER UPDATE)")
    print("-" * 60)
    tasks = todo.list_tasks()
    for task in tasks:
        print(f"  {task}")
    print()

    # Test 7: Delete a task
    print("7. DELETING TASK #3")
    print("-" * 60)
    if todo.delete_task(3):
        print(f"[+] Task 3 deleted successfully")
    print()

    # Test 8: Final task list
    print("8. FINAL TASK LIST")
    print("-" * 60)
    tasks = todo.list_tasks()
    for task in tasks:
        print(f"  {task}")
    print()

    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    print(f"Total: {total} | Completed: {completed} | Pending: {total - completed}")
    print()

    # Test 9: Test error handling
    print("9. ERROR HANDLING TEST")
    print("-" * 60)
    if not todo.complete_task(999):
        print("[-] Correctly handled non-existent task #999")
    if not todo.update_task(999, "Test"):
        print("[-] Correctly handled update of non-existent task #999")
    if not todo.delete_task(999):
        print("[-] Correctly handled delete of non-existent task #999")
    print()

    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)


if __name__ == '__main__':
    test_todo_app()
