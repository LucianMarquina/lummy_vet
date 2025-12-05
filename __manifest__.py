{
    'name': 'Lummy Vet',
    'version': '1.0',
    'summary': 'Módulo de vet_clinic',
    'description': """Un sistema para Lummy-Vet que permite administrar sus pacientes (mascotas),
                    sus dueños (clientes), las citas médicas y el historial clínico""",
    'author': 'Alessandro Marquina',
    'category': 'Inventario & Gestión',

    'depends': [
        'base',
        'contacts'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/vet_appointment.xml'
    ],

    'demo': [

    ],
    
    'auto_install': True,
    'application': True,
    'web_icon': ''
}