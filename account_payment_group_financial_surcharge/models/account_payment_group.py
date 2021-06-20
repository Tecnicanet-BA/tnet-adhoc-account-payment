##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class AccountPaymentGroup(models.Model):

    _inherit = "account.payment.group"

    financing_surcharge = fields.Monetary(compute='_computed_financing_surcharge')

    @api.depends('payment_ids.net_amount')
    def _computed_financing_surcharge(self):
        for rec in self:
            rec.financing_surcharge = sum(
                rec.payment_ids.filtered('financing_plan_id').mapped(lambda x: x.amount - x.net_amount))