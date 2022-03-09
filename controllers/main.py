from odoo import api
import logging
import werkzeug

# from addons.web.controllers.main import ensure_db, SIGN_UP_REQUEST_PARAMS
from odoo import http
# from odoo.http import request
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.auth_signup.models.res_users import ResUsers
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError
from odoo.http import request


_logger = logging.getLogger(__name__)


SIGN_UP_REQUEST_PARAMS = {'db', 'login', 'debug', 'token', 'phone', 'message', 'error', 'scope', 'mode',
                              'redirect', 'redirect_hostname', 'email', 'name', 'partner_id',
                              'password', 'confirm_password', 'city', 'country_id', 'lang'}


class SignupInherit(AuthSignupHome):
    #
    # def get_auth_signup_qcontext(self):
    #     res = super(SignupInherit, self).get_auth_signup_qcontext()
    #     qcontext = {k: v for (k, v) in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}
    #     qcontext.update(self.get_auth_signup_config())
    #     # qcontext['phone'] = qcontext.get('phone')
    #     # print('values', qcontext)
    #     return res

    # @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    # def web_auth_signup(self, *args, **kw):
    #     res = super(SignupInherit, self).web_auth_signup(*args, **kw)
    #     qcontext = self.get_auth_signup_qcontext()
    #     print('resssssss', qcontext)
    #     return res

    # @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        phone = {k: v for (k, v) in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}
        # print('phoneeee',phone['phone'])
        values = {key: qcontext.get(key) for key in ('login', 'name', 'phone', 'password')}
        values['phone'] = phone['phone']
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '')
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        print("phone", values)
        request.env.cr.commit()

    #
    # def _signup_with_values(self, token, values):
    #     print('mememe',values)
    #     db, login,password = request.env['res.users'].sudo().signup(values, token)
    #     request.env.cr.commit()  # as authenticate will use its own cursor we need to commit the current transaction
    #     uid = request.session.authenticate(db, login, password)
    #     if not uid:
    #         raise SignupError(_('Authentication Failed.'))
    #
    #     return super(SignupInherit, self)._signup_with_values( token, values)

# class signNew(ResUsers):
#
#     @api.model
#     def signup(self, values, token=None):
#         res = super(signNew, self).signup(values)
#         # print('values', self)
#         return res
