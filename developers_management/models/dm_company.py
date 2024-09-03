from odoo import fields, models


class Company(models.Model):
    _name='dm.company'
    _description = 'Developers Management Company'

    name = fields.Char()

    address = fields.Text()

    developer_ids = fields.One2many('dm.developer', 'company_id')
