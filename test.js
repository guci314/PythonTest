
Jupyter.notebook.events.one('kernel_ready.Kernel', function () {
    IPython.toolbar.add_buttons_group([
        {
            'label': 'run qtconsole',
            'icon': 'icon-terminal', // select your icon from http://fortawesome.github.io/Font-Awesome/icons
            'callback': function () {
                IPython.notebook.kernel.execute('%qtconsole')
            }
        }
        // add more button here if needed.
    ]);

    IPython.keyboard_manager.edit_shortcuts.add_shortcut('ctrl-enter', {
        help: "run cell and keep focus", //This is optional
        handler: function (event) {
            IPython.notebook.execute_cell();
            IPython.notebook.edit_mode();
            return false;
        }
    }
    );

    IPython.keyboard_manager.edit_shortcuts.add_shortcut('ctrl-x', {
        help: "jedi", //This is optional
        handler: function (event) {
            var index = IPython.notebook.get_edit_index();
            IPython.notebook.execute_cells([0]);
            IPython.notebook.get_cell(index).focus_cell();
            IPython.notebook.edit_mode();
            return false;
        }
    }
    );
});
