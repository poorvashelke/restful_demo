var express = require('express');
var router = express.Router();

var Product = require('../models/product');

// routes
Product.methods(['get', 'put', 'post', 'delete']);
Product.register(router, '/products');

// return router
module.exports = router;
