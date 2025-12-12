from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date

class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Modelo de pacientes (mascotas)'

    name = fields.Char(string='Nombre de Mascota', required=True)
    birth_date = fields.Date(string='Fecha de nacimiento')
    
    age_pet = fields.Char(string='Edad', compute='_compute_age')
    
    pet_breed = fields.Char(string='Raza')
    image_patient = fields.Binary(string='Imagen')
    partner_id = fields.Many2one('res.partner', string='Dueño', required=True)
    
    history_ids = fields.One2many('vet.appointment', 'pet_id', string='Historial de citas')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                d = relativedelta(date.today(), record.birth_date)
                record.age_pet = f"{d.years} años, {d.months} meses"
            else:
                record.age_pet = "Sin fecha"