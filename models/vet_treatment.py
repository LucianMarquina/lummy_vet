from odoo import models, fields

class VetTreatment(models.Model):
    _name = 'vet.treatment'
    _description = 'Resultado médico de una cita'

    # Muchos resultados medicos pertenecen a una cita "vet.appointment"
    appointment_id = fields.Many2one('vet.appointment', string='Cita relacionada')
    diagnosis = fields.Text(string='Diagnóstico médico')
    medication_ids = fields.Many2many('vet.medication', string='Medicinas recetadas')
