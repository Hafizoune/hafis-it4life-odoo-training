# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Session(models.Model):
    _name = 'it4life_academy.session'


    start_date = fields.Date("Start date ")
    end_date = fields.Date("End date ")
    duration = fields.Integer(string="Duration in days ")
    attendees = fields.Integer(string="Maximum number ")
