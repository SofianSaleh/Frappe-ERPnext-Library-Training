# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class ArticleLibrary(WebsiteGenerator):
	def before_save(self):
		route_tuple= self.article_name.split(' ')
		self.route='-'.join(route_tuple)
