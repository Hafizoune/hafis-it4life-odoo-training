# -*- coding: utf-8 -*-
from odoo import fields, models

class Contact(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    former = fields.Boolean("former", default=False)

    session_ids = fields.Many2many('it4life_academy.session',
        string="Attended Sessions", readonly=True)
