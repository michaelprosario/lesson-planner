## Lesson 1: Getting Started with JavaScript

**Learning Objectives:**

* Understand what JavaScript is and its role in web development.
* Set up a basic JavaScript development environment.
* Write your first JavaScript code.
* Understand variables, data types, and basic operators.


**1. What is JavaScript?**

JavaScript is a **dynamically typed**, **interpreted**, **high-level** programming language. It's primarily used for front-end web development to add interactivity and dynamic behavior to websites.  It can also be used for back-end development (using Node.js) and mobile app development (using frameworks like React Native).

**Key Concepts:**

* **Dynamically Typed:**  JavaScript doesn't require you to explicitly declare the data type of a variable. The type is determined automatically during runtime.
* **Interpreted:** JavaScript code is executed line by line by the browser's JavaScript engine, without needing a separate compilation step.
* **High-Level:** JavaScript provides abstractions that make it easier to write and understand code, compared to low-level languages like assembly language.


**2. Setting up your Development Environment:**

You need just a few tools to start writing JavaScript:

* **Web Browser:** Any modern web browser (Chrome, Firefox, Safari, Edge) will work.  We recommend Chrome or Firefox for their excellent developer tools.
* **Text Editor:** A text editor is where you'll write your code.  Popular choices include VS Code, Sublime Text, Atom, and Notepad++.
* **Web Browser Console:**  The browser's console is a powerful tool for testing and debugging JavaScript code. You can access it by right-clicking on a web page and selecting "Inspect" or "Inspect Element," then navigating to the "Console" tab.


**3. Writing your First JavaScript Code:**

Let's write a simple "Hello, World!" program:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First JavaScript</title>
</head>
<body>

  <script>
    console.log("Hello, World!");
  </script>

</body>
</html>
```

Save this code as an HTML file (e.g., `index.html`) and open it in your browser. You should see "Hello, World!" printed in the browser's console.

**Explanation:**

* `<script>` tags: These tags enclose your JavaScript code within the HTML document.
* `console.log()`: This function prints output to the browser's console.


**4. Variables and Data Types:**

**Variables:** Variables are used to store data.  You declare a variable using `let`, `const` (for constant values), or `var` (older style, less recommended).

**Data Types:**

* **String:** Text enclosed in single or double quotes.  Example: `"Hello"`, `'JavaScript'`
* **Number:**  Numeric values. Example: `10`, `3.14`, `-5`
* **Boolean:**  `true` or `false` values.
* **Null:** Represents the intentional absence of a value.
* **Undefined:**  Indicates that a variable has been declared but has not been assigned a value.
* **Object:**  Complex data structures that can hold multiple values.


**Example:**

```javascript
let name = "John"; // String
let age = 30;     // Number
let isStudent = true; // Boolean
let city = null;    // Null
let country;       // Undefined (no value assigned)
```


**5. Basic Operators:**

* **Arithmetic Operators:** `+`, `-`, `*`, `/`, `%` (modulo)
* **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`
* **Comparison Operators:** `==` (loose equality), `===` (strict equality), `!=` (not equal), `!==` (strict not equal), `>`, `<`, `>=`, `<=`
* **Logical Operators:** `&&` (AND), `||` (OR), `!` (NOT)


**Example:**

```javascript
let x = 10;
let y = 5;

let sum = x + y; // 15
let difference = x - y; // 5
let product = x * y; // 50
let quotient = x / y; // 2
let remainder = x % y; // 0

let isEqual = x == y; // false
let isGreater = x > y; // true
```


**Exercises:**

1. **Console Output:** Write JavaScript code to print your name and age to the console.
2. **Variable Manipulation:** Create variables to store your favorite color, a number, and a boolean value.  Print these variables to the console.
3. **Basic Calculations:** Write JavaScript code to calculate the area of a rectangle given its length and width (stored in variables). Print the result to the console.
4. **Comparison:**  Write JavaScript code to compare two numbers and print whether they are equal or not.
5. **Data Type Exploration:** Create variables of different data types (string, number, boolean, null, undefined). Use `typeof` operator to determine the data type of each variable and print it to the console.  Example: `console.log(typeof name);`


**Solutions (Partial):**

Exercise 1:

```javascript
console.log("My name is [Your Name]");
console.log("My age is [Your Age]");
```

Exercise 5:

```javascript
let myString = "Hello";
console.log(typeof myString); // Output: string

let myNumber = 10;
console.log(typeof myNumber); // Output: number

// ... (similarly for other data types)
```


This lesson provides a foundation for your JavaScript journey.  Experiment with the code, try different values, and explore the browser's console to solidify your understanding.  In the next lesson, we'll delve deeper into JavaScript control flow and functions.
## Lesson 2: Control Flow and Data Structures in JavaScript

This lesson covers how to control the execution flow of your JavaScript code and how to work with different data structures to organize and manipulate data.

**I. Control Flow**

Control flow determines the order in which statements are executed in a program.  JavaScript offers several constructs to manage this flow.

**A. Conditional Statements:**

Conditional statements allow you to execute different blocks of code based on whether a condition is true or false.

* **`if` statement:** Executes a block of code if a specified condition is true.
* **`else if` statement:**  Allows you to check multiple conditions sequentially. If the `if` condition is false, it checks the `else if` condition.
* **`else` statement:** Executes a block of code if none of the preceding `if` or `else if` conditions are true.

**Example:**

```javascript
let temperature = 25;

if (temperature > 30) {
  console.log("It's hot outside!");
} else if (temperature > 20) {
  console.log("It's a pleasant day.");
} else {
  console.log("It's a bit cool.");
} // Output: It's a pleasant day.
```

**B. Loops:**

Loops allow you to execute a block of code repeatedly.

* **`for` loop:**  Used for iterating a specific number of times.
* **`while` loop:** Used for iterating as long as a condition is true.


**Example:**

```javascript
// for loop
for (let i = 0; i < 5; i++) {
  console.log(i); // Output: 0 1 2 3 4
}

// while loop
let count = 0;
while (count < 3) {
  console.log(count); // Output: 0 1 2
  count++;
}
```


**II. Data Structures**

Data structures are specialized ways of organizing and storing data in a computer so that it can be used efficiently.

**A. Arrays:**

Arrays are ordered collections of values.  They can hold different data types.

**Example:**

```javascript
let myArray = [1, "hello", true, 3.14];
console.log(myArray[1]); // Output: hello
myArray.push("world"); // Adds "world" to the end of the array
console.log(myArray.length); // Output: 5
```

**B. Objects:**

Objects store data in key-value pairs. Keys are strings (or Symbols), and values can be any data type.

**Example:**

```javascript
let myObject = {
  name: "John",
  age: 30,
  city: "New York"
};

console.log(myObject.name); // Output: John
myObject.occupation = "Engineer"; // Adds a new key-value pair
console.log(myObject); // Output: {name: "John", age: 30, city: "New York", occupation: "Engineer"}
```

**C. Working with Strings:**

Strings are sequences of characters. JavaScript provides many built-in methods for manipulating strings.

**Example:**

```javascript
let myString = "Hello World";
console.log(myString.length); // Output: 11
console.log(myString.toUpperCase()); // Output: HELLO WORLD
console.log(myString.indexOf("World")); // Output: 6
console.log(myString.substring(0, 5)); // Output: Hello
```


**III. Exercises**

1. **Temperature Converter:** Write a program that converts Celsius to Fahrenheit and vice versa.  Prompt the user for the temperature and the unit (C or F). Use conditional statements to perform the conversion.

2. **Even Numbers:** Write a program that prints all even numbers from 0 to 20 using a `for` loop.

3. **Shopping Cart:** Create an array to represent a shopping cart. Add items (strings) to the cart using the `push` method. Print the contents of the cart and the total number of items.

4. **Student Profile:** Create an object to represent a student.  Include properties like name, age, major, and grades (an array of numbers).  Print the student's name and average grade.

5. **Palindrome Checker:** Write a function that checks if a given string is a palindrome (reads the same backward as forward).  Ignore case and spaces.  (e.g., "Race car" is a palindrome).


**IV. Solutions (Partial - encourages students to attempt first)**

Exercise 2:

```javascript
for (let i = 0; i <= 20; i += 2) {
  console.log(i);
}
```

Exercise 3 (Partial):

```javascript
let cart = [];
cart.push("item1");
cart.push("item2");
// ... add more items
console.log(cart);
console.log(cart.length);
```


This lesson provides a foundation for understanding control flow and data structures in JavaScript.  Practice the exercises and explore the documentation to deepen your understanding.  These concepts are crucial for building more complex and dynamic JavaScript applications.
## Lesson 3: Functions - Understanding and Using Functions Effectively in JavaScript

Functions are the building blocks of reusable code in JavaScript. They allow you to encapsulate a block of code, give it a name, and execute it whenever needed. This lesson covers defining, calling, and effectively using functions, including parameters, return values, scope, closures, and built-in functions.

### 1. Defining and Calling Functions

**Definition:** A function is a block of code designed to perform a specific task.  It's defined using the `function` keyword, followed by a name, parentheses `()`, and curly braces `{}`.

**Syntax:**

```javascript
function functionName(parameters) {
  // Code to be executed
}
```

**Calling:** To execute a function, use its name followed by parentheses.

**Example:**

```javascript
function greet(name) {
  console.log("Hello, " + name + "!");
}

greet("Alice"); // Output: Hello, Alice!
```

### 2. Function Parameters and Arguments

**Parameters:**  Placeholders for values that a function can receive when it's called. They are listed inside the parentheses during function definition.

**Arguments:** The actual values passed to a function when it's called.

**Example:**

```javascript
function add(x, y) { // x and y are parameters
  return x + y;
}

let sum = add(5, 3); // 5 and 3 are arguments
console.log(sum); // Output: 8
```

### 3. Return Values

**Return Value:** The value a function sends back after it has finished executing.  Specified using the `return` keyword.

**Example:**

```javascript
function square(number) {
  return number * number;
}

let result = square(4);
console.log(result); // Output: 16
```

A function without an explicit `return` statement implicitly returns `undefined`.

### 4. Scope and Closures

**Scope:**  Determines the accessibility (visibility) of variables. JavaScript has function scope: variables declared inside a function are only accessible within that function.

**Closure:** A function that has access to variables from its surrounding (enclosing) function's scope, even after the outer function has finished executing.

**Example (Closure):**

```javascript
function outerFunction() {
  let outerVar = "I am outside!";

  function innerFunction() {
    console.log(outerVar); // Accessing outerVar from innerFunction
  }

  return innerFunction;
}

let myClosure = outerFunction();
myClosure(); // Output: I am outside! (Even though outerFunction has finished)
```

### 5. Built-in Functions

JavaScript provides many pre-defined functions for common tasks.

**Examples:**

* `console.log()`: Displays output to the console.
* `Math.random()`: Generates a random number between 0 and 1.
* `parseInt()`: Converts a string to an integer.
* `Array.isArray()`: Checks if a variable is an array.


## Exercises

1. **Write a function called `calculateArea` that takes two parameters, `length` and `width`, and returns the area of a rectangle.**

2. **Create a function `greetUser` that takes a `name` as a parameter and greets the user with a personalized message, including their name.  If no name is provided, it should greet with a generic message like "Hello, guest!".** (Hint: Use default parameters or check for undefined.)

3. **Write a function `isEven` that takes a number as a parameter and returns `true` if the number is even, and `false` otherwise.**

4. **Create a closure: Write a function `counter` that returns another function. The inner function should increment a counter variable each time it's called and return the current count.**

5. **Explore built-in functions: Use `Math.random()` to generate a random number between 1 and 10 (inclusive).  Use `parseInt()` to ensure the result is an integer.**


## Solutions (Hidden - Try the exercises first!)

<details>
  <summary>Click to reveal solutions</summary>

```javascript
// 1. calculateArea
function calculateArea(length, width) {
  return length * width;
}

// 2. greetUser
function greetUser(name = "guest") {
  console.log("Hello, " + name + "!");
}

// 3. isEven
function isEven(number) {
  return number % 2 === 0;
}

// 4. counter
function counter() {
  let count = 0;
  return function() {
    return ++count;
  }
}

// 5. Random number 1-10
let randomNumber = parseInt(Math.random() * 10) + 1;
console.log(randomNumber);
```

</details>
## Lesson 4: DOM Manipulation - Introduction to the Document Object Model and how to manipulate web pages with JavaScript

This lesson introduces the Document Object Model (DOM) and how to use JavaScript to dynamically manipulate web page content.

### What is the DOM?

The **Document Object Model (DOM)** is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can connect to the page.  Essentially, it's a tree-like representation of your HTML, allowing JavaScript to access and interact with every element.

**Think of it like this:** Your HTML is a family tree. The `<html>` element is the grandparent, `<body>` is a parent, and elements within the body (like `<p>`, `<h1>`, `<div>`) are children.  The DOM allows JavaScript to find specific family members (elements) and change their characteristics (content, style, attributes).

### Selecting Elements

Before you can manipulate elements, you need to select them. Here are some common methods:

* **`getElementById()`:** Selects an element by its unique ID.
* **`getElementsByClassName()`:** Selects all elements with a specific class name.  Returns an HTMLCollection.
* **`getElementsByTagName()`:** Selects all elements with a specific tag name (e.g., 'p', 'div'). Returns an HTMLCollection.
* **`querySelector()`:** Selects the *first* element that matches a CSS selector.
* **`querySelectorAll()`:** Selects *all* elements that match a CSS selector. Returns a NodeList.

**Examples:**

```javascript
// Selecting by ID
const title = document.getElementById('page-title');

// Selecting by class name
const paragraphs = document.getElementsByClassName('paragraph');

// Selecting by tag name
const links = document.getElementsByTagName('a');

// Selecting with querySelector (first h1 element)
const mainHeading = document.querySelector('h1');

// Selecting with querySelectorAll (all elements with class "highlight")
const highlightedElements = document.querySelectorAll('.highlight');
```

### Modifying Content and Attributes

Once you've selected an element, you can modify its content and attributes.

* **`textContent`:**  Gets or sets the text content of an element.
* **`innerHTML`:** Gets or sets the HTML content of an element (use with caution due to potential security risks like XSS vulnerabilities).
* **`setAttribute()`:** Sets the value of an attribute.
* **`getAttribute()`:** Gets the value of an attribute.

**Examples:**

```javascript
// Changing text content
title.textContent = "New Page Title";

// Changing HTML content (be careful with user-provided content!)
const container = document.getElementById('content');
container.innerHTML = "<p>This is dynamically added content.</p>";

// Setting an attribute
const image = document.querySelector('img');
image.setAttribute('src', 'new-image.jpg');

// Getting an attribute
const linkUrl = link.getAttribute('href');
```


### Handling Events

Events are actions that occur in the browser, like a mouse click or a key press.  You can use JavaScript to listen for these events and execute code in response.

* **`addEventListener()`:** Attaches an event handler to an element.

**Example:**

```javascript
const button = document.getElementById('myButton');

button.addEventListener('click', function() {
  alert("Button clicked!");
});
```


### Exercises

1. **Change the text of a paragraph:** Create an HTML page with a paragraph and a button. When the button is clicked, change the paragraph's text to "Hello, DOM!".

2. **Toggle a class:** Create an HTML page with a `<div>` and a button. When the button is clicked, toggle a class named "highlight" on the `<div>`.  This class should change the background color of the div.

3. **Dynamically create a list:** Create an HTML page with an unordered list (`<ul>`) and a button. When the button is clicked, dynamically create a new list item (`<li>`) with the text "New Item" and append it to the list.

4. **Image slider:** Create an HTML page with an image and two buttons ("Previous" and "Next").  When the "Next" button is clicked, change the image `src` attribute to the next image in a predefined array.  Implement similar functionality for the "Previous" button.

5. **Form validation:** Create a simple form with a text input and a submit button.  Use JavaScript to prevent form submission if the input field is empty. Display an error message next to the input field.


These exercises will help you practice selecting elements, modifying content and attributes, and handling events.  Remember to experiment and explore the DOM further!
## Lesson 5: Asynchronous JavaScript and APIs - Working with Asynchronous Operations and Handling Data from External Sources

This lesson explores asynchronous operations in JavaScript, focusing on Promises, the Fetch API, handling JSON data, and error handling.  We'll learn how to interact with external resources and manage the asynchronous nature of these operations.

**Critical Concepts:**

* **Asynchronous Programming:**  A programming paradigm that allows a program to continue executing other tasks while waiting for a long-running operation to complete, instead of blocking the main thread.  This is crucial for operations like fetching data from a server, which can take a variable amount of time.

* **Promises:**  A JavaScript object representing the eventual completion (or failure) of an asynchronous operation and its resulting value.  A Promise can be in one of three states:
    * **Pending:** The initial state, neither fulfilled nor rejected.
    * **Fulfilled:** The operation completed successfully.
    * **Rejected:** The operation failed.

* **Fetch API:**  A modern interface for making HTTP requests (like getting data from an API). It returns a Promise that resolves to the Response object.

* **JSON (JavaScript Object Notation):** A lightweight data-interchange format that's easy for humans to read and write and easy for machines to parse and generate.  It's commonly used for transmitting data in web applications.

* **Error Handling:**  The process of anticipating, detecting, and resolving programming errors that may occur during the execution of a program, especially in asynchronous operations.


**Samples of Concepts:**

```javascript
// Asynchronous Programming & Promises Example:
function delayedGreeting(name) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(`Hello, ${name}!`);
    }, 1000); // Simulate a 1-second delay
  });
}

delayedGreeting("John")
  .then(message => console.log(message)); // Output after 1 second: "Hello, John!"


// Fetch API & JSON Example:
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json()) // Parse the JSON response
  .then(data => console.log(data)) // Log the parsed JSON data
  .catch(error => console.error('Error:', error)); // Handle potential errors


// Error Handling Example with Fetch:
fetch('https://nonexistent-url.com')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error)); // Catch and log the error
```


**Exercises:**

1. **Delayed Message:** Write a function `delayedMessage(message, delay)` that returns a Promise.  The Promise should resolve with the `message` after the specified `delay` in milliseconds.

2. **Fetch User Data:** Use the Fetch API to retrieve user data from `https://jsonplaceholder.typicode.com/users/1`.  Log the user's name and email to the console.

3. **Post Data:** Use the Fetch API to send a POST request to `https://jsonplaceholder.typicode.com/posts`.  Send a JSON payload with the following data:
    ```json
    {
      "title": "My New Post",
      "body": "This is the content of my new post.",
      "userId": 1
    }
    ```
    Log the response from the server.

4. **Error Handling with Fetch:**  Modify the previous exercise to handle potential errors during the POST request.  Log an appropriate error message if the request fails.

5. **Chaining Promises:**  Write a function that fetches data from two different endpoints (`/users/1` and `/posts?userId=1`) using the Fetch API. Chain the Promises so that the second request is only made after the first one completes successfully.  Log the combined user and post data.


**Solutions (Partial - encourages independent problem-solving):**

```javascript
// Exercise 2:
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => response.json())
  .then(user => {
    console.log("Name:", user.name);
    console.log("Email:", user.email);
  })
  .catch(error => console.error("Error:", error));


// Exercise 3 (Partial - Error handling not included):
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: "My New Post",
    body: "This is the content of my new post.",
    userId: 1
  })
})
.then(response => response.json())
.then(data => console.log(data));
```


This lesson provides a foundation for working with asynchronous operations and APIs in JavaScript.  Practice these concepts and exercises to build your proficiency.  Understanding these principles is essential for modern web development.
## Lesson 6: Advanced Concepts - Introduction to More Advanced Concepts and Best Practices

This lesson introduces more advanced JavaScript concepts, focusing on Object-Oriented Programming (OOP) principles, classes and inheritance, modules, and best practices.

### 1. Object-Oriented Programming (OOP) Principles

OOP is a programming paradigm based on the concept of "objects," which can contain data (properties) and code (methods) that operate on that data.  Key OOP principles include:

* **Encapsulation:** Bundling data and methods that operate on that data within a single unit (the object). This helps organize code and prevent unintended access to data.
* **Inheritance:** Creating new objects (classes) based on existing ones, inheriting their properties and methods. This promotes code reuse and reduces redundancy.
* **Polymorphism:**  The ability of objects of different classes to respond to the same method call in their own specific way. This allows for flexible and extensible code.
* **Abstraction:** Hiding complex implementation details and showing only essential information to the user. This simplifies interaction with objects and improves code maintainability.

**Example:**

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  speak() { // Polymorphism: Overriding the speak method
    console.log(`${this.name} barks!`);
  }
}

const myDog = new Dog("Buddy");
myDog.speak(); // Output: Buddy barks!
```

### 2. Classes and Inheritance

Classes are blueprints for creating objects. Inheritance allows creating new classes based on existing ones.

* **`class` keyword:** Used to define a class.
* **`constructor()`:** A special method within a class that initializes the object's properties.
* **`extends` keyword:** Used to create a subclass that inherits from a superclass.
* **`super()`:**  Calls the constructor of the parent class.

**Example:**  (See the example in the OOP Principles section)


### 3. Modules and Import/Export Statements

Modules help organize code into reusable units.

* **`import`:** Used to import functions, classes, or variables from other modules.
* **`export`:** Used to make functions, classes, or variables available for import by other modules.

**Example:**

**module1.js:**

```javascript
export function greet(name) {
  console.log(`Hello, ${name}!`);
}

export const message = "Welcome!";
```

**module2.js:**

```javascript
import { greet, message } from './module1.js';

greet("Alice"); // Output: Hello, Alice!
console.log(message); // Output: Welcome!
```


### 4. Best Practices and Common Pitfalls

* **Use descriptive variable and function names:** Improves code readability.
* **Comment your code:** Explains the purpose and logic of your code.
* **Avoid global variables:**  Can lead to naming conflicts and make code harder to maintain.
* **Handle errors gracefully:** Use `try...catch` blocks to prevent unexpected crashes.
* **Follow consistent coding style:**  Makes code easier to read and understand.


### Exercises

1. **Create a `Shape` class with a `calculateArea()` method. Create subclasses like `Circle` and `Rectangle` that inherit from `Shape` and override the `calculateArea()` method to calculate the area of the respective shapes.**

2. **Create two modules: one containing a function to calculate the factorial of a number and another module that imports and uses this function.**

3. **Refactor the following code to use classes and inheritance:**

```javascript
function createCar(make, model) {
  return {
    make: make,
    model: model,
    start: function() {
      console.log("Engine started.");
    }
  };
}

const myCar = createCar("Toyota", "Camry");
myCar.start();
```

4. **Research and explain the difference between `let`, `const`, and `var` in JavaScript.  Provide examples of when to use each.**


By understanding and applying these advanced concepts and best practices, you can write more organized, maintainable, and efficient JavaScript code. Remember to practice regularly and explore further to deepen your understanding.
