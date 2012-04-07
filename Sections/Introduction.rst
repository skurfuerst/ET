============
Introduction
============

Ember.js Tutorial
=================

Introduction
============

* Rens Admiraal
* Markus Goldbeck

What is Ember.js?
=================

* Ember.js formerly called SproutCore 2.0
* a JavaScript framework for creating web applications
	* eliminate boilerplate
	* provide architecture
* based on jQuery

How is it different?
====================

* majority of application logic on client side
	* loads all needed templates / objects on page load
	* thus reducing server communication

* it helps to manage the changes in the view and the DOM, when the underlying objects change
* makes it easy to divide a application into MVC

Some key features
=================

* bindings
* computed properties
* observers
* auto-updating templates
* object model

Bindings
========

Use bindings to keep your data and UI in sync by automatically propagating changes to
objects or your view. ::

	Demo = Ember.Object.create({
		applicationNameBinding: 'App.name'
	}

One-way binding
---------------

By default bindings are 2 way, but they can be configured to be 1 way ::

	Demo = Ember.Object.create({
		applicationNameBinding: Ember.Binding.oneWay('App.name')
	}

Computed Properties
===================

Computed properties are functions, handled like it is a property of the object. ::

	Demo = Ember.Object.create({
		firstName: 'Friendly',
		lastName: 'Ghost',
		fullName: function() {
			return this.get('firstName') + ' ' + this.getLastName();
		}.property('firstName', 'lastName').cacheable();
	}

When using computed properties it's highly recommended to use the `.cacheable()` method.

Auto-updating Templates
=======================

Ember uses a templating library named `Handlebars` to add data to the DOM. ::

	<script type="text/x-handlebars">
		My app is named {{App.name}}
	</script>

Those templates are bindings-aware.