# -*- coding: utf-8 -*-
# © 2013-2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _get_group(self):
        # Disable default assignment of group 'users' and 'partner manager'
        res = super(ResUsers, self)._get_group()
        for group in ['group_user', 'group_partner_manager']:
            group_id = self.env.ref('base.%s' % group).id
            if group_id in res:
                res.remove(group_id)
        return res

    _defaults = {
        # Refresh method reference
        'groups_id': _get_group,
    }

    @api.depends('groups_id')
    def _is_external_user(self):
        for rec in self:
            rec.is_external_user = self.env['ir.model.access'].sudo(
                rec.id).check_groups('trp_external_user.group_external_user')

    external_user_partner_ids = fields.Many2many(
        'res.partner', 'trp_external_user_partner_id_rel',
        'user_id', 'partner_id',
        'External access to related partners')
    is_external_user = fields.Boolean(
        'Is external user', compute=_is_external_user)
