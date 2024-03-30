from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'



    def action_confirm(self):
        super(SaleOrder, self).action_confirm()

        for order in self:
            if order.picking_ids:
                for picking in order.picking_ids:
                    for move in picking.move_ids_without_package:
                        sale_line = move.sale_line_id
                        if sale_line:
                            move.size = sale_line.size