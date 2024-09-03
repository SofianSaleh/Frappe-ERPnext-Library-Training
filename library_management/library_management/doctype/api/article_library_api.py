import frappe
import requests
from frappe.utils import now


@frappe.whitelist()
def get_all_articles():
    print("hi")
    articles = frappe.db.get_list(
        "Article Library",
        fields=[
            "article_name",
            "author",
            "description",
            "isbn",
            "status",
            "publisher",
            "image",
        ],
    )
    print(articles)
    return articles


@frappe.whitelist()
def get_article_by_isbn(isbn):
    article = frappe.get_list(
        "Article Library",
        filters={"isbn": isbn},
        fields=[
            "article_name",
            "author",
            "isbn",
            "publisher",
            "status",
            "image",
            "description",
            "owner",
            "creation",
        ],
    )
    return article


@frappe.whitelist()
def get_article_by_date(creation):
    print(now())
    last_date = now()
    article = frappe.get_list(
        "Article Library",
        filters=[["creation", ">=", creation]],
        fields=[
            "article_name",
            "author",
            "isbn",
            "publisher",
            "status",
            "image",
            "description",
            "owner",
            "creation",
        ],
    )
    return {"article": article, "date": last_date}


@frappe.whitelist()
def populate_article_data(isbn):
    """This function gets called when the article library is saved, and calls the open library api
    to fetch all the information about the article using the ISBN
    """
    print("hi")

    url = f"https://openlibrary.org/isbn/{isbn}.json"

    try:
        """Fetching the main article object"""
        authorResponse = {}
        response = requests.get(url).json()

        """Fetching the image from the main object"""
        image = f'https://covers.openlibrary.org/b/id/{response["covers"][0]}-L.jpg'

        """Fetching the author using the information from the main JSON object"""
        if response.get("authors"):
            authorsURL = f'https://openlibrary.org{response["authors"][0]["key"]}.json'
            authorResponse = requests.get(authorsURL).json()

        data = {
            "article_name": response.get("title"),
            "author": (
                authorResponse.get("name") if authorResponse.get("name") else None
            ),
            "image": image,
            "publisher": response.get("publishers")[0],
            "description": (
                response.get("description")
                if response.get("description")
                else "No description is available"
            ),
            "published": 1,
            "route": "-".join(response.get("title").split(" ")),
            "status": "Available",
        }
        return data
    except Exception as e:
        frappe.throw(e)


@frappe.whitelist()
def test_func():
    try:

        las_date = requests.get("http://127.0.0.1:8001/get_date")
        print(las_date.json())
        articles_after_date = frappe.db.sql(
            f"""
                                                SELECT  
                                                article_name, 
                                                author, 
                                                isbn, 
                                                publisher, 
                                                status
                                                FROM `tabArticle Library`
                                                WHERE creation > '{las_date.json().get('result')}'
                                            """
        )
        data = {"article": articles_after_date}

        requests.post("http://127.0.0.1:8001/get_updates_2", json=data)
    except Exception as e:
        frappe.throw(e)
