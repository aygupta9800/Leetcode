// Destructing object
// let address = {
//     street: "Julian Street",
//     city: "San Jose",
//     state: "California"
// }
//
// const {city, state} = address;
// console.log(`My city is ${city}`);
// console.log('My state is ' + state);

// // Destructing array

// let arr = ["aa","bb","cc","dd","ee"];
// let [ first ] = arr;
// console.log(first);

// let [one, two, ...rest] = arr;
// console.log(one);
// console.log(two);
// console.log(rest);

// for of loop
// let numbers = [10, 20 ,30]
// let total = 0;
// for(const note of numbers){
//     total +=note
// }
// console.log(total);

// // map - does not mutate the array
// const upperCase = ['a', 'b', 'c'].map(s => s.toLowerCase());
// console.log(upperCase);
//
// // reduce
// here m is prev value, n is curr value
// const total = [1, 2, 3].reduce((m, n) => m + n, 0);
// console.log(total);
//
// // filter
// const lessThanThree = [1, 2, 3, 4, 5].filter(n => n < 3);
// console.log(lessThanThree);

// // spread operator
// let child1 = { name: "Leo" };
// let child2 = {...child1, age:10};
//
// console.log(child1);
// console.log(child2);

// //rest operator
// //accept only the first argument
// function student(name1, name2) {
//     console.log("All students names without rest operator", name1, name2);
// }
//
// //accept multiple arguments as a array
// function students(...name) {
//     console.log("All student names with rest operator", ...name);
// }
//
// student("Alex", "Bob");
// students("Alex", "Bob");


// //arrow vs traditional
// function traditional(name) {
//     console.log(name);
// }
//
// traditional("cmpe273");
//
// let traditional = function (name) {
//     console.log(name);
// }
// traditional("cmpe273");
//
// let arrow = name => {
//     console.log(name);
// }
// arrow("cmpe273");


// // this in arrow vs this in traditional
// function Traditional() {
//     let value = 10;
//     return function () {
//         console.log(`Traditional function value: ${value}`);
//     }
// }
//
// const traditional = new Traditional();
// traditional();
//
// function Arrow() {
//     this.value = 10;
//     return () => {
//         console.log(`Arrow function value: ${this.value}`);
//     }
// }

const arrow = new Arrow();
arrow();


// //Diff between let, var and const
// var variables are initialized with null
// let variables are not initialized until defined
// //var scope - Error

//Check
// var greeter = "hey hi";

// function newFunction() {
//     var hello = "hello";
//     console.log(greeter)
// }
// console.log(hello);


// // var redefined
// var greeter = "hey hi";
// var greeter = "say Hello instead";

// problem with var
// var greeter = "You expect me to say Hey";

// if (true) {
//     var greeter = "But it says Hello";
// }

// console.log(greeter) //"But it says Hello"

// // let fixes it
//
// let greeter = "You expect me to say Hey";
//
// if (true) {
//     let greeter = "But it says Hello";
// }
//
// console.log(greeter) //"You expect me to say Hey"

// //const

// const temp = 10;
// temp = 100;
//
// const obj = {};
// obj.name = "cmpe273";
// console.log(obj);
//

// // sub directory level changes are allowed in const
// const arr = [];
// arr.push(10);
// console.log(arr);

// //padStart and padEnd
// to give padding to a string and making it to a particular length
// let str = "cmpe"
// console.log(str.padStart(10, '$'));
// console.log(str.padEnd(10, '$'));

// // how async works?
// const students = [
//     {name: "Chandler", year: 2},
//     {name: "Joey", year: 2}
// ];
//
// function createStudent() {
//     setTimeout(() => {
//         students.push({name: "Ross", year: 1})
//     }, 2000);
// }
//
// function getStudents() {
//     console.log(students[2]);
// }
//
// createStudent();
// getStudents();

// //callback
// const students = [
//     {name: "Chandler", year: 2},
//     {name: "Joey", year: 2}
// ]

// function getStudents() {
//     console.log(students[2]);
// }
//
// function createStudent(getStudents) {
//     setTimeout(() => {
//         students.push({name: "Ross", year: 1})
//         getStudents();
//     }, 1000);
// }
//
// createStudent(getStudents);


// //CALLBACK HELL
// async1(function(){
//     async2(function(){
//         async3(function(){
//             async4(function(){
//                 ....
//             });
//         });
//     });
// });

// //Promises
// const students = [
//     {name: "Chandler", year: 2},
//     {name: "Joey", year: 2}
// ]
//
// function getStudents() {
//     console.log(students);
// }
//
// function createStudent(callback) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             students.push({name: "Ross", year: 1})
//             if (false) {
//                 reject('Something went wrong');
//             } else {
//                 resolve();
//             }
//         }, 2000);
//     });
// }

// createStudent()
//     .then(getStudents)
//     .catch(console.log);

// Promise.all
// const promise1 = Promise.resolve('promise1');
// const promise2 = 'promise2';
// const promise3 = new Promise((resolve, reject) => {
//     setTimeout(resolve, 1000, 'promise3');
// });

// Promise.all([promise1, promise2, promise3])
//     .then(console.log);

// // Async and await

// const students = [
//     {name: "Chandler", year: 2},
//     {name: "Joey", year: 2}
// ]
//
// function getStudents() {
//     console.log(students);
// }
//
// function createStudent() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             students.push({name: "Ross", year: 1})
//             const err = false;
//             if (err) {
//                 reject('Something went wrong');
//             } else {
//                 resolve();
//             }
//         }, 2000);
//     });
// }
//
// async function main() {
//     try {
//         await createStudent();
//     } catch (e) {
//         console.log(e);
//     }
//     getStudents();
// }
//
// main();

// //Closure

// function counter() {
//     //Closure
//     let count = 0;
//
//     return () => {
//         return count++;
//     }
// }
//
// const increment = counter();
// console.log(increment());
// console.log(increment());
// console.log(increment());

// //call and apply

// var obj = {name: "Monica"};
//
// function displayNameAndAsset(asset1, asset2) {
//     let totalAsset = asset1 + asset2;
//     console.log(`Name is ${this.name} and asset is ${totalAsset}`);
// }
//
// displayNameAndAsset.call(obj, 1, 2);
//
// var obj = {name: "Monica"};

// function displayNameAndAsset(asset1, asset2) {
//     let totalAsset = asset1 + asset2;
//     console.log(`Name is ${this.name} and asset is ${totalAsset} `);
// }
//
// let assetArray = [1, 2];
// displayNameAndAsset.apply(obj, assetArray);

// // Old
// console.log(Math.max.apply(this, [1, 2, 3]));
// // New
// console.log(Math.max(...[1, 2, 3]));

// //bind
// var obj = {name: "Monica"};
//
// function displayNameAndAsset(asset1, asset2) {
//     let totalAsset = asset1 + asset2;
//     console.log(`Name is ${this.name} and asset is ${totalAsset} `);
// }
//
// var bound = displayNameAndAsset.bind(obj);
// bound(1, 2);
//
// var bound = displayNameAndAsset.bind(obj, 1, 2);
// bound();


// // Almost everything in JavaScript is an Object, like Array, Function, Date,
// // except for Primitives like Number, String, Undefined, Null

// // Array is an object?
// const arr = [1, 2, 3];
// console.log(arr);
//
// //Don't modify the original Object, this is just an example
// Array.prototype.customJoin = function (delimiter = '-') {
//     return this.join(delimiter);
// }
//
// console.log([1, 2, 3].customJoin('A'));


// // Typical way of creating an object

// const Ross = {
//     name: "Ross",
//     year: 1,
// }
//
// const Monica = {
//     name: "Monica",
//     year: 2,
// }

// // Older ways to create object blueprint using constructor
// function Student(name, year) {
//     this.name = name;
//     this.year = year;
// }

// let student1 = new Student("Rachel", 2);
// console.log(student1);

// // prototype
// function Student(name, year) {
//     this.name = name;
//     this.year = year;
// }

// Student.prototype.printName = function () {
//     console.log(`Name of the Student is ${this.name}`);
//     this.newProps = "A new property";
// }

// let student1 = new Student("Rachel", 2);
// student1.printName();
// console.log(student1.newProps);


// // - Inheritance in JavaScript works by using prototypes,
// //   objects just delegate to other objects to find properties

// // - All objects are just instances of the the Object object, Object inherits from null
// //       - Object has properties like constructor, toString, isPrototypeOf etc

// // - The prototype property is of an object is where we put methods and
// //   properties that we want other objects to inherit

// // - Prototypes are just fallback properties
// // This is just an example, you should not be modifying the Object object

// // If this is confusing you its ok!
// // JavaScript was not designed, it has just grown over the years.


// Object.prototype.a = 1;
// const b = {};
// console.log(b);

// // To access prototype of b object use b.__proto__, not b.prototype
// console.log(b.prototype, b.__proto__, b.__proto__ === Object.prototype);

// // Prototype inheritance

// function Student(name, year) {
//     this.name = name;
//     this.year = year;
// }
//
// Student.prototype.printName = function () {
//     console.log(`Name of the student is ${this.name}`);
// }
//
// function TA(name, year, salary) {
//     this.name = name;
//     this.year = year;
//     this.salary = salary;
// }
//
// // Copy the prototype
// TA.prototype = Student.prototype;
// let ta = new TA("Ross", 2, 10);
//
// console.log(ta);
// ta.printName();
//
// // Check if the method is inherited
// console.log(ta.hasOwnProperty('salary')) // true
// console.log(ta.hasOwnProperty('printName')) // false

// // using Object.create()
// Object.create creates a new object with its prototype set to another object
// same as:
//      const objectCreate = obj => Object.setPrototypeOf({}, obj) //not performant

// function Student(name, year) {
//     this.name = name;
//     this.year = year;
// }

// Student.prototype.printName = function () {
//     console.log(`Name of the Student is ${this.name}`);
// }

// let student = new Student("Ross", 1);
// let ta = Object.create(student);

// // add new property
// ta.salary = 10;

// // If property or method is not found in an object,
// // it is recursively searched in its prototype - this is called the prototype chain
// console.log(student, ta);
// ta.printName(); // Name of the Student is Ross
//
// // Useful for checking types
// console.log(student.isPrototypeOf(ta)); // true
// console.log(ta instanceof Student); // true


// // class
// class Student {
//     constructor(name, year) {
//         this.name = name;
//         this.year = year;
//     }
//
//     printName() {
//         console.log(`Student name is ${this.name}`);
//     }
// }
//
// let student = new Student("Ross", 2);
// student.printName();

// // ------------------------ own addition
// // splice method adds and removes elements in array. It mutates original array.
// const fruits = ["Banana", "Orange", "Apple", "Mango"];

// // At position 2, add 2 elements:
// fruits.splice(2, 0, "Lemon", "Kiwi");
// // array.splice(index, howmany, item1, item2 ....,item x)
// //index-> index where to add or remove element. 
// //how many =>no. of items to be removed
// // item1, ..itemx => items to be added

// // slice method returns selected elements in an array, as a new array. It doesnt mutate original array
// //array.slice(start, end) . both start and end are optional
// const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// const citrus = fruits.slice(1, 3); // returns ["Orange", "Lemon"]
// // slice method starts from starting index but doesnt includes end methods
// //U can use negative values to. fruits.slice(-3, -1);

// The includes() method returns true if an array contains a specified element, otherwise false.
// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.includes("Mango")   // Returns true

// To send Json to server we use JSON.stringify as data has to be string. 
// To recieve data from server we use JSON.parse()


// // The static keyword defines a static method or property for a class. Neither static methods 
// // nor static properties can be called on instances of the class. Instead, they're called on the class itself.
// // Static methods are often utility functions, such as functions to create or clone objects, whereas static properties
// //  are useful for caches, fixed-configuration, or any other data you don't need to be replicated across instances.
// class ClassWithStaticMethod {

//     static staticProperty = 'someValue';
//     static staticMethod() {
//       return 'static method has been called.';
//     }
  
//   }
  
//   console.log(ClassWithStaticMethod.staticProperty);
//   // output: "someValue"
//   console.log(ClassWithStaticMethod.staticMethod());
//   // output: "static method has been called."


// Object Assign




