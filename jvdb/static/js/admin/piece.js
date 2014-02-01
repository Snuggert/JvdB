var pieceViewView, pieceNewView;

$(function() {
    pieceViewView = new pieceViewView({el: '#customers tbody'});
    // pieceNewView = new pieceNewView();

    $('#new-btn').click(function() {
        $(this).hide();
        customerNewView.show();
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
            me.render();
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
        var customer = this.customers.get(id);

        var customerEditView = new CustomerEditView({model: customer,
            el: $tr});

        $('.associations, .edit, .remove').hide();
    },
    remove: function(event) {
        if (!confirm('Are you sure?')) {
            return;
        }

        var me = this;
        var $this = $(event.currentTarget);
        var $tr = find_tr($this);
        var id = $tr.data('id');
        var customer = this.customers.get(id);

        customer.destroy({
            success: function() {
                clearflash();
                flash('Customer removed successfully', 'success');

                me.update();
            }, error: function(response) {
                ajax_error_handler(response);
            }
        });
    }
});

// CustomerEditView = Backbone.View.extend({
//     initialize: function() {
//         this.render();
//     },
//     render: function() {
//         var template = _.template($('#customer-edit-template').html(),
//             {customer: this.model});
//         this.$el.html(template);
//     },
//     events: {
//         'click button.save': 'save',
//         'click button.cancel': 'cancel'
//     },
//     save: function(event) {
//         var me = this;
//         var $this = $(event.currentTarget);
//         var $tr = find_tr($this);

//         set_form_values(this.model, $tr);
//         this.model.save({}, {
//             success: function() {
//                 clearflash();
//                 flash('Customer saved successfully', 'success');

//                 me.remove();
//                 customerViewView.update();
//             }, error: function(model, response) {
//                 ajax_error_handler(response);
//             }
//         });
//     },
//     cancel: function(event) {
//         this.remove();
//         customerViewView.update();
//     }
// });

// CustomerNewView = Backbone.View.extend({
//     el: '#new-customer',
//     initialize: function() {
//         this.hide();
//     },
//     show: function() {
//         this.$el.show();
//         this.delegateEvents();
//         this.render();
//     },
//     hide: function() {
//         this.$el.hide();
//         this.undelegateEvents();
//     },
//     render: function() {
//         var template = _.template($('#customer-new-template').html());
//         this.$el.html(template);
//     },
//     events: {
//         'click button#save-new': 'save',
//         'click button#cancel-new': 'cancel'
//     },
//     save: function(event) {
//         var me = this;
//         var $save_btn = $('button#save-new');

//         $save_btn.attr('disabled', true);

//         var customer = new models.Customer();
//         set_form_values(customer, $('#new-customer-form'));

//         customer.save({}, {
//             success: function() {
//                 clearflash();
//                 flash('Customer saved successfully', 'success');

//                 me.hide();
//                 $('#new-btn').show();

//                 customerViewView.update();
//             }, error: function(model, response) {
//                 ajax_error_handler(response);
//                 $save_btn.attr('disabled', false);
//             }
//         });
//     },
//     cancel: function(event) {
//         this.hide();
//         $('#new-btn').show();
//     }
// });
