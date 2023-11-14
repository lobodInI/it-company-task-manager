# IT COMPANY TASK MANAGER

## Project Overview

>This task manager is a web-based application designed to help users organize and keep track of their tasks efficiently. Users can add, edit, and mark tasks as completed. The user interface is clean and user-friendly, providing a seamless experience for managing daily tasks.

## Installation Instructions

To install IT Task Manager, follow these steps:

- Clone the repository:

    ```bash
    git clone https://github.com/lobodInI/it-company-task-manager.git
    ```

- Go to the project directory:

    ```bash
    cd it_company_task_manager
    ```

- Install virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

- Install depending on:

    ```bash
    pip install -r requirements.txt
    ```
- File `.env.sample` is used as example. Rename it  -> `.env` and insert your secret key.
 
- Apply migrations:

    ```bash
    python manage.py migrate
    ```
  
- Create superuser with command:

    ```bash
    python manage.py createsuperuser
    ```
  
- Run server:

    ```bash
    python manage.py runserver
    ```

- Open your browser and check the address (http://127.0.0.1:8000/).

## Usage Guide

1. Sign in | Sing up.
2. Add an employee position.
3. Add tasks type.
4. Add new tasks, edit existing ones and mark them as completed.


## Configuration

- Registration and authentication of users.
- Creating, editing and deleting tasks.
- Marking tasks as completed.
