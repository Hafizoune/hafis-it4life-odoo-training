# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Theme(models.Model):
    _name = 'it4life_academy.theme'

    
    title = fields.Char(string="Titre", required=True)
    


#    @api.multi
    @api.depends('title')
    def name_get(self):
        result = []
        for record in self:
            name = record.title
            result.append((record.id, name))
        return result
