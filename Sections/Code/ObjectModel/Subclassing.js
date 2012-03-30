var LoudPerson = Person.extend({
	say:function (thing) {
		this._super(thing.toUpperCase());
	}
});