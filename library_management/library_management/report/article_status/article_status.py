# Copyright (c) 2024, Sofian and contributors
# For license information, please see license.txt

import frappe


def get_columns(filters=None):
    columns = [
        {
            "label": "Article",
            "fieldname": "article_name",
            "fieldtype": "Data",
            "width": 250,
        },
        {
            "label": "ISBN",
            "fieldname": "isbn",
            "fieldtype": "Link",
            "options": "Article Library",
            "width": 100,
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "data",
            "width": 150,
        },
    ]
    return columns


def get_data(filters=None):
    data = frappe.get_all(
        "Article Library", fields=["article_name", "isbn", "status"], filters=filters
    )
    return data


def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data
