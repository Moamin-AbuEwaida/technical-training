from zoneinfo import available_timezones
from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char()
    selling_price = fields.Integer()
    available_dates = fields.DateTimeField()
    number_of_rooms = fields.Integer()
    
    