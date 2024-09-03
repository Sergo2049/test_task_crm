from odoo import api, fields, models


class Developer(models.Model):
    _name = 'dm.developer'
    _description = 'Developers Management Developer'

    name = fields.Char(required=True)

    type = fields.Selection(selection=[
        ('front_end', 'front-end'),
        ('back_end', 'back-end'),
        ('fullstack', 'fullstack'),
        ('out_stuff', 'out-stuff')
    ],
    required=True)

    global_identification = fields.Char(
        compute='_compute_global_identification')

    phone = fields.Char(required=True)

    email = fields.Char(required=True)

    address = fields.Text()

    birth_date = fields.Date(required=True)

    job_title = fields.Char(required=True)

    company_id = fields.Many2one('dm.company', required=True)

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for rec in self:
            rec.global_identification = f'{rec.name}-{rec.type}'
