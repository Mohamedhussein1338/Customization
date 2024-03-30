from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    size= fields.Integer(string='Size')


    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update({'size': self.size, })
        return res