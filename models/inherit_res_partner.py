from odoo import models, fields

class InheritResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_vet_doctor = fields.Boolean(
        default=False,
        help="Es un veterinario?") 
           
    pet_ids = fields.One2many(
        'vet.patient', 
        'partner_id',
        string="Mascotas")
