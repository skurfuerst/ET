App.View.Example = Ember.View.extend({
	templateName: 'example',

	title: null,
	description: null,
	example: null,

	content: {},

	didInsertElement: function() {
		var content = this.get('content');
		content.didInsertElement = function() {

			$('<h4 />', {text: 'JavaScript'}).appendTo(this.$());
			$('<pre />', {
				text: [
					'MyView = Ember.View.extend(',
					JSON.stringify(content, null, 2).trim(),
					');'
				].join(''),
				'class': 'prettyprint lang-javascript linenums'
			}).appendTo(this.$());

			if (templates[content.templateName]) {
				$('<h4 />', {
					text: 'Handlebars source'
				}).appendTo(this.$());

				$('<pre/>', {
					text: templates[content.templateName].trim(),
					'class': 'prettyprint lang-html linenums'
				}).appendTo(this.$());
			}

			prettyPrint();
		}
		Ember.View.create(
			content
		).appendTo(this.$().find('.example'));
	}
});