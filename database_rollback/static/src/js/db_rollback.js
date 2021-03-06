// Copyright (C) 2019 Cojocaru Aurelian Marcel PFA
// @author Marcel Cojocaru <marcel.cojocaru@gmail.com>
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
openerp.database_rollback = function (instance) {
    'use strict';
    instance.database_rollback.RollbackButtonsWidget = instance.web.Widget
        .extend({

            template:'database_rollback.ButtonsWidget',

            renderElement: function () {
                var self = this;
                this._super();
                this.$el.show();
                this.$el.find('.activate').on('click', function () {
                    self.$el.find('.activate').css("background-color", "green")
                        .css("color", "white");
                    self.rpc('/database_rollback/activate', {});
                });

                this.$el.find('.rollback').on('click', function () {
                    self.$el.find('.activate')
                        .css("background-color", "buttonface")
                        .css("color", "#777");
                    self.rpc('/database_rollback/rollback', {});
                });
            },
        });

    instance.web.UserMenu.include({
        do_update: function () {
            this._super();
            var self = this;
            this.update_promise.done(function () {
                if (!_.isUndefined(self.rollbackButtons)) {
                    return;
                }
                self.rollbackButtons = new instance.database_rollback
                    .RollbackButtonsWidget(self);
                self.rollbackButtons.prependTo(
                    instance.webclient.$('.oe_systray'));
            });
        },
    });

};
