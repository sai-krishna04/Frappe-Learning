# Copyright (c) 2026, Krish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today


class Students(Document):
	pass
	def validate(self):
		if self.dob:
			a=getdate(self.dob)
			b=getdate(today())
			if a > b:
				frappe.throw("Date of Birth cannot be in the future")
			self.age=b.year - a.year
		if self.age < 18:
			frappe.throw("Student must be at least 18 years old.")	

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}".upper()

	def before_insert(self):
		frappe.msgprint("Creating new student.....")

	def after_insert(self):
		frappe.msgprint(f"Student {self.full_name} has been added successfully.")

	def on_submit(self):
		frappe.sendmail(
			recipients=[self.stud_email],
			subject="Welcome",
			message=f"Hello {self.full_name}, your application has been approved.",
			now=True
		)

	def on_update(self):
		frappe.msgprint(f"Student {self.full_name} has been updated successfully.")

	def after_delete(self):
		frappe.msgprint(f"Student {self.full_name} has been deleted successfully.")
	
	def on_cancel(self):
		if self.document=='Pan':
			frappe.throw("Cannot cancel student with Pan document.")

	def on_change(self):
		frappe.msgprint("Changes occured!!!")
