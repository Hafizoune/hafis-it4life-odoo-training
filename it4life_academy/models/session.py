# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta



class Session(models.Model):
    _name = 'it4life_academy.session'

    
    start_date = fields.Date("date debut")
    end_date = fields.Date("date fin")
    duration = fields.Integer(string="Durée")
    attendees = fields.Integer(string="nbre participants")

    former_id = fields.Many2one('res.partner', string="formateur")
    course_id = fields.Many2one('it4life_academy.course',
        ondelete='cascade', string="Cours", required=True)
    attendees_ids = fields.Many2many('res.partner', string="Liste participant")


    @api.depends('course_id')
    def name_get(self):
        result = []
        for record in self:
            name = record.course_id 
            result.append((record.id, name))
        return result


    
    @api.onchange('start_date','end_date')
    def _compute_duration(self):
        if self.start_date and self.end_date:
            d1  = self.start_date
            d2 = self.end_date
            self.duration = int(relativedelta(d2, d1).years)


    _sql_constraints = [
        ('start_date_end_date_check',
         'CHECK( start_date !=  end_date)',
         "La date de début du cours ne doit pas être la date de fin"),

        ('name_unique',
         'UNIQUE(name)',
         "La session date debut doit être unique"),
    ]
