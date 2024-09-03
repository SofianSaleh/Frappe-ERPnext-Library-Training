// Copyright (c) 2023, Sofian and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
  refresh: function (frm) {
    // frm.add_custom_button('test',()=>{
    // 	console.log(frm);
    // });
  },
  membership_type: function (frm) {
    frm.call({
      method: "library_management.utils.generate_dates",
      args: {
        item: frm.doc.membership_type,
      },
      callback(r) {
        console.log(r);
      },
    });
  },
});
