# ES6 Classes

## Overview

This project introduces ES6 Classes and focuses on object-oriented programming in modern JavaScript.

The goal of this project is to understand how ES6 improves object construction and organization by introducing:

- classes
- constructors
- getters and setters
- methods and static methods
- inheritance
- abstract class patterns
- symbols and metaprogramming

Each task builds on the previous one, gradually moving from simple class creation to more advanced concepts like inheritance and metaprogramming.

---

# Task-by-Task Summary

## Task 0 — ClassRoom

This task introduces the basic ES6 class syntax.

The goal is to create a class named ClassRoom that stores one value: the maximum number of students allowed in a room.

The class uses a constructor to initialize the object when a new instance is created.

Main idea:

- Learn how to define a class
- Learn how to initialize attributes with a constructor
- Understand that this refers to the current object

What the class does:

It creates classroom objects that store one internal property:

_maxStudentsSize

---

## Task 1 — initializeRooms

This task introduces class instantiation and imports.

The goal is to import the ClassRoom class and create several classroom objects from it.

Main idea:

- Learn how to import a class from another file
- Learn how to create multiple instances from the same class
- Understand that one class can generate many similar objects

What the function does:

It returns an array containing three different classroom objects with predefined sizes.

---

## Task 2 — HolbertonCourse

This task introduces getters, setters, and validation.

The goal is to create a course object with:

- a name
- a length
- a list of students

Each value must be validated before being stored.

Main idea:

- Learn how to protect object properties
- Learn how getters expose internal values
- Learn how setters control and validate updates

What the class does:

It creates course objects that safely store course information while enforcing correct data types.

---

## Task 3 — Currency

This task introduces instance methods.

The goal is to create a class representing a currency with:

- a code
- a name

Then add a method that formats both values into a readable string.

Main idea:

- Learn how to add methods to a class
- Understand that instance methods define behavior on objects

What the class does:

It stores currency information and provides a method to display it in a readable format.

---

## Task 4 — Pricing

This task introduces static methods and object composition.

The goal is to create a class that represents a price using:

- an amount
- a currency object

The class also includes:

- a normal instance method for formatting the full price
- a static method for converting prices

Main idea:

- Learn the difference between instance methods and static methods
- Learn how one class can contain another class as a property

What the class does:

It combines an amount and a currency into a full pricing object and provides formatting and conversion logic.

---

## Task 5 — Building

This task introduces abstract class behavior.

JavaScript does not support abstract classes directly, so this task simulates one.

The goal is to create a base class that forces child classes to implement a required method.

Main idea:

- Learn how to simulate an abstract class in JavaScript
- Learn how to enforce method implementation in subclasses

What the class does:

It defines a building object and forces every child class to implement an evacuation warning method.

---

## Task 6 — SkyHighBuilding

This task introduces inheritance.

The goal is to create a specialized building class that extends Building.

It adds:

- a number of floors

and overrides the evacuation method.

Main idea:

- Learn how inheritance works with extends
- Learn how to call the parent constructor with super
- Learn how to override inherited methods

What the class does:

It creates a more specific building type with extra behavior.

---

## Task 7 — Airport

This task introduces metaprogramming with symbols.

The goal is to customize how an object is represented when converted to a string.

Main idea:

- Learn how to customize built-in object behavior
- Learn how Symbol.toStringTag changes object string representation

What the class does:

It stores airport information and customizes how the object appears when converted to text.

---

## Task 8 — HolbertonClass

This task introduces primitive conversion.

The goal is to control how an object behaves when JavaScript tries to convert it into:

- a number
- a string

Main idea:

- Learn how to control primitive conversion
- Learn how Symbol.toPrimitive customizes object casting

What the class does:

It returns different values depending on how the object is converted.

---

## Task 9 — Hoisting

This task focuses on fixing broken class logic.

The goal is to correct a file with several issues related to:

- class declaration order
- constructor parameters
- broken getters
- incorrect references

Main idea:

- Understand that classes are not hoisted like functions
- Learn how declaration order matters
- Learn how object relationships should be structured

What the file does:

It creates student objects linked to Holberton classes and returns a full student list.

---

## Task 10 — Car

This task introduces advanced metaprogramming with symbols.

The goal is to clone a class instance while preserving the real class type, even when inherited.

Main idea:

- Learn how cloning works with inheritance
- Learn how Symbol.species controls which constructor is used for derived objects

What the class does:

It creates car objects and clones them while preserving the child class type.

---

# Key Concepts Learned

By the end of this project, the most important ES6 class concepts were:

- how to define a class
- how constructors initialize objects
- how getters and setters protect internal state
- how methods add behavior to objects
- how static methods belong to the class itself
- how inheritance works with extends
- how super connects child and parent classes
- how to simulate abstract classes
- how symbols customize internal JavaScript behavior
- how metaprogramming changes object behavior

---

# Final Takeaway

This project builds the foundation of object-oriented programming in JavaScript.

It teaches how to move from simple object storage to fully structured and reusable class-based design.

By the end, the key lesson is that ES6 classes are not just cleaner syntax.

They provide a better way to:

- organize logic
- structure data
- reuse behavior
- control object behavior
- write more maintainable JavaScript

This project is the foundation for writing scalable object-oriented JavaScript.
:::