# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt
import requests
import frappe
from frappe.website.website_generator import WebsiteGenerator


class ArticleLibrary(WebsiteGenerator):
	def before_save(self):

		'''This function gets called when the article library is saved, and calls the open library api 
		to fetch all the information about the article using the ISBN
		'''

		url= f'https://openlibrary.org/isbn/{self.isbn}.json'

		try:
			'''Fetching the main article object'''

			response = requests.get(url).json()

			'''Fetching the image from the main object'''
			image = f'https://covers.openlibrary.org/b/id/{response["covers"][0]}-L.jpg'

			'''Fetching the author using the information from the main JSON object'''
			authorsURL = f'https://openlibrary.org{response["authors"][0]["key"]}.json'

			authorResponse = requests.get(authorsURL).json()
			data = {
					"title": response.get("title"),
					"author": authorResponse.get("name"),
					"image": image,
					"publisher": response.get('publishers')[0],
					"description":response.get("description") if response.get("description") else "No description is available"
			}
			print(data)
			self.article_name = data["title"]
			self.author = data["author"]
			self.image = data["image"]
			self.publisher = data["publisher"]
			self.status = 'Available'
			self.published = 1
			self.description = data.get('description')
			route_tuple= self.article_name.split(' ')
			self.route='-'.join(route_tuple)

			print(self.description)
		except Exception as e:
			frappe.msgprint(e)

         

	