from odoo import models, fields

class VetMedication(models.Model):
    _name = 'vet.medication'
    _description = 'Modelo de catálogo de medicamentos'

    name = fields.Char(string='Medicamento', required=True)
    active = fields.Boolean(string='Activo', default=True)
    price = fields.Float(string='Precio unitario')