import frappe

@frappe.whitelist(allow_guest=True)
def get_doctors():
    """
    Returns a list of all Healthcare Practitioners with basic info.
    """
    doctors = frappe.get_all(
        "Healthcare Practitioner",
        fields=["name", "first_name", "department", "image", "linkedin", "facebook", "twitter"]
    )
    return doctors


@frappe.whitelist(allow_guest=True)
def get_doctor(id):
    """
    Returns detailed info for a single doctor by name (ID).
    """
    doctor = frappe.get_all(
        "Healthcare Practitioner",
        filters={"name": id},
        fields=[
            "name",
            "first_name",
            "department",
            "image",
            "linkedin",
            "facebook",
            "twitter",
            "working_at",
            "experience",
            "joining_date",
            "op_consulting_charge",
            "hospital",
            "degree",
        ],
    )

    if not doctor:
        frappe.throw("Doctor not found", frappe.DoesNotExistError)

    return doctor[0]
