import frappe

@frappe.whitelist(allow_guest=True)
def get_doctors():
    """
    Returns a list of all Healthcare Practitioners with first_name, department, and image.
    """
    doctors = frappe.get_all(
        "Healthcare Practitioner",
        fields=["first_name", "department", "image"]
    )
    return doctors
