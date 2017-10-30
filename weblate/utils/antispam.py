# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2017 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from django.conf import settings

from weblate.trans.site import get_site_url
from weblate.utils.request import get_ip_address


def is_spam(text, request):
    """Generic spam checker interface."""
    if settings.AKISMET_API_KEY:
        from akismet import Akismet
        akismet = Akismet(
            settings.AKISMET_API_KEY,
            get_site_url()
        )
        return akismet.comment_check(
            get_ip_address(request),
            request.META.get('HTTP_USER_AGENT', ''),
            comment_content=text,
            comment_type='comment'
        )
    return False
