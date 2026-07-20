# Copyright (c) 2026, Krish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class client_side(Document):
    def validate(self):
        
        if self.flags.get("skip_duplicate_loop"):
            return

        
        if self.is_new():
            self.new_document()

    def new_document(self):
        doc = frappe.new_doc("client_side")
        doc.name1 = self.name1 or "Krish"
        doc.age1 = self.age1 or 22
        
        
        doc.flags.skip_duplicate_loop = True
        
        
        doc.insert(ignore_permissions=True)
