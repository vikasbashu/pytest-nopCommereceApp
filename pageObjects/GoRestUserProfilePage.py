import requests

class UserProfile:

    url = "https://gorest.co.in"
    post_end_point = "/public/v2/users"
    get_end_point = "/public/v2/users/{}"
    put_patch_end_point = "/public/v2/users/{}"
    delete_end_point = "/public/v2/users/{}"
    access_token = "Bearer {}".format('ac683ac93cb5d079a79b34ea7febfb2e9f1c9bd7aba7160a8ed15a7898f79293')
    request_header = {
        "Authorization": access_token
    }
    resp = {}

    def createUser(self, payload):
        return requests.post(url=self.url + self.post_end_point, data=payload, headers=self.request_header)

    def getUser(self, user_id):
        return requests.get(url=self.url + self.get_end_point.format(str(user_id)),
                                headers=self.request_header)

    def updateUserPatch(self, user_id, payload):
        return requests.patch(url=self.url + self.put_patch_end_point.format(str(user_id)), data=payload, headers=self.request_header)

    def updateUserPut(self, user_id, payload):
        return requests.put(url=self.url + self.put_patch_end_point.format(str(user_id)), data=payload, headers=self.request_header)

    def deleteUser(self, user_id):
        return requests.delete(url=self.url + self.get_end_point.format(str(user_id)),
                                headers=self.request_header)

