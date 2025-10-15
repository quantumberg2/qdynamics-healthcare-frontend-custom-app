import frappe, json

# ✅ Get all Medical Departments
@frappe.whitelist(allow_guest=True)
def get_departments():
    try:
        departments = frappe.get_all(
            "Medical Department",
            fields=["name", "department"]
        )
        return {"status": "success", "data": departments}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_departments API Error")
        return {"status": "error", "message": str(e)}

# ✅ Get Practitioners by Department
@frappe.whitelist(allow_guest=True)
def get_practitioners(department):
    try:
        doctors = frappe.get_all(
            "Healthcare Practitioner",
            filters={"department": department},
            fields=["name", "first_name", "last_name", "designation"]
        )
        return {"status": "success", "data": doctors}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_practitioners API Error")
        return {"status": "error", "message": str(e)}




# ✅ Create Appointment
@frappe.whitelist(allow_guest=True)
def create_appointment(data=None):
    try:
        if isinstance(data, str):
            data = json.loads(data)

        appointment = frappe.get_doc({
            "doctype": "Patient Appointment",
            "company": data.get("company", "Quantumberg"),
            "appointment_type": data.get("appointment_type"),
            "appointment_date": data.get("appointment_date"),
            "patient": data.get("patient"),
            "practitioner": data.get("practitioner"),
            "department": data.get("department"),
            "duration": data.get("duration", 30),
            "notes": data.get("notes"),
        })
        appointment.insert(ignore_permissions=True)
        frappe.db.commit()
        return {"status": "success", "appointment_id": appointment.name}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "create_appointment API Error")
        return {"status": "error", "message": str(e)}
