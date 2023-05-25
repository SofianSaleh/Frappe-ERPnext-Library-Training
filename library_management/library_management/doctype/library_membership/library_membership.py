# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership(Document):
	

	def before_save(self):
		print(frappe.get_doc({
			"doctype": 'Library Member',
			"full_name": self.full_name
		})	)
		# frappe.msgprint(frappe.get_doc({
		# 	"doctype": 'Library Member',
		# 	"full_name": self.full_name
		# }))
		

	def before_submit(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				'library_member': self.library_member,
				'docstatus': DocStatus.submitted(),
				'to_date': (">", self.from_date)
			}
		)
		print(exists)
		if exists:
			frappe.throw("There is an active membership for this member")

		loan_period = frappe.db.get_single_value('Library Settings', 'loan_period')
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
