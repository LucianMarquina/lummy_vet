from odoo import models, fields, api

class VetTreatment(models.Model):
    _name = 'vet.treatment'
    _description = 'Resultado médico de una cita'
    
    _rec_name = 'name'

    name = fields.Char(string='Referencia', compute='_compute_name', store=True)

    appointment_id = fields.Many2one('vet.appointment', string='Cita relacionada', required=True)
    diagnosis = fields.Text(string='Diagnóstico médico')
    medication_ids = fields.Many2many('vet.medication', string='Medicinas recetadas')

    @api.depends('appointment_id')
    def _compute_name(self):
        for rec in self:
            if rec.appointment_id:
                # El título será: "Tratamiento de [CODIGO_CITA]"
                # Asegúrate de que appointment_id tenga un campo 'code' o 'display_name'
                code = rec.appointment_id.code or 'Borrador'
                rec.name = f"Tratamiento de {code}"
            else:
                rec.name = "Nuevo Tratamiento"