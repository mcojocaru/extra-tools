odoo.define('web.web_database_rollback',function (require) {

    "use strict";

    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');
    var web_client = require('web.web_client');

    var ButtonsWidget = Widget.extend({

        template:'web_database_rollback.ButtonsWidget',

        renderElement: function() {
            var self = this;
            this._super();
            this.$el.show();
            this.$el.find('.activate').on('click', function(ev) {
                    self.$el.find('.activate').css("background-color", "green").css("color", "white");
                    var func = '/web_database_rollback/activate';
                    self.rpc(func, {}).done(function(res) {
                    });
            });

            this.$el.find('.rollback').on('click', function(ev) {
                    self.$el.find('.activate').css("background-color", "buttonface")
                        .css("color", "#777");
                    var func = '/web_database_rollback/rollback';
                    self.rpc(func, {}).done(function(res) {
                    });
            });
        },
    });

    SystrayMenu.Items.push(ButtonsWidget);

});
