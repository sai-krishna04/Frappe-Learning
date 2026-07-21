# Copyright (c) 2026, Krish and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class FeePayment(Document):

    def validate(self):
        doc = frappe.get_doc("Students", self.student)

        doc.paid += self.fee_paid
        doc.balance = doc.total_fee - doc.paid

        doc.save()
	
	# def get_document(self):
	# 	doc=frappe.get_doc("Students", self.student)
	# 	frappe.msgprint(f"Student Name:{doc.full_name},Age :{doc.age}")

	# 	for row in self.get("child"):
	# 		frappe.msgprint(f"The Student name is {row.name1} and Age is {row.age}")