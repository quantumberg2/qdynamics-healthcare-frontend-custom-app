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

# ✅ Get get_appointment_types
@frappe.whitelist(allow_guest=True)
def get_appointment_types(department=None):
    try:
        filters = {}
        if department:
            filters["department"] = department
        
        appointment_types = frappe.get_all(
            "Appointment Type",
            filters=filters,
            fields=["name", "appointment_type"]
        )
        return {"status": "success", "data": appointment_types}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_appointment_types API Error")
        return {"status": "error", "message": str(e)}

#✅ Get Doctor Schedule
import frappe

@frappe.whitelist(allow_guest=True)
def get_doctor_schedule(practitioner):
    """Return day and time slots for a given practitioner"""
    try:
        practitioner_doc = frappe.get_doc("Healthcare Practitioner", practitioner)
        schedule_list = []

        for row in practitioner_doc.practitioner_schedules:
            schedule_doc = frappe.get_doc("Practitioner Schedule", row.schedule)
            for s in schedule_doc.time_slots:
                schedule_list.append({
                    "day": s.day,
                    "from_time": s.from_time,
                    "to_time": s.to_time
                })

        return schedule_list

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_doctor_schedule_error")
        return {"status": "error", "message": str(e)}


#✅ Create Patient Appointment 
import frappe, json, random
from frappe.utils import now_datetime
from datetime import datetime

@frappe.whitelist(allow_guest=True)
def create_appointment():
    """Create a Patient Appointment and show practitioner first name on overlap error"""
    try:
        data = frappe.local.form_dict
        if isinstance(data, str):
            data = json.loads(data)

        name1 = data.get("name1") or data.get("patient")  # Patient Name
        practitioner = data.get("practitioner")  # healthcare practitioner ID
        appointment_date = data.get("appointment_date")
        appointment_time = data.get("appointment_time")  # expecting "HH:MM:SS - HH:MM:SS"

        phone_number = data.get("phone_number") or data.get("phone")
        patient_age = data.get("patient_age") or data.get("age")

        # ✅ Parse time range safely
        if "-" in appointment_time:
            start_str, end_str = [t.strip() for t in appointment_time.split("-")]
            start_time = datetime.strptime(start_str, "%H:%M:%S").time()
            end_time = datetime.strptime(end_str, "%H:%M:%S").time()
        else:
            start_time = datetime.strptime(appointment_time, "%H:%M:%S").time()
            end_time = None

        # Check for overlapping appointment
        overlap = frappe.db.exists({
            "doctype": "Patient Appointment",
            "practitioner": practitioner,
            "appointment_date": appointment_date,
            "appointment_time": start_time  # compare only start time
        })

        if overlap:
            practitioner_doc = frappe.get_doc("Healthcare Practitioner", practitioner)
            first_name = practitioner_doc.first_name or practitioner_doc.practitioner_name or practitioner
            frappe.throw(f"Not allowed, cannot overlap appointment with Dr. {first_name}")

        # Build unique name
        unique_suffix = now_datetime().strftime("%Y%m%d%H%M%S") + str(random.randint(10,99))
        unique_name = f"{name1}-{unique_suffix}"

        # Create the appointment
        appointment = frappe.get_doc({
            "doctype": "Patient Appointment",
            "name": unique_name,
            "patient": name1,
            "email": data.get("email"),
            "gender": data.get("gender"),
            "phone_number": phone_number,
            "patient_age": patient_age,
            "appointment_type": data.get("appointment_type"),
            "appointment_date": appointment_date,
            "appointment_time": start_time,  # store only start time
            "practitioner": practitioner,
            "department": data.get("department"),
            "notes": data.get("notes", "")
        })
        appointment.insert(ignore_permissions=True)
        frappe.db.commit()

        return {"status": "success", "appointment_id": appointment.name}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "create_appointment API Error")
        return {"status": "error", "message": str(e)}
