# -*- coding: utf-8 -*-
{
    'name': 'My Todo',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Manajemen Tugas & To-Do List di Odoo 19',
    'description': """
Modul Todo Odoo 19
==================
Fitur:
- Todo & Task Management (List, Form, Kanban, Search)
- Prioritas Tugas (Rendah, Normal, Tinggi, Sangat Mendesak)
- Status Tugas (Draft, Sedang Dikerjakan, Selesai, Batal)
- Deadline & Filter Penting
    """,
    'author': 'Antigravity & Siba',
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/todo_task_sequence.xml',
        'views/todo_task_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
