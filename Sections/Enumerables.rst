===========
Enumerables
===========

Enumerables
===========

What Are Enumerables?
=====================

In general, Ember objects that represent lists implement the Enumerable interface. Some examples:

* Array: Ember extends the native JavaScript Array with the Enumerable interface.
* ArrayProxy: A construct that wraps a native Array and adds additional functionality for the view layer.
* Set: An object that can quickly answer whether it includes an object.


Parameters
==========

The callbacks to Enumerable methods take three arguments:

* item: the item for the current iteration.
* index: an Integer, counting up from 0.
* self: the Enumerable itself.

Enumeration
===========


To enumerate all the values of an enumerable object, use the `forEach()` method:

::

	enumerable.forEach(function(item, index, self) {
		console.log(item);
	});


To invoke some method on each element of an enumerable object, use the `invoke()` method:

::

	Person = Ember.Object.extend({
		sayHello: function() {
			console.log("Hello from " + this.get('name'));
		}
	});
	var people = [
		Person.create({ name: "Juan" }),
		Person.create({ name: "Charles" })
	]
	people.invoke('sayHello');

	// Hello from Juan // Hello from Charles


First and Last
==============

You can get the first or last object from an Enumerable by getting `firstObject` or `lastObject`.

::

	[1,2,3].get('firstObject') // 1
	[1,2,3].get('lastObject')  // 3


Converting to Array
===================

This one is simple. To convert an Enumerable into an Array, simply call its `toArray()` method.

Transforming
------------

You can transform an Enumerable into a derived Array by using the `map()` method:

::

	['Goodbye', 'cruel', 'world'].map(function(item, index, self) {
		return item + "!";
	});

	// returns ["Goodbye!", "cruel!", "world!"]

Setting and Getting on Each Object
==================================

A very common use of `forEach()` and `map()` is to get (or set) a property on each element. You can use the `getEach()` and `setEach()` methods to accomplish these goals.

::

	var arr = [Ember.Object.create(), Ember.Object.create()];

	// we now have an Array containing two Ember.Objects

	arr.setEach('name', 'unknown');
	arr.getEach('name') // ['unknown', 'unknown']

Filtering
=========

Another common task to perform on an Enumerable is to take the Enumerable as input, and return an Array after filtering it based on some criteria.

* `filter()` expects the callback to return `true` if Ember should include in final Array
* and `false` or `undefined` if not

::

	var arr = [1,2,3,4,5];

	arr.filter(function(item, index, self) {
		if (item < 4) { return true; }
	})

	// returns [1,2,3]


Filtering object based
======================

The `filterProperty()` is used for filter a set of objects upon the value of some property

::

	Todo = Ember.Object.extend({
		title: null,
		isDone: false
	});
	todos = [
		Todo.create({ title: 'Write code', isDone: true }),
		Todo.create({ title: 'Go to sleep' })
	];
	todos.filterProperty('isDone', true);
	// returns an Array containing just the first item



just the first matched value is wanted instead of an Array

* `find()` and `findProperty()`
* which work just like `filter()` and `filterProperty()`, but return only one item.


Aggregate Information (All or Any)
==================================

If you want to find out whether every item in an Enumerable matches some condition, you can use the every()` method:

::

	Person = Ember.Object.extend({
		name: null,
		isHappy: false
	});
	var people = [
		Person.create({ name: 'Yehuda', isHappy: true }),
		Person.create({ name: 'Majd', isHappy: false })
	];

	people.every(function(person, index, self) {
		if(person.get('isHappy')) { return true; }
	});
	// returns false

Aggregate Information (All or Any)
==================================

If you want to find out whether at least one item in an Enumerable matches some conditions, you can use the `some()` method:

::

	people.some(function(person, index, self) {
		if(person.get('isHappy')) { return true; }
	});
	// returns true

Just like the filtering methods, the every and some methods have analogous `everyProperty()` and `someProperty() methods.

::

	people.everyProperty('isHappy', true) // false
	people.someProperty('isHappy', true)  // true


