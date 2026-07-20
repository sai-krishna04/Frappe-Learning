from frappe import _

def get_data(data=None):
    if data is None:
        data = {}

    data["fieldname"] = "student"
    data["transactions"] = [
        {
            "label": _("Academic"),
            "items": ["Attendence","ExamFee"]
        }   
    ]

    return data