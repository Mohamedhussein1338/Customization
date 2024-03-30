from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    size= fields.Integer(string='Size')
