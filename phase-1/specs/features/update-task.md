# Feature: Add Task

## Goal
User natural language ya UI se new task add kar sakay.

## User Stories
- As a user, I can add a task with title
- As a user, I can optionally add description

## Acceptance Criteria
- Title required (1–200 chars)
- Task user se linked ho
- Default completed = false

## Inputs
- title: string (required)
- description: string (optional)

## Outputs
- task_id
- title
- status: created

## Constraints
- No manual code
- Must be implemented via Claude Code
