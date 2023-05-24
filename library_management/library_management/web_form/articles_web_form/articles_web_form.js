frappe.ready(function() {
	frappe.web_form.after_load = () => {
		frappe.msgprint("Please Fill All the Required Fields")
	}
	
	// frappe.web_form.validate = () =>{
	// 	let ISBN = frappe.web_form.get_value('ISBN')
	// 	let check = /^\d$/
	// 	console.log(!check.test(ISBN) , ISBN)
	// 	if(!check.test(ISBN) && ISBN){
	// 		frappe.msgprint('ISBN must be numbers')
	// 		return false
	// 	}
	// return true
	// }
})