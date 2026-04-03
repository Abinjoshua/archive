# -*- coding: utf-8 -*-
from odoo import models,fields
from dateutil.relativedelta import relativedelta

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_archive_products(self):
        """Function to automatically archive inactive products"""
        sale_orders = self.env['sale.order'].search([('state', 'in', 'sale'),('create_date','>=',fields.Date.today() - relativedelta(days=90))])
        sold_products = sale_orders.order_line.product_template_id
        print(sold_products)
        unsold_products = self.env['product.template'].search([('id','not in',sold_products)])
        print(unsold_products)
        for i in unsold_products:
            i.write({'active': False})

