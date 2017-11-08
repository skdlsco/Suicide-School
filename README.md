uicide-School

# Schema

### user Schema

    name : String
    
    id : String
    
    password : String
    
    token : String
    
    
# /auth

### : POST /auth/login

> require

    id : 유저 id
    
    password : 유저 password
    
> response : Success

    status : 200
    
    data : userSchema
 
> response : Failed
    
    status : 404
    
    
### : POST /auth/register

> require

    id : 유저 id
    
    password : 유저 password

    name : 유저 name
    
> response : Success

    status : 200
    
    data : userShema
    
> response : Failed
    
    status : 404
    
    
### : GET /auth/getData

> require

    token : 유저 token
    
> response : Success

    status : 200
    
    data : userSchema
 
> response : Failed
    
    status : 404

