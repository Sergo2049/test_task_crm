from odoo import api, fields, models


class Developer(models.Model):
    _name = 'dm.developer'
    _description = 'Developers Management Developer'

    name = fields.Char()

    type = fields.Selection(selection=[
        ('front_end', 'front-end'),
        ('back_end', 'back-end'),
        ('fullstack', 'fullstack'),
        ('out_stuff', 'out-stuff')
    ])

    global_identification = fields.Char(
        compute='_compute_global_identification')

    phone = fields.Char()

    email = fields.Char()

    address = fields.Text()

    birth_date = fields.Date()

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for rec in self:
            rec.global_identification = f'{rec.name}-{rec.type}'
