App.View.Example = Ember.View.extend({
	templateName: 'example',

	title: null,
	description: null,
	example: null,

	content: {},

	didInsertElement: function() {
		var content = this.get('content');
		content.didInsertElement = function() {

			$('<pre />', {
				'class': 'prettyprint lang-html linenums',
				text: this.$().html().trim()
			}).appendTo(this.$());

			$('<h4 />', {
				text: 'Output'
			}).prependTo(this.$());

			if (templates[content.templateName]) {

				$('<pre/>', {
					text: templates[content.templateName].trim(),
					'class': 'prettyprint lang-html linenums'
				}).prependTo(this.$());

				$('<h4 />', {
					text: 'Handlebars source'
				}).prependTo(this.$());

			}


			$('<pre />', {
				text: [
					'MyView = Ember.View.extend(',
					JSON.stringify(content, null, 2).trim(),
					');'
				].join(''),
				'class': 'prettyprint lang-javascript linenums'
			}).prependTo(this.$());
			$('<h4 />', {text: 'JavaScript'}).prependTo(this.$());



			prettyPrint();
		}
		Ember.View.create(
			content
		).appendTo(this.$().find('.example'));
	}
});