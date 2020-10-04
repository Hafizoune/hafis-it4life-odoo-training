# -*- coding: utf-8 -*-

from odoo.tests import common



class TestSession(common.TransactionCase):

  def setUp(self):
      super(TestSession, self).setUp()

  def test_data(self):
      test_ca=self.env['it4life_academy.session'].create({
     'start_date':"10/04/2020",
     'end_date':"10/04/2022",
     'attendees':"4",
     'former_id':"modou"
          })
      test_ca1=self.env['it4life_academy.session'].create({
     'start_date':"10/09/2020",
     'end_date':"20/09/2022",
     'attendees':"9",
     'former_id':"sidy"

      self.assertEqual(test_ca.attendees,test_ca1.attendees)
      print(" Test is successful")
