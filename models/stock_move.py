from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    size= fields.Integer(string='Size')
