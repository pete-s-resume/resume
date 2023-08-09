const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs')
const User = require('../model/user');

const keyForjwt = 'qwertyu'

const test = (req,res) => {
    console.log("test route")
}

const register = async(req,res) => {
    try{
        const {first_name,last_name,email,password} = req.body;
        

        if(!(email&&password&&email&&password)){
            res.status(400).send("All inputs are required")
        }

        const oldUser = await User.findOne({email})

        if(oldUser){
            return res.status(400).send("User already exist.")
        }

        encryptedPassword = await bcrypt.hash(password, 10);

        const user = await User.create({
            first_name,
            last_name,
            email,
            password:encryptedPassword,
        })

    }catch(err){
        console.log(err)
    }
}



const login = async(req,res) => {
    try{
        const {email,password} = req.body

        if (!(email&&password)){
            res.status(400).send("login are required all input")
        }

        const user = await User.findOne({email});

        if (user&& await bcrypt.compare(password, user.password)){
            const token = jwt.sign(
                {user_id:user._id,email},
                keyForjwt,
                {
                    expiresIn:"2h"
                }
            )
            user.token = token
            return res.status(200).send(user)
        }
        res.status(400).send("login fail")
    }catch(err){
        console.log(err)
    }
}


module.exports = {test,register,login} 