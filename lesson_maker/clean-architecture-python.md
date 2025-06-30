## Clean Architecture Fundamentals: An Introduction

This lesson introduces Clean Architecture and Onion Architecture, focusing on their core principles and benefits. We'll explore layered architecture, separation of concerns, and the dependency inversion principle to understand how these concepts contribute to building robust and maintainable software.

### 1. Understanding Layered Architecture

Layered architecture organizes software into distinct layers, each with a specific responsibility. This promotes modularity and makes it easier to understand, maintain, and test the system.  Communication between layers typically follows a strict hierarchy, with higher-level layers depending on lower-level layers, but not the other way around.

**Example:** A typical three-tier architecture consists of:

* **Presentation Layer:** Handles user interface and user interaction.
* **Business Logic Layer:** Contains the core business rules and logic of the application.
* **Data Access Layer:** Interacts with the database or other data sources.

### 2. Separation of Concerns (SoC)

SoC is a design principle that promotes dividing a software system into distinct sections, each addressing a separate concern. This reduces complexity and improves code reusability. In Clean Architecture, SoC is achieved by separating the application's core business logic from external concerns like databases, frameworks, and UI.

**Example:**  Imagine an e-commerce application.  Concerns might include:

* **Product Management:** Handling product details, inventory, etc.
* **Order Processing:** Managing orders, payments, and shipping.
* **User Authentication:** Handling user login and registration.

Each concern should be implemented independently, allowing changes in one area to have minimal impact on others.

### 3. Dependency Inversion Principle (DIP)

DIP states that:

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

This principle decouples layers, making them more independent and testable.  It allows you to easily swap implementations without affecting other parts of the system.

**Example:** Instead of a business logic class directly depending on a specific database implementation, it should depend on an abstract interface (e.g., `UserRepository`).  Different database implementations (e.g., SQL, NoSQL) can then implement this interface, allowing you to switch databases without modifying the business logic.

### 4. Onion Architecture

Onion Architecture is a specific implementation of Clean Architecture. It visualizes the application as a series of concentric circles, with the core business logic at the center and external dependencies on the outer layers.  Dependencies always point inwards, meaning outer layers depend on inner layers, but not vice-versa.

**Example:**

* **Core:** Contains entities and use cases (business logic).
* **Application Layer:** Contains interfaces and implementations for interacting with external services (e.g., database gateways).
* **Infrastructure Layer:** Contains concrete implementations of external services (e.g., database drivers, UI frameworks).

### 5. Benefits of Clean Architecture

* **Testability:**  Decoupled layers make it easier to test individual components in isolation.
* **Maintainability:** Changes in one part of the system have minimal impact on other parts.
* **Flexibility:**  Easily adapt to changing requirements and technologies.
* **Reusability:**  Core business logic can be reused across different platforms and applications.
* **Scalability:**  Easier to scale different parts of the system independently.


### Exercises

1. **Identify Layers:** Consider a simple blogging application. Identify the different layers you would use in a clean architecture approach and describe their responsibilities.

2. **Apply DIP:**  Imagine a scenario where you need to switch from a SQL database to a NoSQL database in your application. How would the Dependency Inversion Principle help you achieve this with minimal code changes?

3. **Onion Architecture Diagram:** Draw an Onion Architecture diagram for a ride-sharing application. Identify the core domain, application layer, and infrastructure layer components.

4. **Violation of SoC:** Describe a scenario where the Separation of Concerns principle is violated and explain the potential negative consequences.

5. **Benefits in Practice:**  Choose one of the benefits of Clean Architecture (e.g., testability) and explain how it would manifest in a real-world project. Provide a concrete example.


This lesson provides a foundational understanding of Clean Architecture and its core principles. By applying these principles, you can build more robust, maintainable, and scalable software systems. Remember that Clean Architecture is a set of guiding principles, and the specific implementation can vary depending on the project's needs.
## Project Setup and Introduction to FastAPI

This lesson covers setting up your development environment and introducing fundamental FastAPI concepts. We'll focus on creating a robust project structure based on Clean Architecture principles, setting up a virtual environment, installing necessary dependencies, and understanding basic routing and requests.

### Critical Concepts

* **Virtual Environment:** An isolated environment for your Python projects, preventing dependency conflicts between different projects.  It allows you to install specific package versions without affecting your global Python installation.
* **Dependency Management:**  The process of managing external libraries (dependencies) required by your project.  `pip` is the standard package installer for Python.  A `requirements.txt` file lists these dependencies for easy installation and reproducibility.
* **Clean Architecture:** A software design architecture that promotes separation of concerns, testability, and maintainability.  We'll use a simplified version focusing on layering our application into distinct components.
* **FastAPI:** A modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **Routing:** Defining the endpoints (URLs) of your API and how they map to specific functions in your code.
* **Requests:** How clients interact with your API.  We'll focus on handling incoming HTTP requests (e.g., GET, POST).

### Setting up the Virtual Environment and Dependencies

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv  # Creates a virtual environment named .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate  # On Windows
   ```

3. **Install FastAPI and Uvicorn:**
   ```bash
   pip install fastapi uvicorn[standard]
   ```

4. **Create a `requirements.txt` file:** This file lists your project's dependencies.
   ```bash
   pip freeze > requirements.txt
   ```

### Project Structure (Clean Architecture Inspired)

```
my_fastapi_project/
├── app/
│   ├── core/        # Core business logic and entities
│   │   └── ...
│   ├── infrastructure/ # Database interactions, external services
│   │   └── ...
│   ├── presentation/ # API endpoints (FastAPI routers)
│   │   └── ...
│   └── main.py      # Entry point for the application
├── tests/           # Unit and integration tests
└── requirements.txt
```

### Introduction to FastAPI: Routing and Requests

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Defines a GET request route at the root URL
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}") # Path parameter
async def read_item(item_id: int): # Type hinting for validation
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: dict): # Request body as a dictionary
    return item
```

### Exercises

1. **Set up a new FastAPI project:** Follow the steps above to create a virtual environment, install FastAPI and Uvicorn, and create the project structure.

2. **Create a simple API endpoint:** Define a GET route at `/hello` that returns a JSON response with the message "Hello from FastAPI!".

3. **Implement a route with a path parameter:** Create a GET route at `/users/{user_id}` that takes an integer `user_id` as a path parameter and returns a JSON response like `{"user_id": 123}`.

4. **Handle a POST request:** Define a POST route at `/items` that accepts a JSON request body with a `name` and `description` field.  Return the received data in the response.

5. **Explore the interactive documentation:** Run your FastAPI application using `uvicorn app.main:app --reload` (assuming your main file is `app/main.py` and the FastAPI instance is named `app`).  Navigate to `/docs` in your browser to explore the automatically generated interactive API documentation.


### Further Learning

* **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* **Uvicorn Documentation:** [https://www.uvicorn.org/](https://www.uvicorn.org/)
* **Clean Architecture:** [https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)


This lesson provides a foundation for building robust and well-structured FastAPI applications.  Experiment with the exercises and explore the provided resources to deepen your understanding. Remember to practice and build your own projects to solidify your knowledge.
## Core Logic Implementation: Use Cases and Entities

This lesson covers the core of application logic implementation, focusing on use cases, entities, and their interaction. We'll also touch upon dependency injection as a crucial design pattern.

**Key Concepts:**

* **Use Case (Interactor):** A use case represents a specific action or operation a user can perform within the system. It encapsulates the business logic required to fulfill that action.  Think of it as the "what" the system does.  It orchestrates the flow of data to and from entities, and other dependencies, to achieve the desired outcome.

* **Entity:** An entity represents a core concept or object within the system's domain. It holds data and often contains methods related to its data.  It's the "who" or "what" the system operates on.  Entities are typically persistent, meaning their data is stored and retrieved from a database or other storage mechanism.

* **Business Logic:** The rules, processes, and constraints that govern how the system operates and manipulates data. This logic resides within the use cases and ensures data integrity and consistency.

* **Dependency Injection (DI):** A design pattern that allows dependencies to be provided to a class instead of being created within the class itself. This promotes loose coupling, testability, and maintainability.


**Examples:**

**1. Use Case Example:**

Imagine a social media application. A use case could be "Create New Post." This use case would handle:

* Validating the post data (e.g., length, content).
* Creating a new `Post` entity.
* Saving the `Post` entity to the database.
* Notifying followers of the new post.

**2. Entity Example:**

In the same social media application, a `Post` entity might have the following attributes:

* `postId`: Unique identifier for the post.
* `userId`: ID of the user who created the post.
* `content`: The text of the post.
* `timestamp`: Date and time the post was created.

**3. Business Logic Example:**

A business rule within the "Create New Post" use case might be: "A post cannot exceed 280 characters."  This rule would be enforced within the use case before the post is saved.

**4. Dependency Injection Example:**

Instead of the "Create New Post" use case directly creating a database connection, it would receive a database connection object as a dependency through its constructor or a setter method.


**Exercises:**

**Exercise 1: Identify Use Cases and Entities**

Consider an e-commerce application. Identify three use cases and three entities relevant to this domain.  For each use case, briefly describe its purpose. For each entity, list its key attributes.

**Exercise 2: Implement a Simple Use Case**

Create a simple use case called `AddUser` for a user management system.  The use case should:

* Receive a `User` object as input.
* Validate the user's email address (ensure it contains an "@" symbol).
* If the email is valid, "save" the user (you can simulate saving by printing a success message).
* If the email is invalid, throw an exception or return an error message.

**Exercise 3: Implement Dependency Injection**

Modify the `AddUser` use case from Exercise 2 to use dependency injection.  Instead of hardcoding the email validation logic within the use case, create a separate `EmailValidator` class. Inject an instance of `EmailValidator` into the `AddUser` use case.


**Example Solution (Exercise 2 - without DI):**

```python
class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name

class AddUser:
    def execute(self, user):
        if "@" not in user.email:
            raise ValueError("Invalid email address")
        print(f"User {user.name} with email {user.email} saved successfully!")

user = User("test@example.com", "Test User")
add_user = AddUser()
add_user.execute(user)

user_invalid = User("test.example.com", "Invalid User")
try:
    add_user.execute(user_invalid)
except ValueError as e:
    print(e)
```

**Example Solution (Exercise 3 - with DI):**

```python
class User: # Same as before
    # ...

class EmailValidator:
    def is_valid(self, email):
        return "@" in email

class AddUser:
    def __init__(self, email_validator):
        self.email_validator = email_validator

    def execute(self, user):
        if not self.email_validator.is_valid(user.email):
            raise ValueError("Invalid email address")
        print(f"User {user.name} with email {user.email} saved successfully!")

email_validator = EmailValidator()
add_user = AddUser(email_validator) # Injecting the dependency
# Rest of the code remains the same...
```


These exercises and examples provide a starting point for understanding and implementing core application logic using use cases, entities, and dependency injection.  As you progress, you'll encounter more complex scenarios and learn advanced techniques for building robust and maintainable applications.
## Building the API Interface with FastAPI

This lesson covers building the interface/controller layer of your application using FastAPI. We'll explore how to connect FastAPI endpoints to business logic (use cases), handle HTTP requests and responses, validate and serialize data, and implement error handling and logging.

**Critical Concepts:**

* **Endpoints:**  Specific URLs in your API that clients interact with to perform actions or retrieve data.  They are defined using decorators like `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()`.
* **Use Cases:** Represent specific actions or operations within your application's business logic. They encapsulate the core logic and interact with data layers or external services.
* **HTTP Requests and Responses:** The fundamental way clients communicate with your API. Requests contain data sent to the server (e.g., in the body or URL parameters), and responses contain data returned by the server.
* **Data Validation and Serialization:** Ensuring incoming data conforms to expected formats and converting data between Python objects and formats suitable for transmission (e.g., JSON).
* **Error Handling and Logging:**  Gracefully handling unexpected situations and recording information about application events for debugging and monitoring.


**Samples:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Sample Use Case (Imagine this interacts with a database or other service)
class CreateUserUseCase:
    def execute(self, username: str, email: str):
        # ... logic to create a user ...
        if "@" not in email:
            raise ValueError("Invalid email format")
        return {"username": username, "email": email}

# Pydantic model for request data validation
class UserCreateRequest(BaseModel):
    username: str
    email: str

app = FastAPI()
create_user_use_case = CreateUserUseCase() # Dependency Injection

@app.post("/users/", status_code=201)
async def create_user(user_data: UserCreateRequest):
    try:
        new_user = create_user_use_case.execute(user_data.username, user_data.email)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e: # Catching general exceptions
        print(f"An error occurred: {e}") # Logging the error
        raise HTTPException(status_code=500, detail="Internal Server Error")
```

**Exercises:**

1. **Endpoint Creation:** Create a new endpoint `/items/` that accepts a `GET` request and returns a list of sample items (e.g., `[{"name": "Item 1"}, {"name": "Item 2"}]`).

2. **Connecting to a Use Case:**  Create a simple use case `GetItemsUseCase` that returns a list of items. Modify the `/items/` endpoint to use this use case.

3. **Request Data Validation:**  Define a Pydantic model `ItemCreateRequest` with fields `name` (string, required) and `description` (string, optional). Create a `POST /items/` endpoint that uses this model to validate incoming data for creating a new item.

4. **Error Handling:**  In the `POST /items/` endpoint, add error handling to raise a `400 Bad Request` error if the `name` field in the request body is empty or contains only whitespace.

5. **Logging:**  Add logging to the `POST /items/` endpoint to log the created item data (e.g., using `print()` for simplicity or a proper logging library).

6. **Advanced Error Handling:** Modify the error handling in the `POST /items/` endpoint to catch different types of exceptions (e.g., `ValueError` for specific validation errors, `TypeError` for data type issues) and return appropriate HTTP error codes and messages.


**Solutions (Partial - for Exercises 2, 3, and 5):**

```python
# Exercise 2 & 5 (combined)
class GetItemsUseCase:
    def execute(self):
        return [{"name": "Item 1"}, {"name": "Item 2"}]

get_items_use_case = GetItemsUseCase()

@app.get("/items/")
async def get_items():
    items = get_items_use_case.execute()
    print(f"Retrieved items: {items}") # Logging
    return items


# Exercise 3
class ItemCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None

@app.post("/items/", status_code=201)
async def create_item(item_data: ItemCreateRequest):
    # ... (Implementation for creating an item, including validation and error handling) ...
    return {"message": "Item created successfully"} 
```

This lesson provides a foundation for building robust and well-structured API interfaces with FastAPI. By combining endpoints, use cases, data validation, and error handling, you can create APIs that are easy to maintain, extend, and integrate with other parts of your application.  Remember to expand on these concepts and explore the rich features FastAPI offers for building production-ready APIs.
## Unit Testing Fundamentals: Introduction to Unit Testing and Mocking

This lesson introduces the fundamentals of unit testing and mocking, focusing on Python and the `pytest` framework.

**1. What is Unit Testing?**

Unit testing is a software testing method where individual units or components of a software are tested in isolation from the rest of the system to determine if they are functioning as expected.  A "unit" can be a function, a method, a class, or a module.

**Key Benefits of Unit Testing:**

* **Early Bug Detection:** Identifies bugs early in the development cycle, reducing the cost and effort of fixing them later.
* **Improved Code Design:** Encourages modular and well-defined code, as testable code is often better structured.
* **Faster Debugging:** Isolates problems quickly, making it easier to pinpoint the source of errors.
* **Regression Prevention:** Prevents the reintroduction of bugs when making changes to the codebase.
* **Living Documentation:** Serves as a form of documentation, illustrating how individual components are intended to be used.


**2. Choosing a Testing Framework: pytest**

`pytest` is a popular Python testing framework known for its simplicity, flexibility, and powerful features.  It offers:

* **Simple Test Discovery:** Automatically discovers test files and functions.
* **Concise Syntax:** Uses simple `assert` statements for writing test cases.
* **Rich Plugin Ecosystem:** Extensible with numerous plugins for various testing needs.
* **Detailed Test Reporting:** Provides comprehensive reports on test execution.

**Installation:**

```bash
pip install pytest
```

**3. Writing Basic Unit Tests with pytest**

Let's create a simple function and write a unit test for it:

```python
# calculator.py
def add(x, y):
    return x + y
```

```python
# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5
```

**Running Tests:**

Navigate to the directory containing `test_calculator.py` in your terminal and run:

```bash
pytest
```

`pytest` will automatically discover and run the test functions.


**4. Mocking Dependencies**

When testing units that rely on external dependencies (databases, APIs, etc.), we often want to isolate the unit's logic from these dependencies.  Mocking allows us to simulate the behavior of these dependencies without actually interacting with them.

**Example with `unittest.mock`:**

```python
# user_service.py
import requests

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    return response.json()

```

```python
# test_user_service.py
from unittest.mock import patch
import user_service

@patch('user_service.requests.get') # Mock the requests.get function
def test_get_user_data_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"id": 1, "name": "Test User"}
    mock_response.status_code = 200

    user_data = user_service.get_user_data(1)
    assert user_data == {"id": 1, "name": "Test User"}

@patch('user_service.requests.get')
def test_get_user_data_not_found(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")

    try:
        user_service.get_user_data(999)
    except requests.exceptions.HTTPError as e:
        assert str(e) == "Not Found"
```

Here, `@patch` replaces `requests.get` with a mock object. We can then control the mock's behavior (e.g., the returned JSON data and status code) to simulate different scenarios.


**Exercises:**

1. **Write unit tests for a function that calculates the area of a rectangle.**  Include tests for positive and zero dimensions.

2. **Write unit tests for a function that checks if a number is prime.** Include tests for prime and non-prime numbers.

3. **Write a function that fetches data from a hypothetical API endpoint using `requests`.  Then, write unit tests for this function using mocking to simulate different API responses (success, error, etc.).**


This lesson provides a foundation for understanding and implementing unit tests and mocking in Python.  By practicing these techniques, you can significantly improve the quality and reliability of your code.
## Advanced Unit Testing and Mocking in Python

This lesson covers advanced unit testing techniques in Python, focusing on testing FastAPI endpoints, mocking external services and databases, Test-Driven Development (TDD), and code coverage analysis.

**Critical Concepts:**

* **Unit Testing:**  Isolating and testing individual components (units) of your code in isolation to ensure they function correctly.  A unit can be a function, a method, or a class.
* **Mocking:** Replacing real dependencies (like databases or external APIs) with simulated objects that mimic their behavior. This allows you to test your code without relying on external systems, making tests faster and more reliable.
* **FastAPI:** A modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **Test-Driven Development (TDD):** A software development approach where tests are written *before* the code they are intended to test. This helps clarify requirements, improve design, and ensure high test coverage.
* **Code Coverage Analysis:**  A metric that measures the percentage of your code that is executed during testing.  High code coverage indicates that a larger portion of your codebase has been tested, reducing the likelihood of undiscovered bugs.


**Samples of Concepts:**

**1. Mocking an External API Call:**

```python
import requests
from unittest.mock import patch

def get_data_from_api(url):
    response = requests.get(url)
    return response.json()

@patch('requests.get') # Mock the requests.get function
def test_get_data_from_api(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"key": "value"} # Set the mock response

    data = get_data_from_api("https://example.com/api")
    assert data == {"key": "value"}
    mock_get.assert_called_once_with("https://example.com/api") # Verify the API call
```

**2. Testing a FastAPI Endpoint with Mocking:**

```python
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from unittest.mock import Mock

app = FastAPI()

def external_service():
    # In a real application, this would interact with an external service
    return "Data from external service"

@app.get("/data")
def get_data(data: str = Depends(external_service)):
    return {"data": data}

def test_get_data():
    with TestClient(app) as client:
        mock_external_service = Mock(return_value="Mocked data")
        app.dependency_overrides[external_service] = mock_external_service # Override the dependency

        response = client.get("/data")
        assert response.status_code == 200
        assert response.json() == {"data": "Mocked data"}
```

**3. Simple TDD Example:**

```python
import pytest

# Test first (will fail initially)
def test_add():
    assert add(2, 3) == 5

# Implement the function to make the test pass
def add(x, y):
    return x + y
```


**Exercises:**

1. **Mocking a Database:** Write a function that interacts with a database (e.g., inserts data).  Write a unit test that mocks the database interaction and verifies that the function calls the correct database methods with the correct arguments.

2. **Testing a FastAPI Endpoint with Dependencies:** Create a FastAPI endpoint that depends on two different services (e.g., authentication and data retrieval). Write a unit test that mocks both dependencies and verifies the endpoint's behavior.

3. **TDD Practice:**  Using the TDD approach, write a function that calculates the factorial of a number. Write the tests first, then implement the function to make the tests pass.

4. **Code Coverage:** Use a code coverage tool (like `coverage.py`) to analyze the test coverage of your code from the previous exercises.  Identify any gaps in your test coverage and write additional tests to improve it.


**Further Exploration:**

* **pytest Fixtures:** Learn how to use pytest fixtures to manage test setup and teardown efficiently.
* **Parametrized Tests:**  Explore how to write parameterized tests to test your code with different inputs using `@pytest.mark.parametrize`.
* **Mocking Libraries:** Investigate more advanced mocking libraries like `pytest-mock` and `mock`.


This lesson provides a foundation for advanced unit testing and mocking techniques.  By practicing these concepts and exploring the suggested further learning, you can significantly improve the quality and reliability of your Python code.
## Building a Sample Application: Putting it All Together

This lesson demonstrates how to build a small CRUD (Create, Read, Update, Delete) application using FastAPI and Clean Architecture, integrating concepts learned throughout previous lessons. We'll also discuss best practices and common pitfalls.

**Critical Concepts:**

* **Clean Architecture:**  A software design architecture that promotes separation of concerns, testability, and maintainability. It emphasizes the independence of the core business logic from external frameworks, databases, or UI.
* **FastAPI:** A modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **CRUD Operations:**  Fundamental data operations: Create, Read, Update, and Delete.
* **Dependency Injection:** A design pattern where dependencies are provided to a class instead of being created within the class. This promotes loose coupling and testability.
* **Repository Pattern:** An abstraction layer that separates the data access logic from the rest of the application.

**Sample Application: Task Management API**

We'll build a simple API for managing tasks.  The API will allow users to create, read, update, and delete tasks.

**Code Example (Simplified):**

```python
# domain/task.py (Entity)
class Task:
    def __init__(self, title: str, description: str, completed: bool = False):
        self.title = title
        self.description = description
        self.completed = completed

# use_cases/create_task.py (Use Case)
class CreateTaskUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, title: str, description: str):
        task = Task(title, description)
        self.task_repository.save(task)
        return task

# infrastructure/task_repository_in_memory.py (Repository Implementation)
class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = []

    def save(self, task: Task):
        self.tasks.append(task)

# presentation/api.py (FastAPI)
from fastapi import FastAPI, Depends
from .use_cases.create_task import CreateTaskUseCase
from .infrastructure.task_repository_in_memory import InMemoryTaskRepository

app = FastAPI()

def get_task_repository():
    return InMemoryTaskRepository()

@app.post("/tasks")
def create_task(title: str, description: str, task_repository = Depends(get_task_repository)):
    use_case = CreateTaskUseCase(task_repository)
    task = use_case.execute(title, description)
    return task
```

**Best Practices:**

* **Small, Focused Use Cases:**  Keep each use case focused on a single action.
* **Clear Separation of Concerns:** Adhere to Clean Architecture principles by separating domain logic, use cases, and infrastructure.
* **Dependency Injection:** Use dependency injection to manage dependencies and improve testability.
* **Input Validation:** Validate user input to prevent unexpected behavior and security vulnerabilities.
* **Error Handling:** Implement proper error handling to provide informative error messages.

**Common Pitfalls:**

* **Mixing Layers:** Avoid mixing logic from different layers (e.g., putting database queries in the use case).
* **Large Use Cases:**  Overly large use cases can become difficult to test and maintain.
* **Ignoring Dependency Injection:**  Not using dependency injection can lead to tight coupling and make testing harder.
* **Insufficient Testing:**  Lack of testing can lead to bugs and regressions.


**Exercises:**

1. **Implement the remaining CRUD operations (Read, Update, Delete) for the Task Management API.**  Follow the same structure as the `create_task` example.
2. **Replace the `InMemoryTaskRepository` with a persistent database repository (e.g., using SQLAlchemy).** This will require modifying the `infrastructure` layer.
3. **Add input validation to the API endpoints.** For example, ensure that the task title is not empty.
4. **Write unit tests for the use cases and repository implementations.**  Focus on testing the core logic of each component.
5. **Implement error handling for the API endpoints.**  Return appropriate HTTP status codes and error messages.


**Further Exploration:**

* Explore different dependency injection frameworks for Python (e.g., `injector`, `dependency_injector`).
* Learn more about advanced FastAPI features, such as authentication and authorization.
* Research different database options and ORMs for Python.


By following these principles and completing the exercises, you'll gain practical experience building robust and maintainable applications using FastAPI and Clean Architecture. Remember to focus on separation of concerns, testability, and maintainability throughout the development process.
