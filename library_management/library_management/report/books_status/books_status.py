# Copyright (c) 2024, Sofian and contributors
# For license information, please see license.txt

import frappe


def get_columns():
    columns = [
        {
            "label": "Name",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Library Member",
            "width": 250,
        },
        {
            "label": "Full Name",
            "fieldname": "full_name",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": "Membership Type",
            "fieldname": "membership_type",
            "fieldtype": "Link",
            "options": "Item",
            "width": 150,
        },
        {
            "label": "From Date",
            "fieldname": "from_date",
            "fieldtype": "Date",
            "width": 150,
        },
        {
            "label": "To Date",
            "fieldname": "to_date",
            "fieldtype": "Date",
            "width": 150,
        },
    ]
    return columns


def get_data():
    # data = frappe.get_all("Article Library", fields=["article_name", "isbn", "status"])
    sql = """
			SELECT 
				l.name, l.full_name, lm.membership_type, lm.from_date, lm.to_date
            FROM `tabLibrary Member`l
            INNER JOIN `tabLibrary Membership` as lm on lm.library_member = l.name
		"""
    data = frappe.db.sql(sql, as_dict=True)

    return data


def execute(filters=None):
    columns, data = get_columns(), get_data()
    return columns, data
