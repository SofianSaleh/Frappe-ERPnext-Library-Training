// Copyright (c) 2023, Sofian and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article Library', {
	refresh: function(frm) {
		frm.add_custom_button('Populate Fields', function(){
			if (!frm.doc.isbn){
				frappe.throw('Please enter an ISBN')
			}
			console.log(frm.doc.isbn)
			frappe.call({
				method: 'library_management.library_management.doctype.api.article_library_api.populate_article_data',
				args:{
					isbn: frm.doc.isbn,
				},
				callback: function(r){
					console.log(r.message)
					let keys = Object.keys(r.message)

					keys.forEach((key)=>{
						frm.set_value(key,r.message[key])
						frm.refresh_field(key)
					})
				}
			})
		})
	}
});
