import frappe, erpnext



def get_items_from_purchase_receipts(self):
		self.set("items", [])
		for pr in self.get("purchase_receipts"):
			if pr.receipt_document_type and pr.receipt_document:
				pr_items = frappe.db.sql("""select pr_item.item_code, pr_item.description,
					pr_item.qty, pr_item.base_rate, pr_item.base_amount, pr_item.name,
					pr_item.cost_center, pr_item.is_fixed_asset
					from `tab{doctype} Item` pr_item where parent = %s
					and exists(select name from tabItem
						where name = pr_item.item_code and (is_stock_item = 1 or is_fixed_asset=1))
					""".format(doctype=pr.receipt_document_type), pr.receipt_document, as_dict=True)

				for d in pr_items:
					len = frappe.db.get_value("Item", {"name":d.item_code}, "length")
					wid = frappe.db.get_value("Item", {"name":d.item_code}, "width")
					area = len*wid
					if area > 0: 
						slab = d.qty/area
					item = self.append("items")
					item.item_code = d.item_code
					item.description = d.description
					item.qty = d.qty
					item.slab = slab
					item.rate = d.base_rate
					item.cost_center = d.cost_center or \
						erpnext.get_default_cost_center(self.company)
					item.amount = d.base_amount
					item.receipt_document_type = pr.receipt_document_type
					item.receipt_document = pr.receipt_document
					item.purchase_receipt_item = d.name
					item.is_fixed_asset = d.is_fixed_asset