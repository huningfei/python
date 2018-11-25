import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.conf import settings


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        检查用户登录的中间件
        :param request:
        :return:
        """

        for url in settings.AUTH_VALID_URL:
            if re.match(url, request.path_info):
                return None
        next_url = request.path_info
        user_info = request.session.get('user_info')
        if not user_info:


            return redirect('/login/')
