
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Course(models.Model):
    _name = 'it4life_academy.course'

    title = fields.Char(string="Titre", required=True)
    description = fields.Text("description")
    duration = fields.Integer(string="duréé")
    theme_id = fields.Many2one('it4life_academy.theme', ondelete='cascade', string="Theme", required=True)


    @api.depends('title')
    def name_get(self):
        result = []
        for record in self:
            name = record.title
            result.append((record.id, name))
        return result


    _sql_constraints = [
        ('name_description_check',
         'CHECK(title != description)',
         "Le titre du cours ne doit pas être la description"),

        ('name_unique',
         'UNIQUE(title)',
         "The course title must be unique"),
    ]
