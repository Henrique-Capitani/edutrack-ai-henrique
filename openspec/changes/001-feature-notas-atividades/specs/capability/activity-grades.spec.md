# activity-grades Specification

## Purpose
This specification defines the requirements for storing and managing student grades for specific academic tasks.

## ADDED Requirements

### Requirement: Store activity grades
The system SHALL store grades given to a user for a specific academic task.

**Fields:**
- `user_id`: Foreign key to `user` table (the student).
- `academic_task_id`: Foreign key to `academic_tasks` table.
- `grade`: number (e.g., float or integer) representing the score.
- `created_by`: Foreign key to `user` table (the teacher who graded it).

#### Scenario: A teacher grades an activity for a student
- **WHEN** a teacher submits a grade for a student on a specific academic task
- **THEN** the system SHALL create a new record in the `activity_grades` table with the student's `user_id`, the `academic_task_id`, the `grade`, and the teacher's `user_id` as `created_by`.

### Requirement: Provide an endpoint to submit grades
The system SHALL provide a secure endpoint to create a new activity grade.

#### Scenario: A request is made to create a grade
- **WHEN** a POST request is sent to `/activity_grades` with a valid payload containing `user_id`, `academic_task_id`, and `grade`
- **THEN** the system SHALL validate that the authenticated user has permission to grade
- **AND** the system SHALL create the grade record as specified in the 'Store activity grades' requirement.
