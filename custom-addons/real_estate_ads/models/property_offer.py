from odoo import fields, models, api
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string = "Status")
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string="Validity")
    creation_date = fields.Date(string="Create Date", default = '_set_create_date')

   
    deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse='_inverse_deadline')
    @api.depends('creation_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else: 
                rec.deadline = False
    def _inverse_deadline(self):
        if rec.deadline and rec.creation_date:
            for rec in self:
                rec.validity = (rec.deadline - rec.creation_date).days
        else:
            rec.validity = False


    @api.model
    def _set_create_data(self):
        return fields.Date.today()