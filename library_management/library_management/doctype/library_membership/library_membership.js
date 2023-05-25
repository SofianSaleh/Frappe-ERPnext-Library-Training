// Copyright (c) 2023, Sofian and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
		frm.add_custom_button('test',()=>{
			console.log(frm);
		});
	}
});
