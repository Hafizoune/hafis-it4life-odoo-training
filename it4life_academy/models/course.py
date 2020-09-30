# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Course(models.Model):
    _name = 'it4life_academy.course'

    title = fields.Char(string="Title", required=True)
    description = fields.Text()
    duration = fields.Integer(string="Number of hours scheduled for the course")
