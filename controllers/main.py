from odoo import http
from odoo.http import request


class WebDirectPrintController(http.Controller):

    @http.route('/web_direct_print/data', auth='user')
    def web_direct_print_data(self):
        report_list = request.env['ir.actions.report'].sudo().search([['is_print','=',True]]).read(['report_name'])
        if report_list:
            return list(map(lambda x: x['report_name'],report_list[0]))
        return []
