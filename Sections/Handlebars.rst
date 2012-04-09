==========
Handlebars
==========

Describing Your UI with Handlebars
==================================

Handlebars templates are stored in the applications HTML source using `<script>`
tags.

::

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

`Ember.View` renders Handlebars and insert them into DOM

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
Those placeholders look like in the HTML code of your running Application:

::

	My new car is
	<script id="metamorph-0-start" type="text/x-placeholder"></script>
	blue
	<script id="metamorph-0-end" type="text/x-placeholder"></script>.



{{#if}}, {{else}}
=================

::

	App.SayHelloView = Ember.View.extend({
		person: Ember.Object.create({
			firstName: "Joy",
			lastName: "Clojure"
		})
	});

Only displays the part of the template, if the object `person` exists

::

	{{#if person}}
		Welcome back, <b>{{person.firstName}} {{person.lastName}}</b>!
	{{else}}
		Please log in.
	{{/if}}


{{#unless}}
============


`{{#unless}}` is used to render a block if a values is false

::

	{{#unless hasPaid}}
		You owe: ${{total}}
	{{/unless}}

{{#with}}
=========

By default, the context is the Ember.View to which the template belongs.

`{{#with}}` changes the context of the block you pass to it


::

	{{#with person}}
		Welcome back, <b>{{firstName}} {{lastName}}</b>!
	{{/with}}


Binding Element Attributes with {{bindAttr}}
============================================

putting attributes into the HTML template

::

	App.LogoView = Ember.View.extend({
		logoUrl: 'http://www.mycorp.com/images/logo.png'
	});

::

	<div id="logo">
		<img {{bindAttr src="logoUrl"}} alt="Logo">
	</div>

::

	App.InputView = Ember.View.extend({
		isDisabled: true
	});

::

	<input type="checkbox" {{bindAttr disabled="isDisabled"}}>


Binding Class Names with {{bindAttr}}
=====================================

::

	App.AlertView = Ember.View.extend({
		priority: "p4",
		isUrgent: true
	});

::

	<div {{bindAttr class="priority"}}>
		Warning!
	</div>

::

	<div class="p4">
		Warning!
	</div>



Binding Class Names with {{bindAttr}} with boolean
==================================================

::

	<div {{bindAttr class="isUrgent"}}>
		Warning!
	</div>

::

	<div class="is-urgent">
		Warning!
	</div>

Binding multiple Classes
========================

::

	<div {{bindAttr class="isUrgent priority"}}>
		Warning!
	</div>


if urgent is true the class will be added, otherwise it will be removed

::

	<div {{bindAttr class="isUrgent:urgent"}}>
		Warning!
	</div>


Handling Events with {{action}}
===============================

attaching an `click` event to `edit()

::

	<a href="#" {{action "edit" on="click"}}>Edit</a>

targeting another view

::

	<a href="#" {{action "edit" target="parentView"}}>Edit</a>

::

	App.ListingView = Ember.View.extend({
		templateName: 'listing',

		edit: function(event) {
			event.view.set('isEditing', true);
		}
	});

::

	<a href="#" data-ember-action="3">Edit</a>



Building a View Hierarchy
=========================

* till now templates only for single view
* target is creating a hierarchy of views to encapsulte different areas on a page
	* CRUD actions
* seperating views for handling their events and maintaining the properties


Child View Templates with {{view}}
==================================

::

	// Define parent view
	App.UserView = Ember.View.extend({
		templateName: 'user',
		firstName: "Albert",
		lastName: "Hofmann"
	});
	// Define child view
	App.InfoView = Ember.View.extend({
		templateName: 'info',
		posts: 25,
		hobbies: "Riding bicycles"
	});

::

	User: {{firstName}} {{lastName}}
	{{#view App.InfoView}}
		<b>Posts:</b> {{posts}}
		<br>
		<b>Hobbies:</b> {{hobbies}}
	{{/view}}


Setting Up Bindings
===================

::

	App.userController = Ember.Object.create({
		content: Ember.Object.create({
			firstName: "Albert",
			lastName: "Hofmann",
			posts: 25,
			hobbies: "Riding bicycles"
		})
	});

::

	App.UserView = Ember.View.extend({
		templateName: 'user',
		firstNameBinding: 'App.userController.content.firstName',
		lastNameBinding: 'App.userController.content.lastName'
	});

::

	User: {{firstName}} {{lastName}}
	{{#view App.UserView postsBinding="App.userController.content.posts"
		hobbiesBinding="App.userController.content.hobbies"}}
		<b>Posts:</b> {{posts}}
		<br>
		<b>Hobbies:</b> {{hobbies}}
	{{/view}}

Modifying a View's HTML
=======================

* New instances of Ember.View create by default a `<div>` element.
* You can override this by passing a `tagName` parameter:
* `id` and `class` also possible
* `classBinding`

::

	{{view App.InfoView tagName="span"}}

::

	{{view App.InfoView id="info-view"}}

::

	{{view App.AlertView classBinding="isUrgent priority"}}


Displaying a List of Items
==========================

for enumerating over a list of objects use `{{each}}`

::

	App.PeopleView = Ember.View.extend({
		people: [ { name: 'Yehuda' },
			{ name: 'Tom' } ]
	});

::

	<ul>
		{{#each people}}
			<li>Hello, {{name}}!</li>
		{{/each}}
	</ul>

create a view for every item

::

	{{#each App.peopleController}}
		{{#view App.PersonView contentBinding="this"}}
			{{content.firstName}} {{content.lastName}}
		{{/view}}
	{{/each}}


Writing Custom Helpers
======================

::

	Handlebars.registerHelper('highlight', function(property) {
		var value = Ember.getPath(this, property);
		return new Handlebars.SafeString('<span class="highlight">'+value+'</span>');
	});

::

	{{highlight name}}

::

	<span class="highlight">Peter</span>

Included Views
==============

* Ember.Button
* Ember.Checkbox
* Ember.TextField
* Ember.Select
* Ember.TextArea