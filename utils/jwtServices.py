import jwt
from dotenv import load_dotenv
import os

# should have env variable
class jwtService:
    def __init__(self,secretKey,algorithm):
        self.secretKey = secretKey
        self.algorithm = algorithm
    
    def extractToken(self,request):
        """Extract user info from JWT token"""
        try:
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
                payload = jwt.decode(token,self.secretKey, algorithms = self.algorithm)
                user_id = payload.get('uid')
                return user_id
            
            return None
        
        except jwt.PyJWTError:
            return None
        
#test
if __name__ == "__main__":
    payload = {'uid': "U001"}

    # Encode token
    token = jwt.encode(payload, str(JWT_SECRET_KEY), algorithm="HS256")
    print(token)

    result = jwt.decode(token,str(JWT_SECRET_KEY), algorithms = ['HS256'])
    print(result)