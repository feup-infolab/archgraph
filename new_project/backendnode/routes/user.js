const user = require('../controllers/users');
const express = require('express');
const router = express.Router();

router.post('/create', user.create);
router.get('/get/:id', user.getById);
router.get('/getall', user.getAll);
router.delete('/delete/:id', user.delete);
router.put('/update/:id', user.update);
router.post('/login', user.login)



module.exports = router;

