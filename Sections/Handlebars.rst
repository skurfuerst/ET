==========
Handlebars
==========

Describing Your UI with Handlebars
==================================

Handlebars templates are stored in the applications HTML source using `<script>`
tags. ::

	<html>
		<head>
			<script type="text/x-handlebars"
					data-template-name="say-hello">
				Hello, <b>{{name}}</b>,
					you are using {{MyApp.name}}
			</script>
		</head>
	</html>

Ember.View
==========

::

	var view = Ember.View.create({
		templateName: 'say-hello',
		name: "Bob"
	}).appendTo('#element');

Append to body
--------------

::

	view.append();

Remove view from DOM
--------------------

::

	view.remove();

Display a property
==================

::

	My new car is {{color}}.

Display a global property
-------------------------

::

	My app is named {{MyApp.name}}

Placeholders
============

Ember.js adds placeholders to find what to do when a property changes.
Those placeholders look like: ::

	My new car is
	<script id="metamorph-0-start" type="text/x-placeholder"></script>



{{#if}}, {{else}}, and {{#unless}}
----------------------------------





{{#with}}
=========




Binding Element Attributes with {{bindAttr}}
============================================


Binding Class Names with {{bindAttr}}
=====================================


Handling Events with {{action}}
===============================


Building a View Hierarchy
=========================


{{view}}
========


Setting Child View Templates
============================


Setting Up Bindings
===================


Modifying a View's HTML
=======================



Displaying a List of Items
==========================



Writing Custom Helpers
======================