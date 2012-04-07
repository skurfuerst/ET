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
objects or your view.

::

	MyApp.president = Ember.Object.create({
		name: "Barack Obama"
	});
	MyApp.country = Ember.Object.create({
		presidentNameBinding: 'MyApp.president.name'
	});
	MyApp.country.get('presidentName');

One-way binding
---------------

By default bindings are two-way, but they can be configured to be one-way ::

	MyApp.country = Ember.Object.create({
		presidentNameBinding: Ember.Binding.oneWay('MyApp.president.name')
	});

Computed Properties
===================

Computed properties are functions, handled like it is a property of the object. ::

	MyApp.dateHandler = Ember.Object.create({
		currentDate: function() {
			var now = new Date();
			return now.getDate() + '-' + d.getMonth()
				+ '-' + d.getFullYear();
		}.property()
	});

When using computed properties it's highly recommended to use the `.cacheable()` method.

Auto-updating Templates
=======================

Ember uses a templating library named `Handlebars <http://handlebarsjs.com/>`_ to add data
to the DOM. ::

	<script type="text/x-handlebars">
		The President of the United States is {{MyApp.president.fullName}}.
	</script>

Those templates are bindings-aware.