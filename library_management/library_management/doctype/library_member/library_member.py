# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMember(Document):
    #this method will run before saving custom method
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'
