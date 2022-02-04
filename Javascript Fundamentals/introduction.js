/*
Notes:
1. Everything in JS happens inside the execution context
 execution context has 2 component: 
 a. variable environment(or memory) where key: value pair are stored
 b. thread of execution(or code) where code is executed one command at a time line by line.

2. JS is synchronous, blocking, single threaded language.
single threaded means that only one command can be executed at a time.
*/

/*
Notes:
1. What happens when you run JavaScript Code?
An Execution Context is created when we run a JS program. First, Global Execution context
is created to run the program.
Execution context is created in 2 phases
a. Memory creation phase: in which memory is assigned to evry variables and functions
variables get undefined value while fn store entire code in key:value type storage
b. code execution phase: in this code is executed line by line and value is assigned to memory
If there is any other fn called inside it then a local execution context is created inside it
Once the function ends, the EC is removed from the call stack.
When the program ends, even the global EC is pulled out of the call stack.

Call stack maintains the order of execution of Execution Context in JS.
*/

/*
Hoisting concept
2 Golden Rules:
1. Variable declarations are scanned and are made undefined
2. Function declarations(which are not stored in variable) are scanned and
 are made available

For arrow functions, we are storing function inside a variable, and when memory
is allocated to variables it store undefined, so when we try to invoke the variable
as a function, js finds undefined instead of a function, so it shows error 
that getName() is not a function as that is actually a normal variable
that you're are trying to access as a function............
*/

/*
1. Shortest Program in JS: Empty file. Still, browsers make global EC and global space along with Window object.
2. Global Space: Anything that is not in a function, is in the global space.
3. Variables present in a global space can be accessed by a "window" object. (like window.a)
4. In global space, (this === window) object.
*/

/*
1. Undefined is like a placeholder till a variable is not assigned a value.
2. undefined !== not defined
3. JS- weakly typed language since it doesn't depend on data type declarations.
*/

/*
1. Whenever EC is created, Lexical Environment is also created.
2. Lexical Environment is the local memory alongwith the lexical environment of its parent
3. scope chain - chain of LE which defines whether the variable/fn is present or not in the scope.

Scope: where you can access the value of our function in our code
Lexical environment : the Local memory(Created and goes hand-in-hand with 1st phase of corresponding execution context ) 
along with Lexical environment with the parent! and
every time the lexical environment of the corresponding context is used,
it references to its parent Lexical environment

for simply understanding, I will try it as 'an onion example'
see when one layer of onion(a variable) covers the layer inside it, it also covers the inner layers inside that layer and a point on our first layer of onion encloses inner layers our inner layer(variable and function inside the layer) gets covered by our first layer(can access the variable on the context) and the second layer(under first layer) encloses the third layer(innermost layer)still covered by 1st layer(can access the variable on layer)

the Closure concept starts here
*/

/*
Temporal Dead Zone is a behaviour that occurs with variables declared using let and const keywords.
It is a behaviour where we try to access a variable before it is initialized.
Examples of temporal dead zone:
x = 23; // Gives reference error
let x;
function anotherRandomFunc(){
  message = "Hello"; // Throws a reference error
  let message;
}
anotherRandomFunc();
-> let and const are hoisted. we cant use them before initialization is 
    result of "temporal dead zone". we get reference error if we try to access variable
    in TDZ(i.e before they are initialized)
-> js use diff memory than global execution context to store let and cost. which is reason behind "temporal dead zone"
-> level of strictness ... var<<let<<const.
-> var //no temporal dead zone, can redeclare and re-initialize, stored in GES, not block scoped.
    let //use TDZ, can't re-declare, can re-initialize, stored in separate memory, block scoped.
    const //use TDZ, can't re-declare, can't re-initialize, stored in separate memory, block scoped.
-> syntax error is similar to compile error. while type and reference error falls under run time error.
-> syntax error ... violation of JS syntax
   type error ...  while trying to re-initialize const variable
   reference error ... while trying to access variable which is not there in the scope.

*/

/*
Q) What is block in JavaScript?
> multiple js statements formed in a group enclosed in brackets and it forms a block

Q) What is need of a block/Grouping?
> JavaScript sometimes expect to run a single statement to run, but we need
 to run commands with multiple statements which is only possible by block

eg. on 4:14

write a simple function:
// even empty script is perfectly valid js script, what about empty brackets!!
{
 var a = 10;
 let b = 20;
 const c =30; 
}

When a js script get hoisted (a GEC) gets created 'var' listed towards 'Global environment' and other variables 'let' and 'const' declarations go to the 'Block environment' .
This become especially important when deciding the scope of a particular variable, since b and c are located in 'Block environment' and for a as we know exists in 'Global environment' any statement out of the "Block" can access 'a' ie.  ' Variable in Global environment' and other are not!
so when we understand the extent of Global and local environment variables and their 'Scopes' == Environment that forms the lexical hierarchy of 'Scopes' and 'Scopes' have Levels like 'Scope inside scope'

see script in 7:03

 var a = 100;
{
 var a = 10;
 let b = 20;
 const c =30; 
 console.log(a);
 console.log(b);
 console.log(c);
}
 console.log(a);
 console.log(b);
 console.log(c);

So in block " var a = 10;" influences the value within the block hence  console.log(a); >> 10 and outside of the block 'Variable in Global environment' influences value of a hence console.log(a); >> 100

Illegal shadowing:

let a = 200;
{
 var a =20;
}

as 'var' declaration goes to 'Global environment' and sets in Memory context, it cannot be set using 'Block environment' value Hence:    Uncaught SyntaxError: Identifier 'a' has already been declared

*/


/*
Closure- Its a function bundled together(enclosed) with its Lexical Environment.
In js, when a fn is returned from another fn, they remember the reference to their Lexical scope.
Whenever function is returned, even if its vanished in execution context but still it remembers the reference it was pointing to. Its not just that function alone it returns but the entire closure and that's where it becomes interesting 
function x() {
    var a = 7;
    function y() {
        console.log(a)
    }
    return y
}
var z = x();
console.log(z)
z()
#returns 7

Closure Used in:
1. module design pattern
2. currying
3. functions like once
4. memoize
5. maintaining state in async world
6. set timeouts
7. iterators
8. data hiding and encapsulation: As now no one in global scope can just directly change the variable value, and they have to use closure fn to update the value.
*/

/*
function x() {
    for (var i; i <= 5; i++)
    setTimeout(()=> {
        console.log(i)
    }, i* 1000)
    return y
}
// Prints 6 everytimeas for loop will get executed first and then all the settimeout
fn in callstack will be refering to same i which is equal to 6
// if u change it to let i, every time a new copy of i is created as let is block scoped so it will work
// to work with var, u can put settimeout inside another fn and pass i as parameter
and run that fn in the loop. this way every iteration will have new copy of i which setimeout will have reference to.
*/

/*
- using function constructor in JS with closure:
function Counter() {
    var count = 0
    this.incrementCounter = function() {
        count ++;
        console.log(count)
    }
    this.decrementCounter = function() {
        count --;
        console.log(count)
    }
}

counter1 = new Counter(); # for constructor fn we need to use new keyword
counter1.incrementCounter()
counter1.incrementCounter()
counter1.decrementCounter()
counter1.decrementCounter()

Disadvantages of Closure-
1. Overconsumption of memory- As everytim closure is formed, the closed over variables are not garbage collected, leading to accumulation of memory use which can result in memory leaks. 
Modern browser like V8 chrome engine have smart garbage collection mechanism which somehow finds out unreachable variables and collects them as garbage variables.
Example of smart garbage collection:
function a() {
    var x = 0, z= 1;
    funcion b() {
        console.log(x)
    }
    return b
}
var y = a()
y();
- here x is not garbage collected as it will be needed in future by closure, but z
is garbage collected.
*/

/*
a();
b();
// Function stmt/ function declaration same thing
function a() {
    console.log("a called")
}

// Function expression
var b = function () {
    console.log("b called")
}

Difference btw function stmt and function expression is the way they are hoisted
Above, a() will run while b() will give Type error as b value will be undefined initially.

// Anonymous fun- function without a name
// syntac error function needs a name
function () {}
// valid syntax
var x = function() {}

// Named Function Expression
var a = function xyz() {
    console.log(xyz) # will run as xyz is in local memory
}
a() # will run
xyz() # reference error as xyz is not in global scope

# parameter- passed in function expression
# Arguments- passed when we invoke function

// First class function- The ability to use fn as values
(when passed as arguments or return from function, Assigned as an identifier (variable) value).
 Fn are also called first class citizens.

*/

/*
callback function- are the function passed into another function. which helps JS to have asynchronous behaviour.
Everything is JS is called using single callstack or Main thread. Any operation that blocks the callstack, is called blocking the main thread.

Event listner- On Event, it pushed the event listner as callback function in call stack and runs it.
Remove Event listner and Garbage collection- Remove listner helps in removing unneccessary memory occupied by the closure scope of listner which no longer is needed.
*/

/*
- Eventloop, callstack, web apis, callback queue, microtask queue
Web Apis's Inside browser provides this to call stack:
setTimeout, DOM Api's, fetch(), localstorage, console, location

Say when setTimeout is called, it gets registered in browser, then once timer is over,
the callback fn is pushed in callback queue and then eventloop puts it into call stack

Eventloop has single task to observe all this task queue(callback and microtask) and callstack, and when callstack is empty it puts task from queue into call stack.

Microtask queue- this queue has higher priority than callback queue. so eventloop will 
execute the task of this queue before callback queue.
task which comes under it
1. All the fn which comes through promise will go inside microtask queue like fetch calls.
2. Mutation observer which keeps checking whether some mutation in dom tree or not.

Starvation of callback queue-
When microtask queue keep getting created and callback queue task doesnt get chance to
execute.

*/
/*
Javascript run time Envrionment ex; Browser, Node.js etc
Js engine of  chrome- v8, mozilla- spider monkey(1st engine), edge-chakra
JS is JIt(just in time) compilation which uses both interpreter to execute code and compiler to optimise code. JS engine has 3 phases- 
1. parsing creates AST(abstract syntax tree), 
2. compilation 3. execution
Memory heap- All the memory stored there, garbage collector,call stack in sync with it.
optimisation techniques- mark and sweep alog used by garbage collector,
inlning, copy elison, inline caching
*/

/*
Higher order function- Functions in which functions are passed as arguments
or returns a function, are called higher order functions.
Ex. map function is Higher order function.
In other words, you can use higher order functions to make a function polymorphic.
As you can see, higher order functions can be a whole lot more reusable and versatile than their first order cousins. 

Higher order function is in contrast to first order functions, which don’t take
a function as an argument or return a function as output.
Ex. we can reduce our repeated code of calculating specifc thing every time by:
    const area = (radius) => {...}
    const circumference=  (radius) => {...}
    const diamter = (radius) => {...}
    const calculate = function(logic) {...}
    # calculate here is higher order function.
    -----


*/
