import frappe
import requests


@frappe.whitelist()
def get_article_by_isbn(isbn):
    article  = frappe.get_list('Article Library',
                               filters={'isbn': isbn}, 
                               fields=['article_name', 'author', 'isbn', 'publisher', 'status', 'image', 'description', 'owner', 'creation'])
    return article



@frappe.whitelist()
def populate_article_data (isbn):
    
    '''This function gets called when the article library is saved, and calls the open library api 
    to fetch all the information about the article using the ISBN
    '''
   

    url= f'https://openlibrary.org/isbn/{isbn}.json'

    try:
        '''Fetching the main article object'''

        response = requests.get(url).json()

        '''Fetching the image from the main object'''
        image = f'https://covers.openlibrary.org/b/id/{response["covers"][0]}-L.jpg'

        '''Fetching the author using the information from the main JSON object'''
        authorsURL = f'https://openlibrary.org{response["authors"][0]["key"]}.json'

        authorResponse = requests.get(authorsURL).json()
        data = {
                "article_name": response.get("title"),
                "author": authorResponse.get("name"),
                "image": image,
                "publisher": response.get('publishers')[0],
                "description":response.get("description") if response.get("description") else "No description is available",
                "published": 1,
                "route": '-'.join(response.get("title").split(' ')),
                "status": 'Available'
        }
        return data
    except Exception as e:
        frappe.msgprint(e)
