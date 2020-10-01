# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Session(models.Model):
    _name = 'it4life_academy.session'


    start_date = fields.Date("Start date ")
    end_date = fields.Date("End date ")
    duration = fields.Integer(string="Duration in days ")
    attendees = fields.Integer(string="Maximum number ")

    former_id = fields.Many2one('res.partner', string="former")
    course_id = fields.Many2one('it4life_academy.course',
        ondelete='cascade', string="Course", required=True)
    attendees_ids = fields.Many2many('res.partner', string="List_Attendees")
