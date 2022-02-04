//1.  Q data types in js
// primtitive types:
string, Number, BigInt, Boolean, Undefined, Null, Symbol
// When a variable is declared but not assigned, it has the value of undefined and it’s type is also undefined.
// Null - It represents a non-existent or a invalid value.
// Symbol - It is a new data type introduced in the ES6 version of javascript. 
// It is used to store an anonymous and unique value.
// example. var symbol1 = Symbol('symbol');
// typeof(NaN) 'number', typeof(undefined) 'undefined', typeof(null) 'object'
// Non Primitive types: Object
// It is important to remember that any data type that is not primitive data type, is of Object type in javascript.

// 2. In JavaScript, primitive data types are passed by value and non-primitive data types are passed by reference.

// 3. IIFE(Immediately invoked function) => function which that runs as soon as defined.
// ex. (function(){ 
//     // Do something;
//   })();
// Below code will throw error as function should have a name. but for iife it wont.
// function (){
//     //Do something;
// }
// To remove this error, we add the first set of parenthesis that tells the compiler that the function is not a function declaration, instead, it’s a function expression.

4. // “this” keyword refers to the object that the function is a property of.
// The value of “this” keyword will always depend on the object that is invoking the function.
// function doSomething() {
//     console.log(this);
//   }
          
//   doSomething(); # returns global object
// var obj = {
//     name:  "vivek",
//     getName: function(){
//     console.log(this.name);
//   }
// }
        
// obj.getName(); #return obj object
// ex.3
// var obj = {
//     name:  "vivek",
//     getName: function(){
//     console.log(this.name);
//   }      
// }    
// var getName = obj.getName; 
// var obj2 = {name:"akshay", getName };
// obj2.getName();

//5.  Call Apply Bind
let printFullName = function(x, y) {
    console.log(this.name + x +y)
}
obj = {name: 'Ayush'}
// With call and apply we can borrow the function and pass any object for this reference inside the fn.
// Function borrowing
printFullName.call(obj, x, y); // argument passed seperately
printFullName.apply(obj, [x, y]); // argument passed in array
let printName = printFullName.bind(obj, x,y); // return copy of function with this binding. not immediately called 
printName();


// 6.
// Currying is an advanced technique to transform a function of arguments n, to n functions of one or less arguments.
// Ex. 1 curring using closuse
var multiply = function(x) {
    return function(y) {
        console.log(x,y)
    }
}
multipyByTwo = multiply(2) // Transforming the function with less arguments
multiplyByThree = mulitply(3)
multiplyByTwo(5)

// Ex. 2 curring using Bind
var multiply = function(x,y) {
    console.log(x,y);
}
multipyByTwo = multiply.bind(this,2) // Transforming the function with less arguments
multiplyByThree = mulitply.bind(this,3)
multiplyByTwo(5)


// 7. Prototype and Prototypical Inheritance
arr= [1,2,3,4,5]
arr.__proto__ // will return all the properties attached by JS Engine 
arr.__proto__ === Array.prototype
arr.__proto__.__proto__ === Object.prototype
arr.__proto__.__proto__.__proto__ === null

// All javascript objects inherit properties from a prototype. ex. Array objects inherit properties from the Array prototype.
// On top of the chain is Object.prototype. Every prototype inherits properties and methods from the Object.prototype.
// A prototype is a blueprint of an object. Prototype allows us to use properties and methods on an object even if the properties and methods do not exist on the current object
arr.push(2)
// The javascript engine sees that the method push does not exist on the current array object and therefore, looks for the method push inside the Array prototype and it finds the method. => Prototypical Inheritance

// 8. Memoization: Memoization is a form of caching where the return value of a function is cached based on its parameters. If the parameter of that function is not changed, the cached version of the function is returned.
// ex.

// function memoizedAddTo256(){
//     var cache = {};
//     return function(num){
//       if(num in cache){
//         console.log("cached value");
//         return cache[num]
//       }
//       else{
//         cache[num] = num + 256;
//         return cache[num];
//       }
//     }
//   }
//   var memoizedFunc = memoizedAddTo256();
//   memoizedFunc(20); // Normal return
//   memoizedFunc(20); // Cached return

// 9. Constructor Function in JS: Used to create objects in JS
// Name of a constructor function should always be written in Pascal Notation: every word should start with a capital letter.
// ex.
// function Person(name,age,gender){
//     this.name = name;
//     this.age = age;
//     this.gender = gender;
//   }
  
//   var person1 = new Person("Vivek", 76, "male");
//   console.log(person1);
  
//   var person2 = new Person("Courtney", 34, "female");
//   console.log(person2);


// 10. DOM stands for Document Object Model.

// DOM is a programming interface for HTML and XML documents.

// When the browser tries to render a HTML document, it creates an object based on the HTML document called DOM. Using this DOM, we can manipulate or change various elements inside the HTML document.


// 11. / Arrow functions can only be used as a function expression.
// The biggest difference between the traditional function expression and the arrow function, is the handling of the this keyword. The this keyword inside an arrow function, does not refer to the object calling it. It rather inherits its value from the parent scope which is the window object in this case.
// By general definition, the this keyword always refers to the object that is calling the function.

// var obj1 = {
//     valueOfThis: function(){
//       return this;
//     }
//   }
//   var obj2 = {
//     valueOfThis: ()=>{
//       return this;
//     }
//   }
  
//   obj1.valueOfThis(); // Will return the object obj1
//   obj2.valueOfThis(); // Will return window/global object

// 12. Rest operator:
// Using rest operator, we can create fns which can take variable number of arguments
// Any number of arguments will be converted into an array using the rest parameter.
// Rest parameter should always be used at the last parameter of a function:


// 13. classes in JS
// Introduced in the ES6 version, classes are nothing but syntactic sugars for constructor functions.
// KEY DIFFERENCES:
// Unlike functions, classes are not hoisted. A class cannot be used before it is declared.
// A class can inherit properties and methods from other classes by using the extend keyword.
// All the syntaxes inside the class must follow the strict mode(‘use strict’) of javascript. Error will be thrown if the strict mode rules are not followed.

// // Before ES6 version, using constructor functions
// function Student(name,rollNumber,grade,section){
//     this.name = name;
//     this.rollNumber = rollNumber;
//     this.grade = grade;
//     this.section = section;
//   }
  
//   // Way to add methods to a constructor function
//   Student.prototype.getDetails = function(){
//     return 'Name: ${this.name}, Roll no: ${this.rollNumber}, Grade: ${this.grade}, Section:${this.section}';
//   }
  
  
//   let student1 = new Student("Vivek", 354, "6th", "A");
//   student1.getDetails();
//   // Returns Name: Vivek, Roll no:354, Grade: 6th, Section:A
  
//   // ES6 version classes
//   class Student{
//     constructor(name,rollNumber,grade,section){
//       this.name = name;
//       this.rollNumber = rollNumber;
//       this.grade = grade;
//       this.section = section;
//     }
  
//     // Methods can be directly added inside the class
//     getDetails(){
//       return 'Name: ${this.name}, Roll no: ${this.rollNumber}, Grade:${this.grade}, Section:${this.section}';
//     }
//   }
  
//   let student2 = new Student("Garry", 673, "7th", "C");
//   student2.getDetails();
//   // Returns Name: Garry, Roll no:673, Grade: 7th, Section:C


// 14. Generator Functions
// Introduced in ES6 version, generator functions are a special class of functions.
// They can be stopped midway and then continue from where it had stopped.
// Generator functions are declared with the function* keyword instead of the normal function keyword:

// In the case of generator functions, when called, they do not execute the code, instead they return a generator object . This generator object handles the execution.

// function* genFunc(){
//   yield 3;
//   yield 4;
// }
// genFunc(); // Returns Object [Generator] {}

// // The generator object consists of a method called next() , this method when called, executes the code until the nearest yield statement, and returns the yield value.

// // For example if we run the next() method on the above code:

// genFunc().next(); // Returns {value: 3, done:false}
// genFunc().next(); // Returns {value: 4, done:true}


// 15. Weakset in js. In javascript, Set is a collection of unique and ordered elements.
// Just like Set, WeakSet is also a collection of unique and ordered elements with some key differences:
// Weakset contains only objects and no other type.
// An object inside the weakset is referenced weakly. This means, if the object inside the weakset does not have a reference, it will be garbage collected.

// Unlike Set, WeakSet only has three methods, add() , delete() and has() .
// const newSet = new Set([4, 5, 6, 7]);
// console.log(newSet);// Outputs Set {4,5,6,7}
// const newSet2 = new WeakSet([3, 4, 5]); //Throws an error

// let obj1 = {message:"Hello world"};
// const newSet3 = new WeakSet([obj1]);
// console.log(newSet3.has(obj1)); // true


// 16.
// In javascript, Map is used to store key-value pairs. The key-value pairs can be of both primitive and non-primitive types.

// WeakMap is similar to Map with key differences:

// The keys and values in weakmap should always be an object.
// If there are no references to the object, the object will be garbage collected.


// const map1 = new Map();
// map1.set('Value', 1);

// const map2 = new WeakMap();
// map2.set('Value', 2.3); // Throws an error

// let obj = {name:"Vivek"};
// const map3 = new WeakMap();
// map3.set(obj, {age:23});





