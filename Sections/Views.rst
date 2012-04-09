=====
Views
=====

Views In-Depth
==============

Customizing views to needs

Handling Events
===============

* no need of registering event listeners to elements
* simply implement the nameof the event to your view

::

	{{#view App.ClickableView}}
		This is a clickable area!
	{{/view}}

::

	App.ClickableView = Ember.View.extend({
		click: function(evt) {
			alert("ClickableView was clicked!");
		}
	});


Manually Managed Views with Ember.ContainerView
===============================================

* the `childViews` array of the instance of `Ember.ContainerView` is editable

::

	var container = Ember.ContainerView.create();
	container.append();
	var coolView = App.CoolView.create(),
		childViews = container.get('childViews');
	childViews.pushObject(coolView);

* specifiy childViews as keys and properties
* views are added to the child views array

::

	var container = Ember.ContainerView.create({
		childViews: ['firstView', 'secondView'],
		firstView: App.FirstView,
		secondView: App.SecondView
	});

Render Pipeline
===============

* other rendering than Handlebars
* override `render()`

::

	App.CoolView = Ember.View.create({
		render: function(buffer) {
			buffer.push("<b>This view is so cool!</b>");
		}
	});

* other template engines possible
* value updates your responsibility


Customizing the HTML Element
============================
`tagName`

::

	App.MyView = Ember.View.extend({
		tagName: 'span'
	});


`classNames`

::

	App.MyView = Ember.View.extend({
		classNames: ['my-view']
	});

`className` binding like in Handlebars chapter


`attributeBindings`

::

	App.MyView = Ember.View.extend({
		tagName: 'a',
		attributeBindings: ['href'],
		href: "http://emberjs.com"
	});