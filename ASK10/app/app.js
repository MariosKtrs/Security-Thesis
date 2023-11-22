const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const cookieParser = require('cookie-parser');

const app = express();
const port = 1500;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'html')));
app.use(cookieParser());

const validCredentials = { username: 'admin', password: 'secret' };

app.get('/login', function(req, res) {
    res.sendFile(path.join(__dirname, 'html', 'login.html'));
});

app.post('/login', function(req, res) {
    const username = req.body.username;
    const password = req.body.password;

    const isValidUser = username === validCredentials.username && password === validCredentials.password;

    if (isValidUser) {
        res.cookie('authenticated', 'true');
        res.redirect('/html/index.html');
    } else {
        res.redirect('/login');
    }
});

app.get('/html/index.html', function(req, res) {
    const isAuthenticated = req.cookies.authenticated === 'true';

    if (isAuthenticated) {
        res.sendFile(path.join(__dirname, 'html', 'index.html'));
    } else {
        res.redirect('/login');
    }
});


// Catch-all route to redirect to login page for undefined routes
app.get('*', function(req, res) {
    res.redirect('/login');
});

app.listen(port, '0.0.0.0', function() {
    console.log('App listening at http://localhost:' + port);
});
