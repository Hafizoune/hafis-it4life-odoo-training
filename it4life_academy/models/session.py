# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import logging 
log = logging.getLogger("mes log")


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


#    @api.onchange('start_date','end_date')
#    def calcul_duration(self):
#        if self.start_date and self.end_date:
#            dt=self.start_date
#            dt1=self.end_date
#            #d1 = datetime.strptime(dt, "%d/%m/%Y").date()
#            #d2 = datetime.strptime(dt1, "%d/%m/%Y").date()
#            rd = relativedelta(self.end_date, self.start_date)
#            self.duration = str(rd.years) 
#        return self.duration

    
    @api.onchange('start_date','end_date')
    def _compute_duration(self):
        #self.ensure_one()
        log.error("suis ds la fonction compute")
        if self.start_date and self.end_date:
            d1  = self.start_date
            log.error(d1)
            d2 = self.end_date
            log.error(d2)
            self.duration = int(relativedelta(d2, d1).years)
