(# ES6 Promises)

(## Overview)

This project introduces asynchronous programming in modern JavaScript using ES6 Promises.

Until now, most JavaScript code in previous projects was synchronous:

(- instructions executed immediately)
(- values were available instantly)
(- functions returned direct results)

Promises change this model completely.

A Promise represents:

a value that will exist later.

This project teaches how JavaScript handles asynchronous operations such as:

(- API requests)
(- file reading)
(- database communication)
(- uploads/downloads)
(- timers and delayed operations)

The project also introduces the modern async/await syntax used in professional JavaScript applications.

(---)

(# What We Learned)

(## 1. What a Promise Is)

A Promise represents the future result of an asynchronous operation.

A Promise can exist in 3 states:

(- Pending)
The operation is still running.

(- Fulfilled)
The operation succeeded.

(- Rejected)
The operation failed.

Main idea:

A Promise is a placeholder for a future value.

(---)

(## 2. Creating a Promise)

Promises are created using:

(```js
new Promise((resolve, reject) => {
...
});


The Promise constructor provides two important functions:

(- `resolve`)
used when the operation succeeds

(- `reject`)
used when the operation fails

Example:

(```js
new Promise((resolve, reject) => {
  resolve('Success');
});
```)

(---)

(## 3. Resolving a Promise)

A Promise is resolved using:

(```js
resolve(value);
```)

This changes the Promise state from:

(```txt
pending → fulfilled
```)

Example:

(```js
resolve({
  status: 200,
  body: 'Success',
});
```)

(---)

(## 4. Rejecting a Promise)

A Promise is rejected using:

(```js
reject(new Error('message'));
```)

This changes the Promise state from:

(```txt
pending → rejected
```)

Example:

(```js
reject(new Error('API Error'));
```)

(---)

(## 5. `then()`)

`then()` handles successful Promises.

Example:

(```js
promise.then((result) => {
  console.log(result);
});
```)

Main idea:

> "If the Promise succeeds, do this."

(---)

(## 6. `catch()`)

`catch()` handles Promise failures.

Example:

(```js
promise.catch((error) => {
  console.log(error);
});
```)

Main idea:

> "If the Promise fails, handle the error."

(---)

(## 7. `finally()`)

`finally()` always executes, regardless of success or failure.

Example:

(```js
promise.finally(() => {
  console.log('Done');
});
```)

Main idea:

> some actions must always happen.

(---)

(## 8. `Promise.resolve()`)

Creates an already successful Promise.

Example:

(```js
Promise.resolve('Success');
```)

Useful when:

(- immediately returning async values)
(- mocking APIs)
(- simplifying code)

(---)

(## 9. `Promise.reject()`)

Creates an already failed Promise.

Example:

(```js
Promise.reject(new Error('Failure'));
```)

Useful for:

(- manual error creation)
(- testing failures)
(- simplified rejection logic)

(---)

(## 10. `Promise.all()`)

Waits for all Promises to succeed.

Example:

(```js
Promise.all([promise1, promise2]);
```)

Main idea:

> all operations must succeed.

If one Promise fails, the entire Promise fails.

Useful for:

(- parallel requests)
(- loading multiple resources)
(- profile creation flows)

(---)

(## 11. `Promise.allSettled()`)

Waits for all Promises to finish, whether they succeed or fail.

Example:

(```js
Promise.allSettled([promise1, promise2]);
```)

Main idea:

> observe every Promise result individually.

Unlike `Promise.all()`, failures do not stop execution.

Useful for:

(- batch processing)
(- reporting results)
(- collecting all statuses)

(---)

(## 12. `Promise.race()`)

Returns the first Promise that finishes.

Example:

(```js
Promise.race([promise1, promise2]);
```)

Main idea:

> take the fastest result.

Useful for:

(- load balancing)
(- timeouts)
(- selecting fastest servers)

(---)

(## 13. Throwing Errors)

JavaScript errors can be created manually using:

(```js
throw new Error('message');
```)

This immediately stops execution.

Used for:

(- invalid arguments)
(- forbidden operations)
(- validation)

Example:

(```js
if (denominator === 0) {
  throw new Error('cannot divide by 0');
}
```)

(---)

(## 14. `try / catch / finally`)

These blocks handle synchronous errors safely.

Structure:

(```js
try {
  ...
} catch (error) {
  ...
} finally {
  ...
}
```)

Roles:

(- `try`)
attempt risky code

(- `catch`)
handle errors

(- `finally`)
always execute cleanup logic

Main idea:

> code should fail safely.

(---)

(## 15. `async` Functions)

Functions declared with `async` automatically return Promises.

Example:

(```js
async function test() {}
```)

Main idea:

`async` allows modern asynchronous syntax.

(---)

(## 16. `await`)

`await` pauses execution until a Promise finishes.

Example:

(```js
const result = await promise;
```)

Main idea:

> wait here until the Promise resolves.

This makes async code look synchronous.

(---)

(## 17. `async / await` + `try/catch`)

Modern JavaScript combines:

(- `async`)
(- `await`)
(- `try/catch`)

to write clean asynchronous logic.

Example:

(```js
async function example() {
  try {
    const result = await fetchData();
    return result;
  } catch (error) {
    return null;
  }
}
```)

This is now the standard way to handle asynchronous code in JavaScript.

(---)

(# Key Takeaways)

By the end of this project, the most important concepts learned were:

(- Promises represent future values)
(- asynchronous operations can succeed or fail)
(- `resolve` handles success)
(- `reject` handles failure)
(- `then`, `catch`, and `finally` manage Promise flows)
(- `Promise.all` waits for all successes)
(- `Promise.allSettled` observes all results)
(- `Promise.race` selects the fastest Promise)
(- `throw` creates manual errors)
(- `try/catch/finally` safely handles failures)
(- `async/await` simplifies asynchronous programming)

(---)

(# Final Thought)

Promises are one of the most important concepts in modern JavaScript.

Almost every real-world JavaScript application uses asynchronous operations constantly.

This project teaches the foundation of:

(- API communication)
(- backend requests)
(- uploads/downloads)
(- async frontend interactions)
(- modern server logic)

Understanding Promises is essential before moving into advanced backend development, APIs, React, Node.js, databases, and real-world asynchronous systems.
:::
