from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response
from datetime import datetime as dt
vk = Blueprint('veriden_key', __name__)



class VeridenKey:

    @staticmethod
    @vk.route("/social/signin/", methods=['POST'])
    def signin():
        resp = {
            'access_token': 'fasd8f97as9df87asd9f8a7sdf8!'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/social/signup/", methods=['POST'])
    def signup():
        resp = {
            'access_token': 'fasd8f97as9df87asd9f8a7sdf8!'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/me/", methods=['GET'])
    def me():
        email1 = {
            'email': 'test@test.hr',
            'permission': 1
        }
        email2 = {
            'email': 'user@decode.agency',
            'permission': 1
        }
        emailList = []
        emailList.append(email1)
        emailList.append(email2)
        phoneList = []
        phone = {
            'permission': 1,
            'phone': '+385991234567'
        }
        phoneList.append(phone)

        social1 = {
            'app_id': 'asd123asd123',
            'handle': 'handle1',
            'permissions': [
                1,
                2,
                3
            ]
        }

        social2 = {
            'app_id': 'asd321as321',
            'handle': 'handle2',
            'permissions': [
                1,
                2
            ]
        }
        socialList = []
        socialList.append(social1)
        socialList.append(social2)
        resp = {
            'address': 'Radnicka cesta 47, Zagreb',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'country': 'Croatia',
            'emails': emailList,
            'facebook_connected': True,
            'facebook_gentoo_friends': 3,
            'handle': 'some handle (username?)',
            'id': 'asd6a7s8d6as8d76as8d7',
            'linkedin_connected': True,
            'linkedin_gentoo_friends': 5,
            'messaging_phones': phoneList,
            'name': 'some name',
            'occupation': 'developer',
            'phones':  phoneList,
            'qr_code': 'qr code b64?',
            'socials': socialList,
            'notification_key': 'asd8asdas78dg6sd9h6dfgh9d6'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/me/update/", methods=['PATCH'])
    def mePatch():
        emailList = []
        emailList.append("test@test.hr")
        emailList.append("user@decode.agency")
        phoneList = []
        phone = {
            'permission': 1,
            'phone': '+385991234567'
        }
        phoneList.append(phone)

        social1 = {
            'app_id': 'asd123asd123',
            'handle': 'handle1',
            'permissions': [
                1,
                2,
                3
            ]
        }

        social2 = {
            'app_id': 'asd321as321',
            'handle': 'handle2',
            'permissions': [
                1,
                2
            ]
        }
        socialList = []
        socialList.append(social1)
        socialList.append(social2)
        resp = {
            'address': 'Radnicka cesta 47, Zagreb',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'country': 'Croatia',
            'emails': emailList,
            'facebook_connected': True,
            'facebook_gentoo_friends': 3,
            'handle': 'some handle (username?)',
            'id': 'asd6a7s8d6as8d76as8d7',
            'linkedin_connected': True,
            'linkedin_gentoo_friends': 5,
            'messaging_phones': phoneList,
            'name': 'some name',
            'occupation': 'developer',
            'phones': phoneList,
            'qr_code': 'qr code b64?',
            'socials': socialList,
            'notification_key': 'asd8asdas78dg6sd9h6dfgh9d6'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/social/connect/", methods=['POST'])
    def socialConnect():
        emailList = []
        emailList.append("test@test.hr")
        emailList.append("user@decode.agency")
        phoneList = []
        phone = {
            'permission': 1,
            'phone': '+385991234567'
        }
        phoneList.append(phone)

        social1 = {
            'app_id': 'asd123asd123',
            'handle': 'handle1',
            'permissions': [
                1,
                2,
                3
            ]
        }

        social2 = {
            'app_id': 'asd321as321',
            'handle': 'handle2',
            'permissions': [
                1,
                2
            ]
        }
        socialList = []
        socialList.append(social1)
        socialList.append(social2)
        resp = {
            'address': 'Radnicka cesta 47, Zagreb',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'country': 'Croatia',
            'emails': emailList,
            'facebook_connected': True,
            'facebook_gentoo_friends': 3,
            'handle': 'some handle (username?)',
            'id': 'asd6a7s8d6as8d76as8d7',
            'linkedin_connected': True,
            'linkedin_gentoo_friends': 5,
            'messaging_phones': phoneList,
            'name': 'some name',
            'occupation': 'developer',
            'phones': phoneList,
            'qr_code': 'qr code b64?',
            'socials': socialList,
            'notification_key': 'asd8asdas78dg6sd9h6dfgh9d6'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/me/", methods=['POST'])
    def mePost():
        resp = {
            'access_token': 'fasd8f97as9df87asd9f8a7sdf8!'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/user/<string:handle>/profile/", methods=['GET'])
    def getProfile(handle):
        print(handle)
        resp = {
            'id': 'asd234asd24a3sd2a43sd2',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd87a6sd876asd',
            'request_sent_id': '6da78s6d8a7s6d'

        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/user/search/", methods=['GET'])
    def search():
        search = request.args.get('search_term')
        profileList = []
        profile = {
            'id': 'asd234asd24a3sd2a43sd2',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd87a6sd876asd',
            'request_sent_id': '6da78s6d8a7s6d'
        }

        profileList.append(profile)

        resp = {
            'count': 1,
            'next': 'next',
            'previous': 'previous',
            'result': profileList
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/contact/request/", methods=['GET'])
    def getContactReq():

        profileJane = {
            'id': 'asd234asd24a3sd2a43sd2',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd87a6sd876asd',
            'request_sent_id': '6da78s6d8a7s6d'
        }

        profileJoe = {
            'id': 'erty234asd24a3sd2a43sd2',
            'name': 'Joe Doe',
            'handle': 'handle-qwerty1927319asdf67asd5f',
            'occupation': 'dev',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 20, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'qwert3a6sd876asd',
            'request_sent_id': 'qwert3s6d8a7s6d'
        }

        listResp = []
        one = {
            'id': 'a09s8d9as8d7asd9f8a7sdf8',
            'from_user': profileJane,
            'to_user': profileJoe
        }
        listResp.append(one)
        resp = {
            listResp
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/contact/request/", methods=['POST'])
    def postContactReq():

        resp = {
            'request_sent_id': 'a09s8d9as8d7asd9f8a7sdf8'

        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/contact/request/action/<string:reqId>/", methods=['POST'])
    def contactReqAction(reqId):
        resp = {
            'response': 'Not implemented'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/contact/", methods=['POST', 'GET'])
    def hashtag():
        profileJane = {
            'id': 'asd234asd24a3sd2a43sd2',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd87a6sd876asd',
            'request_sent_id': '6da78s6d8a7s6d'
        }

        profileJoe = {
            'id': 'erty234asd24a3sd2a43sd2',
            'name': 'Joe Doe',
            'handle': 'handle-qwerty1927319asdf67asd5f',
            'occupation': 'dev',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 20, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'qwert3a6sd876asd',
            'request_sent_id': 'qwert3s6d8a7s6d'
        }

        profileTesto = {
            'id': 'test234asd24a3sd2a43sd2',
            'name': 'Testo Testic',
            'handle': 'handle-test1927319asdf67asd5f',
            'occupation': 'tester',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 20, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'test3a6sd876asd',
            'request_sent_id': 'test3s6d8a7s6d'
        }

        contactList = []
        contactList.append(profileJoe)
        contactList.append(profileJane)
        contactList.append(profileTesto)

        deletedList = []
        deletedList.append("Nitko1")
        deletedList.append("Nitko2")
        resp = {
            'contacts': contactList,
            'deleted_contacts': deletedList
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/hashtag/<string:id>/", methods=['DELETE'])
    def hashtagDelete(id):

        resp = {
            'access_token': 'fasd8f97as9df87asd9f8a7sdf8!'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/suggestions/", methods=['GET'])
    def getSuggestion():
        limit = request.args.get('limit')
        profileList = []
        profile = {
            'id': 'asd234asd24a3sd2a43sd2',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd87a6sd876asd',
            'request_sent_id': '6da78s6d8a7s6d'
        }

        profileList.append(profile)

        resp = {
            'count': 1,
            'next': 'next',
            'previous': 'previous',
            'results': profileList
        }
        return jsonify(resp)