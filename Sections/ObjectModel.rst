============
Object Model
============

The Ember Object Model
======================

Ember ships with a powerful object model.

Defining an object
------------------

::

	Person = Ember.Object.extend({
		say: function(thing) {
			alert(thing);
		}
	});

Making a new instance
---------------------

::

	var person = Person.create();
	person.say("Hello");

Add new properties during instantiation
=======================================

::

	var tom = Person.create({
		name: "Tom Dale",

		helloWorld: function() {
			this.say("Hi my name is " + this.get('name'));
		}
	});

	tom.helloWorld();

Calling the parent method
-------------------------

::

	var yehuda = Person.create({
		name: "Yehuda Katz",

		say: function(thing) {
			var name = this.get('name');
			this._super(name + " says: " + thing);
		}
	});

Subclassing
===========

::

	var LoudPerson = Person.extend({
		say:function (thing) {
			this._super(thing.toUpperCase());
		}
	});

Reopening Classes and Instances
===============================

Use `reopen()` it's possible to change instances, like adding or overwriting
properties / methods and call `this._super()`.

::

	Person.reopen({
		isPerson: true
	});
	Person.create().get('isPerson'); // true


::

	Person.reopen({
		say: function(thing) {
			this._super(thing + "!");
		}
	});

Use `reopenClass()` to extend the class

::

	Person.reopenClass({
		createMan: function() {
			return Person.create({isMan: true});
		}
	}
	Person.createMan().get('isMan') // true


Computed Properties (Getter only)
=================================

::

	Person = Ember.Object.extend({
		firstName: null,
		lastName: null,

		fullName: function() {
			var firstName = this.get('firstName');
			var lastName = this.get('lastName');

			return firstName + ' ' + lastName;
		}.property('firstName', 'lastName')
	});

	var tom = Person.create({
		firstName: "Tom",
		lastName: "Dale"
	});

	tom.get('fullName');

Getter without Embers prototype extensions
==========================================

* property method defines the function as a computed property
* defines its dependencies
* Those dependencies will come into play later for bindings and observers.

::

	Person = Ember.Object.extend({
		firstName: null,
		lastName: null,

		fullName: Ember.computed(function() {
			var firstName = this.get('firstName');
			var lastName = this.get('lastName');

			return firstName + ' ' + lastName;
		}).property('firstName', 'lastName')
	});



Computed Properties (Setters)
=============================

::

	Person = Ember.Object.extend({
		firstName: null,
		lastName: null,

		fullName: Ember.computed(function(key, value) {
			if (arguments.length === 1) {
					// getter
				var firstName = this.get('firstName');
				var lastName = this.get('lastName');
				return firstName + ' ' + lastName;
			} else {
					// setter
				var name = value.split(" ");
				this.set('firstName', name[0]);
				this.set('lastName', name[1]);
				return value;
			}
		}).property('firstName', 'lastName')
	});
	var person = Person.create();
	person.set('fullName', "Peter Wagenet");
	person.get('firstName') // Peter
	person.get('lastName') // Wagenet

Observers
=========

observe an object by using `addObserver()`

::

	Person = Ember.Object.extend({
		firstName: null
	});

	var person = Person.create({firstName: "Yehuda"});

	person.addObserver('firstName', function() {
		console.log('firstName changed');
	});

	person.set('firstName', "Brohuda");

Observe array changes
=====================

::

	App.todosController = Ember.Object.create({
		todos: [
			Ember.Object.create({ isDone: false })
		],

		remaining: function() {
			var todos = this.get('todos');
			return todos.filterProperty('isDone', false).get('length');
		}.property('todos.@each.isDone')
	});

* `@each` as special key instructs Ember to update bindings and fire observers when:
	* `isDone` is changed
	* item is added to the array or removed
	* the todos property of the controller is moved to a different array


Example for observing array changes
===================================

::

	var todos = App.todosController.get('todos');
	var todo = todos.objectAt(1);
	todo.set('isDone', true);

	App.todosController.get('remaining');
	// 0

	todo = Ember.Object.create({ isDone: false });
	todos.pushObject(todo);

	App.todosController.get('remaining');
	// 1


Bindings
========

::

	App.wife = Ember.Object.create({
		householdIncome: 80000
	});

	App.husband = Ember.Object.create({
		householdIncomeBinding: 'App.wife.householdIncome'
	});

	App.husband.get('householdIncome');

	App.husband.set('householdIncome', 90000);
	App.wife.get('householdIncome');


* bindings create a `link` between two properties
* bindings can connect properties of the same, or across two different objects
* can be used with any object
* are updated after the application code has finished



One-Way Bindings
================


::

	App.user = Ember.Object.create({
		fullName: "Kara Gates"
	});

	App.userView = Ember.View.create({
		userNameBinding: Ember.Binding.oneWay('App.user.fullName')
	});

	// Changing the name of the user object changes
	// the value on the view.
	App.user.set('fullName', "Krang Gates");
	// App.userView.userName will become "Krang Gates"

	// ...but changes to the view don't make it back to
	// the object.
	App.userView.set('userName', "Truckasaurus Gates");
	App.user.get('fullName'); // "Krang Gates"

* one-way bindings used for performance improvements

What Do I Use When?
===================

* use computed properties 'only' to return a combined value of multiple properties
* use observers when you need to perform an action after some property has changed
* use bindings to keep objects in sync