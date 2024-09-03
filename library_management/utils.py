import frappe


DURATIONS = {
    "1 Month": 30,
    "2 Months": 60,
    "3 Months": 90,
    "1 Year": 365,
}


@frappe.whitelist()
def generate_dates(item: str):

    duration = frappe.db.get_value(
        "Item",
        {"name": item},
        fieldname=["custom_lms_membership_duration"],
        as_dict=True,
    )
    days = DURATIONS[duration.custom_lms_membership_duration]

    obj = {
        "from_date": frappe.utils.today(),
        "to_date": frappe.utils.add_days(frappe.utils.today(), days),
    }

    return obj
