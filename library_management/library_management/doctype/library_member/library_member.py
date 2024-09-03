# Copyright (c) 2023, Sofian and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    # this method will run before saving custom method
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    def on_submit(self):
        try:
            create_customer(self.name, self.first_name, self.last_name, self.territory)
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Error creating customer")
            frappe.throw(title="LMS Error", msg="Error in create customer")


def create_customer(name: str, first_name: str, last_name: str, territory: str):
    try:
        settings = frappe.get_single("Library Settings")
        customer = frappe.new_doc("Customer")
        customer.first_name = first_name
        customer.last_name = last_name
        customer.customer_name = f"{first_name} {last_name}"
        customer.territory = territory
        customer.customer_group = settings.customer_group
        customer.custom_lms_is_library_member = 1
        customer.custom_lms_library_member = name
        customer.insert()
        return customer.name
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error creating customer")
        return None
