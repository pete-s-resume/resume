const express = require('express');
const verifyToken = require('../middleware/auth')
const {test,register,login} = require('../controller/userController');

const router = express.Router();

router.post('/test',verifyToken,test);
router.post('/register',register)
router.post('/login',login)

module.exports = router;