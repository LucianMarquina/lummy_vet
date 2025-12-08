from odoo import models, fields

class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Todo el evento de la cita'

    code = fields.Char(string='Referencia')
    date_time = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now ,required=True)
    partner_id = fields.Many2one('res.partner', string="Dueño", required=True)
    pet_ids = fields.Many2one('vet.patient', string='Paciente', required=True)
    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_vet_doctor', '=', True)])
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('confirmed', 'Confirmado'),
            ('done', 'Realizado'),
            ('cancel', 'Cancelado')
        ], default='draft'
    )
    description = fields.Text(string='Observaciones iniciales')

    payment_ids = fields.One2many('vet.payment', 'appointment_id', string='Pagos realizados')
