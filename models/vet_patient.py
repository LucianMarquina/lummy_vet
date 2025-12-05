from odoo import models, fields

class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Modelo de pacientes (mascotas)'

    name = fields.Char(string='Nombre de Mascota', help="Nombre de la mascota", required=True)
    birth_date = fields.Date(string='Fecha de nacimiento', help='Fecha de nacimiento de la mascota')
    age_pet = fields.Char(string='Edad', compute='_compute_age', help='Edad de la mascota', readonly=False)
    pet_breed = fields.Char(string='Raza', help='Raza de la mascota')
    image_patient = fields.Binary(string='Imagen', help='Imagen de la mascota')
    partner_id = fields.Many2one('res.partner', string='Dueño', required=True)
    history_ids = fields.One2many('vet.appointment', 'pet_ids', string='Historial de citas')