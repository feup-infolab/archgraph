const user = require('../controllers/users');
const verifyToken = require('../controllers/verifyToken');

const express = require('express');
const router = express.Router();

router.post('/create', verifyToken, user.create);
router.get('/get/:id', verifyToken, user.getById);
router.get('/getall', verifyToken, user.getAll);
router.get('/islogged', verifyToken, user.IsLogged);
router.delete('/delete/:id', verifyToken, user.delete);
router.put('/update/:id', verifyToken, user.update);
router.post('/login', user.login)


module.exports = router;

