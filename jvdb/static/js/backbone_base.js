var models = {};

models.Piece = Backbone.Model.extend({
    urlRoot: '/api/piece',
    defaults: {
        id: null,
        name: '',
        description: '',
    },
});

/* Collections. */
var collections = {};

collections.Pieces = Backbone.Collection.extend({
    model: models.Piece
});
