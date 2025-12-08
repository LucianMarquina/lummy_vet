{
    'name': 'Lummy Vet',
    'version': '1.1',
    'summary': 'Gestión de clínica veterinaria',
    'description': """Un sistema para Lummy-Vet que permite administrar sus pacientes (mascotas),
                    sus dueños (clientes), las citas médicas y el historial clínico""",
    'author': 'Lummy Vet Team (A. Marquina, G. Jaramillo)',
    'category': 'Servicio médico',

    'depends': [
        'base',
        'contacts'
    ],

    'data': [
        'security/ir.model.access.csv',

        'views/vet_appointment.xml',
        'views/inherit_res_partner.xml',
        'views/vet_payment_views.xml',
        'views/menus.xml'
    ],

    'demo': [],
    
    'auto_install': True,
    'application': True,
    'web_icon': 'lummy_vet,static/description/icon.png',
}