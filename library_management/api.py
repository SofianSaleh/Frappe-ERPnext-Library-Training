import frappe


@frappe.whitelist()
def get_all_articles():
    print('hi')
    articles = frappe.db.get_list('Article Library', 
                                  fields=[
                                      'article_name','author', 'description','isbn','status','publisher','image'
                                      ]
                                      )
    print(articles)
    return articles


@frappe.whitelist()
def get_article_by_isbn(isbn):
    print('hi')
    article = frappe.db.get_list('Article Library', 
                                  fields=[
                                      'article_name','author', 'description','isbn','status','publisher','image'
                                      ],
                                      filters={'isbn':isbn}
                                      )
    
    print(article)
    return article

@frappe.whitelist()
def update_article(updateData,isbn):
    pass