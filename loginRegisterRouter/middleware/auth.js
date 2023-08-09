const jwt = require('jsonwebtoken')

const keyForjwt = 'qwertyu'

const verifyToken = (req,res,next) => {
    const token = req.headers['x-access-token'];

    if(!token){
        return res.status(403).send('A token is requred for auth')
    }

    try{
        const decode = jwt.verify(token,keyForjwt)
        req.user = decode;
    }catch(err){
        console.log(err)
        return res.status(401).send("Invalid Token")
    }
    return next();
}

module.exports = verifyToken;