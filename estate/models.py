from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

   

    name = fields.Char()
    selling_price = fields.Integer(readonly=True, copy=False)
    available_dates = fields.Date(copy=False, default=datetime.today() - relativedelta(months=3) )
    number_of_rooms = fields.Integer(default=2)
    active = fields.Boolean(default=False)
    state = fields.One2many('New', 'Offer Received' , 'Offer Accepted', 'Sold' , 'Canceled')

    