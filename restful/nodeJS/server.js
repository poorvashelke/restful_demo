var express = require('express');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

// Database
mongoose.connect('mongodb://localhost/rest_test');

var app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use('/api', require('./routes/api'));

//port num
app.listen(5000);
