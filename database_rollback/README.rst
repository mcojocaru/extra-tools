=================================================
Revert the changes done on the database 
=================================================

This module allows to revert the database state prior to a certain moment chosen by the user.
It is useful when you test something in Odoo and afterwards want to go back to the initial database state. 

Usage
=====

On the right side of the systray there are two buttons: Activate and Rollback
Press the Activate button (it will turn green), do any changes/actions in odoo (products, pickings, sale orders, etc) and save them.
If you want to undo all the changes, press Rollback button.
The database state will revert to the state prior to pressing Activate button.

The number of Odoo workers has to be 0.

Note that when you press Rollback button, all the changes done by other users will be lost.

Also note that, you always have to press Rollback button at the end of your testing/investigation session.
When you press the Activate button, the cursor used for accessing the db is test cursor.
The Rollback button will revert to the real odoo cursor. So in case the results seen are the ones you expect and want to keep them in the database, you have to press Rollback and do the same actions again in Odoo.

Contributors
------------

* Marcel Cojocaru <marcel.cojocaru@gmail.com>
