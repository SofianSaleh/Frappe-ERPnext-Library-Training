# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
	def before_submit(self):
		if self.type == 'Issue':
			# Validate Issue
			self.validate_issue()
			self.validate_maximum_limit
			article = frappe.get_doc("Article Library", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == 'Return':
			self.validate_return()
			article = frappe.get_doc("Article Library", self.article)
			article.status = "Available"
			article.save()

	def validate_issue(self):
		# Validate Membership
		self.validate_membership()
		article = frappe.get_doc("Article Library", self.article)
		if article:
			frappe.throw('Article is already issued by another member')

	def validate_return(self):
		article = frappe.get_doc("Article Library", self.article)
		if article.status == 'Available':
			frappe.throw('Article cannot be returned without being issued first')

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value('Library_settings','max_articles')
		count = frappe.db.count('Library Transactions',{'library_member': self.library_member, 'type':"Issue", 'docstatus': DocStatus.submitted()})
	
	def validate_membership(self):
		valid_membership = frappe.db.exists(
			'Library Membership',
			{
				'library_member': self.library_member,
				'docstatus': DocStatus.submitted(),
				'from_date': ('<', self.date),
				'to_date': ('>', self.date),
			},
		)
		print(valid_membership)
		if not valid_membership:
			frappe.throw('The member dose not have a valid membership')
	
