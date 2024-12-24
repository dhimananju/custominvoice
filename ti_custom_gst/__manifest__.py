# -*- coding: utf-8 -*-
{
  "name"       : "Add Two GST numbers to invoice",
  "summary"    : "Add Two GST numbers to invoice",
  "category"   : "Uncategorized",
  "license"    : "Other proprietary",
  "version"    : "16.0.0.0",
  "author"     : "Target Integration.",
  "website"    : "http://www.targetintegration.com",

  # any modules required for this to work properly
  "depends"    : ["sale", "purchase", "account"],

  # always loaded
    'data'     : [
                'invoice/ti_custom_invoice.xml'
    ]
}