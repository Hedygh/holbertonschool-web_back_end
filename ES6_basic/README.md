# ES6 Basics

## Overview

This project introduces the core features of ES6 ECMAScript 2015 and focuses on writing modern, cleaner, and more maintainable JavaScript.

The goal is not only to make code work, but to understand how ES6 improves:

- readability
- consistency
- maintainability
- developer habits

Throughout this project, we rewrote older JavaScript patterns using modern ES6 syntax and concepts.

---

# What We Learned

## 1. const and let

One of the first ES6 improvements is replacing var with:

- const → when the variable should not be reassigned
- let → when the variable needs to change

### Key idea

Use const by default.
Only use let when reassignment is necessary.

### Why?

var is function-scoped and can lead to unexpected behavior.
const and let are safer and more predictable.

---

## 2. Block Scope

let and const are block-scoped, which means they only exist inside the block where they are declared.

```js
if true {
const message = 'Hello';
}


`message` only exists inside the `if` block.

### Why it matters

This prevents variables from being accidentally overwritten outside their intended scope.

---

## 3. Arrow Functions

Arrow functions provide a shorter and cleaner way to write functions.

### Traditional function

```js
function adda, b {
  return a + b;
}
```

### ES6

```js
const add = a, b => a + b;
```

### Why it matters

Arrow functions are:

- shorter
- cleaner
- easier to read

They also preserve the surrounding `this`, which avoids older workarounds like `const self = this`.

---

## 4. Default Parameters

ES6 allows default values directly in function parameters.

### Before

```js
if value === undefined {
  value = 10;
}
```

### ES6

```js
function examplevalue = 10 {}
```

### Why it matters

Cleaner and more readable function definitions.

---

## 5. Rest Parameters

Rest syntax `...args` allows a function to receive an unknown number of arguments.

```js
function example...args {
  return args.length;
}
```

### Why it matters

Useful when a function should accept a flexible number of values.

---

## 6. Spread Syntax

Spread syntax `...` expands arrays, strings, or objects.

### Example

```js
const arr = [...array1, ...array2];
```

### Why it matters

Useful for:

- merging arrays
- copying arrays
- expanding strings
- combining objects

---

## 7. Template Literals

Template literals make string interpolation easier and more readable.

### Before

```js
'Hello ' + name
```

### ES6

```js
`Hello ${name}`
```

### Why it matters

Cleaner string construction, especially for long or dynamic text.

---

## 8. Object Property Shorthand

When an object key and variable name are the same, ES6 allows shorter syntax.

### Before

```js
const obj = {
  income: income,
};
```

### ES6

```js
const obj = {
  income,
};
```

### Why it matters

Less repetition, cleaner object creation.

---

## 9. Computed Property Names

ES6 allows dynamic property names when creating objects.

```js
const obj = {
  [`income-${year}`]: value,
};
```

### Why it matters

Useful when object keys depend on variables or computed values.

---

## 10. Method Properties

ES6 allows shorter syntax for methods inside objects.

### Before

```js
const obj = {
  sayHello: function  {
    return 'Hello';
  },
};
```

### ES6

```js
const obj = {
  sayHello {
    return 'Hello';
  },
};
```

### Why it matters

Cleaner and more natural object methods.

---

## 11. `for...of` Loops

`for...of` is the ES6-friendly way to loop through iterable values like arrays.

### Example

```js
for const value of array {
  console.logvalue;
}
```

### Why it matters

Unlike `for...in`, which iterates over indexes, `for...of` iterates directly over values.

This makes array iteration more readable and less error-prone.

---

## 12. Dynamic Objects

We learned how to create objects with dynamic keys based on function input.

```js
return {
  [departmentName]: employees,
};
```

### Why it matters

Useful when object structure depends on runtime values.

---

## 13. Objects with Data and Behavior

Objects in JavaScript can store both:

- data
- methods

Example:

```js
{
  allEmployees: employeesList,
  getNumberOfDepartmentsemployees {
    return Object.keysemployees.length;
  },
}
```

### Why it matters

Objects are not just containers for data.  
They can also define behavior and logic around that data.

---

# Tools and Environment

## Node.js

Node.js allows us to run JavaScript outside the browser.

In this project, it is used to:

- run JavaScript files
- execute project scripts
- work with npm dependencies

---

## npm

npm is the package manager used to install and manage project dependencies.

We use it to:

- install tools
- run scripts
- manage the project environment

---

## ESLint

ESLint checks code quality and style.

It helps detect:

- bad formatting
- unused variables
- poor practices
- style inconsistencies

### Command

```bash
npm run check-lint
```

### Why it matters

Code must not only work.  
It must also be clean and follow standards.

---

## Jest

Jest is the testing framework used to test code behavior.

### Command

```bash
npm test
```

### Why it matters

Jest checks if the code works as expected.

---

## Babel

Babel allows modern JavaScript syntax to run correctly in the project environment.

### Why it matters

It ensures ES6 code is supported and executable.

---

# Key Takeaways

By the end of this project, the most important lessons were:

- write modern JavaScript
- prefer `const` over `let`
- avoid `var`
- use ES6 syntax to reduce unnecessary code
- write cleaner and more readable functions
- simplify object creation
- understand the difference between older and modern JavaScript patterns
- use ESLint to enforce clean code habits
- understand that readability is just as important as functionality

---

# Final Thought

The purpose of this project was not just to learn new syntax.

It was to build better JavaScript habits.

ES6 helps write code that is:

- cleaner
- safer
- easier to read
- easier to maintain
- closer to professional standards

This project was a foundation for writing modern JavaScript properly.
:::
