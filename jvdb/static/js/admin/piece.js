var pieceViewView;

$(function() {
    pieceViewView = new pieceViewView({el: '#pieces tbody'});
    $('#new-btn').click(function() {
        $(this).parents('.panel-body').hide();
        var pieceNewView = new PieceNewView({el: '#new-piece'});
        $(this).hide();
    });
});

pieceViewView = Backbone.View.extend({
    pieces: new collections.Pieces(),

    initialize: function() {
        this.update();
    },
    update: function() {
        var me = this;

        $.get('/api/piece/all', {}, function(data) {
            me.pieces = new collections.Pieces(data.pieces);
            $.get('/api/piece_serie/all', {}, function(data) {
                var piece_series = new collections.PieceSeries(data.piece_series);
                _.each(me.pieces.models, function(piece) {
                    piece.piece_serie = piece_series.get(piece.get('piece_serie_id'));
                });
                me.render();
            });
        });
    },
    render: function() {
        var template = _.template($('#piece-view-template').html(),
            {pieces: this.pieces.models});
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
        var piece = this.pieces.get(id);

        var pieceEditView = new PieceEditView({model: piece,
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
        var piece = this.pieces.get(id);

        piece.destroy({
            success: function() {
                clearflash();
                flash('Piece removed successfully', 'success');

                me.update();
            }, error: function(response) {
                ajax_error_handler(response);
            }
        });
    }
});

PieceEditView = Backbone.View.extend({
    initialize: function() {
        this.render();
    },
    render: function() {
        var template = _.template($('#piece-edit-template').html(),
            {piece: this.model});
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
                pieceViewView.update();
            }, error: function(model, response) {
                ajax_error_handler(response);
            }
        });
    },
    cancel: function(event) {
        this.remove();
        pieceViewView.update();
    }
});

PieceNewView = Backbone.View.extend({
    piece_series: new collections.PieceSeries(),
    initialize: function() {
        var me = this;
        $.get('/api/piece_serie/all', {}, function(data) {
            me.piece_series = new collections.PieceSeries(data.piece_series);
            me.render();
        });
    },
    render: function() {
        var template = _.template($('#piece-new-template').html(), {
            piece_series: this.piece_series.models,
        });
        this.$el.html(template);
        $('select#piece_serie_id').select2();
        var url = "/api/piece/upload"
        $('#file_upload').fileupload({
            url: url,
            dataType: 'json',
            done: function (e, data) {
                $('input#location').val(data.result.location);
            },
            progressall: function (e, data) {
                var progress = parseInt(data.loaded / data.total * 100, 10);
                $('#progress .progress-bar').css(
                    'width',
                    progress + '%'
                );
            }
        });
    },
    events: {
        'click button#save-new': 'save',
        'click button#cancel-new': 'cancel'
    },
    save: function(event) {
        var me = this;
        var $save_btn = $('button#save-new');

        $save_btn.attr('disabled', true);

        var piece = new models.Piece();
        set_form_values(piece, $('#new-piece-form'));

        var view = this;
        piece.save({}, {
            success: function() {
                clearflash();
                flash('Piece saved successfully', 'success');
                view.cancel();
                $('#new-btn').show();
                pieceViewView.update();
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
