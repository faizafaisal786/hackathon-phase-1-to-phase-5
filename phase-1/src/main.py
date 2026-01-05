#!/usr/bin/env python3
"""
Python CLI Todo Application
A simple command-line todo list manager with in-memory storage.
"""

import argparse
import sys
from typing import List, Dict, Optional
from datetime import datetime


class Task:
    """Represents a single task."""

    def __init__(self, task_id: int, description: str):
        self.id = task_id
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None

    def complete(self):
        """Mark task as completed."""
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self):
        status = "X" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"


class TodoManager:
    """Manages the todo list in memory."""

    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id = 1

    def add_task(self, description: str) -> Task:
        """Add a new task."""
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """List all tasks."""
        tasks = list(self.tasks.values())
        if not show_completed:
            tasks = [t for t in tasks if not t.completed]
        return sorted(tasks, key=lambda t: t.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, description: str) -> bool:
        """Update a task's description."""
        task = self.get_task(task_id)
        if task:
            task.description = description
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.get_task(task_id)
        if task:
            task.complete()
            return True
        return False


# Global todo manager instance
todo_manager = TodoManager()


def cmd_add(args):
    """Handle add command."""
    description = ' '.join(args.description)
    task = todo_manager.add_task(description)
    print(f"[+] Task added: {task}")


def cmd_list(args):
    """Handle list command."""
    tasks = todo_manager.list_tasks(show_completed=args.all)

    if not tasks:
        print("No tasks found.")
        return

    print(f"\n{'='*50}")
    print(f"{'TODO LIST':^50}")
    print(f"{'='*50}\n")

    for task in tasks:
        print(f"  {task}")

    print(f"\n{'='*50}")
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    print(f"Total: {total} | Completed: {completed} | Pending: {total - completed}")
    print(f"{'='*50}\n")


def cmd_update(args):
    """Handle update command."""
    description = ' '.join(args.description)
    if todo_manager.update_task(args.id, description):
        print(f"[+] Task {args.id} updated successfully.")
    else:
        print(f"[-] Error: Task {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args):
    """Handle delete command."""
    if todo_manager.delete_task(args.id):
        print(f"[+] Task {args.id} deleted successfully.")
    else:
        print(f"[-] Error: Task {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def cmd_complete(args):
    """Handle complete command."""
    if todo_manager.complete_task(args.id):
        print(f"[+] Task {args.id} marked as completed.")
    else:
        print(f"[-] Error: Task {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description='Python CLI Todo Application - Manage your tasks from the command line',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s add Buy groceries
  %(prog)s list
  %(prog)s list --all
  %(prog)s update 1 Buy groceries and cook dinner
  %(prog)s complete 1
  %(prog)s delete 1
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', nargs='+', help='Task description')
    parser_add.set_defaults(func=cmd_add)

    # List command
    parser_list = subparsers.add_parser('list', help='List all tasks')
    parser_list.add_argument('--all', action='store_true',
                            help='Show all tasks including completed (default: pending only)')
    parser_list.set_defaults(func=cmd_list)

    # Update command
    parser_update = subparsers.add_parser('update', help='Update a task')
    parser_update.add_argument('id', type=int, help='Task ID')
    parser_update.add_argument('description', nargs='+', help='New task description')
    parser_update.set_defaults(func=cmd_update)

    # Delete command
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='Task ID')
    parser_delete.set_defaults(func=cmd_delete)

    # Complete command
    parser_complete = subparsers.add_parser('complete', help='Mark a task as completed')
    parser_complete.add_argument('id', type=int, help='Task ID')
    parser_complete.set_defaults(func=cmd_complete)

    # Parse arguments
    args = parser.parse_args()

    # If no command provided, show help
    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Execute the command
    args.func(args)


if __name__ == '__main__':
    main()
