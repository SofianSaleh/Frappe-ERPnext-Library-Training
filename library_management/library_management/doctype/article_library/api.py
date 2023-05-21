import frappe
import requests
# https://openlibrary.org/isbn/0-671-12805-1.JSON

@frappe.whitelist()
def get_all_articles():
	return frappe.db.sql('''select * from `tabArticle Library`''')


# @frappe.whitelist()
# def get_publisher(isbn):
#     frappe.msgprint(isbn)
#     print('hello world')
#     url= f'https://openlibrary.org/isbn/{isbn}.json'
#     frappe.msgprint(url)
#     # url = 'https://openlibrary.org/isbn/0-671-12805-1.json'
#     try:
#         response = requests.get(url).json()
#         image = f'https://covers.openlibrary.org/b/id/{response["covers"][0]}-L.jpg'
#         authorsURL = f'https://openlibrary.org{response["authors"][0]["key"]}.json'
#         authorResponse = requests.get(authorsURL).json()
#         data = {
#                 "title": response["title"],
#                 "author": authorResponse["name"],
#                 "image": image,
#                 "publisher": response['publishers'][0]
#         }
#         return data
#     except Exception as e:
#          frappe.msgprint(e)
