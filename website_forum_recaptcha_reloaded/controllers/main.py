# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C)2004-TODAY Tech Receptives(<https://www.techreceptives.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.tools.translate import _
import openerp.addons.website_forum.controllers.main as main


class WebsiteForum(main.WebsiteForum):
     
    @http.route('/forum/<model("forum.forum"):forum>/question/new', type='http', auth="user", methods=['POST'], website=True)
    def question_create(self, forum, **post):
        if post.has_key('g-recaptcha-response') and post['g-recaptcha-response'] and request.website.is_captcha_valid(post['g-recaptcha-response']):
            return super(WebsiteForum, self).question_create(forum, **post)
        values = self._prepare_forum_values(forum=forum, searches={}, header={'ask_hide': True})
        values.update(post)
        return request.website.render("website_forum.ask_question", values) 
    
    
                
    
