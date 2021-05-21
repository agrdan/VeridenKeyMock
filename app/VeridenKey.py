from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response
from datetime import datetime as dt
import jwt
from main import app

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
            'app_id': 'linkedin',
            'handle': 'appOwner',
            'permissions': [
                1,
                2
            ]
        }

        social2 = {
            'app_id': 'instagram',
            'handle': 'appOwner',
            'permissions': [
                0,
                1
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
            'name': 'App Owner',
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
            'app_id': 'linkedin',
            'handle': 'handle1',
            'permissions': [
                1,
                2
            ]
        }

        social2 = {
            'app_id': 'instagram',
            'handle': 'handle2',
            'permissions': [
                0,
                1
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
            'name': 'App Owner',
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
            'app_id': 'linkedin',
            'handle': 'handle1',
            'permissions': [
                1,
                2
            ]
        }

        social2 = {
            'app_id': 'instagram',
            'handle': 'handle2',
            'permissions': [
                0,
                1
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
    @vk.route("/contact/permission/", methods=['POST'])
    def contactPermission():
        resp = {
            'response': 'placeholder'
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
        print(search)
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

    @staticmethod
    @vk.route("/contact/request/", methods=['DELETE'])
    def deleteContact():
        resp = {
            'response': 'Not implemented'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/blocked-users/", methods=['POST', 'DELETE'])
    def blockedUsers():
        resp = {
            'response': 'Not implemented'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/blocked-users/", methods=['GET'])
    def blockedUsersGET():

        blockedUserList = []

        user1 = {
            'id': 'asd267asd24a3sd2a43sd2',
            'name': 'John Johnson',
            'handle': 'handle-1a31234sdfg1927319asdf67asd5f',
            'occupation': 'PM',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 20, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'a8a8a6sd876asd',
            'request_sent_id': '678s6d9a8s6d'
        }

        user2 = {
            'id': 'asd268asd24a3sd2a43sd2',
            'name': 'Mark Markson',
            'handle': 'handle-1a31235sdfg1927319asdf67asd5f',
            'occupation': 'PM',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 20, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'a8a8a6sd898asd',
            'request_sent_id': '678s6d4a3es6d'
        }

        blockedUserList.append(user1)
        blockedUserList.append(user2)

        resp = {

            'response': 'Not implemented'
        }
        return jsonify(blockedUserList)

    @staticmethod
    @vk.route("/login", methods=['POST'])
    def login():
        username = ""
        password = ""
        login = request.get_json()
        try:
            print(login)
            username = login['username']
            password = login['password']

        except Exception as e:
            response = {
                'error': str(e)
            }
            return jsonify(response), 406

        if (username == "decode" and password == "agency!"):
            resp = {
                'token': VeridenKey.generateJWTToken(login)
            }
            return jsonify(resp), 200
        else:
            resp = {
                'error': 'Invalid credentials'
            }
            return jsonify(resp), 401

    @staticmethod
    @vk.route("/contact/request/", methods=['GET'])
    def getContactReq():
        app_owner = {
            'id': 'asd267asd24a3sd2a43sd2',
            'name': 'App Owner - req',
            'handle': 'handle-1asfasd31234sdfg1927319asdf67asd5f',
            'occupation': 'test',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 40, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd8a8a6sd876asd',
            'request_sent_id': '6da78s6d9a8s6d'
        }

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
            'permission': 1,
            'to_user': app_owner
        }
        two = {
            'id': 'a08s8d9as8d7asd9f8a7sdf8',
            'from_user': profileJoe,
            'permission': 2,
            'to_user': app_owner
        }
        listResp.append(one)
        listResp.append(two)
        return jsonify(listResp)

    """

    # android
    @staticmethod
    @vk.route("/contact/request/", methods=['GET'])
    def getContactReq():
        app_owner = {
            'id': 'asd267asd24a3sd2a43sd2',
            'name': 'App Owner - req',
            'handle': 'handle-1asfasd31234sdfg1927319asdf67asd5f',
            'occupation': 'test',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 40, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': True,
            'request_received': True,
            'request_received_id': 'asd8a8a6sd876asd',
            'request_sent_id': '6da78s6d9a8s6d'
        }

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
            'to_user': app_owner
        }
        two = {
            'id': 'a08s8d9as8d7asd9f8a7sdf8',
            'from_user': profileJoe,
            'to_user': app_owner
        }
        listResp.append(one)
        listResp.append(two)
        return jsonify(listResp)
        """


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
    @vk.route("/contact/handle/<string:handle>", methods=['GET'])
    def handleRefresh(handle):
        emailList = []
        emailList.append("test@test.hr")
        emailList.append("test@decode.agency")
        phoneList = []
        phoneList.append("+385991234567")
        phoneList.append("+385981234567")
        social1 = {
            'app_id': 'linkedin',
            'handle': 'handle1',
            'permissions': [
                1,
                2
            ]
        }

        social2 = {
            'app_id': 'instagram',
            'handle': 'handle2',
            'permissions': [
                1,
                2
            ]
        }
        socialList = []
        socialList.append(social1)
        socialList.append(social2)
        hashtagList = []
        hashtagList.append("#krivi")
        hashtagList.append("#model")
        hashtagList.append("#:P")

        resp = {
            'contact_id': 'asd234asd24a3sd2a43sd2',
            'user_id': 'asd908as09d8as0f7d8g7',
            'name': 'Jane Doe',
            'handle': handle,
            'occupation': 'unknown',
            'country': 'Croatia',
            'address': 'Radnicka cesta 47, Zagreb',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'permission_sent': 1,
            'emails': emailList,
            'phones': phoneList,
            'messaging_phones': phoneList,
            'hashtags': hashtagList,
            'socials': socialList
        }

        return jsonify(resp)


    @staticmethod
    @vk.route("/contact/", methods=['POST', 'GET'])
    def contactRequest():
        email1 = {
            'email': 'test@test.hr',
            'permission': 1
        }
        email2 = {
            'email': 'user@decode.agency',
            'permission': 1
        }
        emailList = []
        # emailList.append(email1)
        # emailList.append(email2)
        emailList.append("test@test.hr")
        emailList.append("test@decode.agency")
        phoneList = []
        phone = {
            'permission': 1,
            'phone': '+385991234567'
        }
        phoneList.append(phone)
        messagingPhones = []
        messagingPhones.append("+38599123456")
        messagingPhones.append("+38598123456")
        social1 = {
            'app_id': 'linkedin',
            'handle': 'handle1',
            'permissions': [
                1,
                2
            ]
        }

        social2 = {
            'app_id': 'instagram',
            'handle': 'handle2',
            'permissions': [
                0,
                1
            ]
        }
        socialList = []
        socialList.append(social1)
        socialList.append(social2)
        hashtagList = []
        hashtagList.append("#krivi")
        hashtagList.append("#model")
        hashtagList.append("#:P")
        profileJane = {
            'contact_id': 'asd234asd24a3sd2a43sd2',
            'user_id': 'asd908as09d8as0f7d8g7',
            'name': 'Jane Doe',
            'handle': 'handle-12381927319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'address': 'Radnicka cesta 47, Zagreb',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'permission_sent': 1,
            'emails': emailList,
            'phones': messagingPhones,
            'messaging_phones': messagingPhones,
            'hashtags': hashtagList,
            'socials': socialList
        }

        profileJoe = {
            'contact_id': '123234asd24a3sd2a43sd2',
            'user_id': '123908as09d8as0f7d8g7',
            'name': 'Joe Doe',
            'handle': 'handle-asdf27319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'address': 'Radnicka cesta 47, Zagreb',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'permission_sent': 1,
            'emails': emailList,
            'phones': messagingPhones,
            'messaging_phones': messagingPhones,
            'hashtags': hashtagList,
            'socials': socialList
        }

        contactList = []
        contactList.append(profileJoe)
        contactList.append(profileJane)

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
    @vk.route("/contact/hashtags/", methods=['POST'])
    def contactHashtags():
        resp = {
            'response': 'mock response'
        }
        return jsonify(resp)

    @staticmethod
    @vk.route("/suggestions/", methods=['GET'])
    def getSuggestion():
        limit = request.args.get('limit')
        profileList = []
        profile = {
            'id': 'asd234asd24a3sd2a43sd18q9347',
            'name': 'Pero Peric',
            'handle': 'handle-12sdf81sdfg27319asdf67asd5f',
            'occupation': 'unknown',
            'country': 'Croatia',
            'qr_code': 'qr_code B46',
            'avatar_small_url': 'https://davismarketingcompany.com/wp-content/uploads/2016/01/avatar_placeholder_small.png',
            'avatar_url': 'https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png',
            'address': 'Radnicka cesta 47, Zagreb',
            'last_updated': str(dt.now()),
            'request_sent': False,
            'request_received': False,
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

    @staticmethod
    def generateJWTToken(model):
        m = {
            "username": model['username'],
            "password": model['password']
        }
        return str(jwt.encode(m, app.config["salt"]))