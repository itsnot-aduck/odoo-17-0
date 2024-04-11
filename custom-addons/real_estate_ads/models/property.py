from odoo import fields, models, api

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Name", required=True)
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date", readonly=True)
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price")
    best_offer = fields.Integer(string="Best Offer")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string = "Facades")
    garage = fields.Boolean(string = "Garage", default = False)
    garden = fields.Boolean(string = "Garden", default = False)
    garden_area = fields.Integer(string = "Garden Area")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        string = "Garden Orientation", default = 'north')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', True)])
    phone = fields.Char(string="Phone", related='buyer_id.phone')

    # Compute properties
    @api.onchange('living_area', 'garden_area')
    def _computer_total_area(self):
        self.total_area = self.living_area + self.garden_area
    total_area = fields.Integer(string="Total Area")


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Estate Property Type"

    name = fields.Char(string="Name", required = True)


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = "Estate Property Tags"

    name = fields.Char(string="Name", required = True)