var pieceSerieViewView;

$(function() {
    pieceSerieViewView = new PieceSerieViewView({el: '#piece_series tbody'});
    $('#new-btn').click(function() {
        $(this).parents('.panel-body').hide();
        var pieceSerieNewView = new PieceSerieNewView({el: '#new-piece_serie'});
        $(this).hide();
    });
});

PieceSerieViewView = Backbone.View.extend({
    piece_series: new collections.PieceSeries(),

    initialize: function() {
        this.update();
    },
    update: function() {
        var me = this;

        $.get('/api/piece_serie/all', {}, function(data) {
            me.piece_series = new collections.PieceSeries(data.piece_series);
            me.render();
        });
    },
    render: function() {
        console.log(this.piece_series.models)
        var template = _.template($('#piece_serie-view-template').html(),
            {piece_series: this.piece_series.models});
        this.$el.html(template);
    },
    events: {
        'click button.edit': 'edit',
        'click button.remove': 'remove'
    },
    edit: function(event) {
        var $this = $(event.currentTarget);
        var $tr = find_tr($this);
        var id = $tr.data('id');
        var piece_serie = this.piece_series.get(id);

        var pieceSerieEditView = new PieceSerieEditView({model: piece_serie,
            el: $tr});

        $('.edit, .remove').hide();
    },
    remove: function(event) {
        if (!confirm('Are you sure?')) {
            return;
        }

        var me = this;
        var $this = $(event.currentTarget);
        var $tr = find_tr($this);
        var id = $tr.data('id');
        var piece_serie = this.piece_series.get(id);

        piece_serie.destroy({
            success: function() {
                clearflash();
                flash('Serie succesvol verwijderd', 'success');

                me.update();
            }, error: function(response) {
                ajax_error_handler(response);
            }
        });
    }
});

PieceSerieEditView = Backbone.View.extend({
    initialize: function() {
        this.render();
    },
    render: function() {
        var template = _.template($('#piece_serie-edit-template').html(),
            {piece_serie: this.model});
        this.$el.html(template);
    },
    events: {
        'click button.save': 'save',
        'click button.cancel': 'cancel'
    },
    save: function(event) {
        var me = this;
        var $this = $(event.currentTarget);
        var $tr = find_tr($this);

        set_form_values(this.model, $tr);
        this.model.save({}, {
            success: function() {
                clearflash();
                flash('Piece saved successfully', 'success');

                me.remove();
                pieceSerieViewView.update();
            }, error: function(model, response) {
                ajax_error_handler(response);
            }
        });
    },
    cancel: function(event) {
        this.remove();
        pieceSerieViewView.update();
    }
});

PieceSerieNewView = Backbone.View.extend({
    initialize: function() {
        this.render();
    },
    render: function() {
        var template = _.template($('#piece_serie-new-template').html());
        this.$el.html(template);
    },
    events: {
        'click button#save-new': 'save',
        'click button#cancel-new': 'cancel'
    },
    save: function(event) {
        var me = this;
        var $save_btn = $('button#save-new');

        $save_btn.attr('disabled', true);

        var piece_serie = new models.PieceSerie();
        set_form_values(piece_serie, $('#new-piece_serie-form'));

        var view = this;
        piece_serie.save({}, {
            success: function() {
                clearflash();
                flash('Serie succesvol opgeslagen', 'success');
                view.cancel();
                $('#new-btn').show();
                pieceSerieViewView.update();
            }, error: function(model, response) {
                ajax_error_handler(response);
                $('button#save-new').attr('disabled', false);
            }
        });
    },
    cancel: function(event) {
        this.destroy_view();
        $('#new-btn').parents('.panel-body').show();
        $('#new-btn').show()
    },
    destroy_view: function() {

    //COMPLETELY UNBIND THE VIEW
    this.undelegateEvents();
    this.$el.html('')
    this.$el.removeData().unbind(); 
    }
});
