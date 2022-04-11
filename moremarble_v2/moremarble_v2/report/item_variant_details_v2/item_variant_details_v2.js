// Copyright (c) 2016, Usama Naveed and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Variant Details V2"] = {
	"filters": [
		{
			reqd: 1,
			default: "",
			options: "Item",
			label: __("Item"),
			fieldname: "item",
			fieldtype: "Link",
			get_query: () => {
				return {
					filters: { "has_variants": 1 }
				}
			}
		}
	]
};
