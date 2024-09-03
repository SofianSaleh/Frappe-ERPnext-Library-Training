import frappe


def on_submit(doc, event):
    references = doc.references
    if len(references) > 0:
        for reference in references:
            if reference.reference_doctype == "Sales Invoice":
                membership = frappe.db.get_value(
                    "Sales Invoice",
                    {"name": reference.reference_name},
                    fieldname=["custom_lms_library_membership"],
                    as_dict=True,
                )
                if membership and reference.outstanding_amount == 0:
                    frappe.db.set_value(
                        "Library Membership",
                        {"name": membership.custom_lms_library_membership},
                        "paid",
                        1,
                    )
