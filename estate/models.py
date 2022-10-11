from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

   

    name = fields.Char()
    selling_price = fields.Integer(string='Selling price',readonly=True, copy=False)
    available_dates = fields.Date(string='Available Dates',copy=False, default=datetime.today() - relativedelta(months=3) )
    number_of_rooms = fields.Integer(string='Number of Rooms',default=2)
    active = fields.Boolean(default=False)
    # state = fields.Many2one('New', 'Offer Received' , 'Offer Accepted', 'Sold' , 'Canceled')
    state = fields.Selection([
        ('New','New'), 
        ('Offer Received','Offer Received') , 
        ('Offer Accepted', 'Offer Accepted'), 
        ('Sold', 'Sold') , 
        ('Canceled', 'Canceled')
        ])

    