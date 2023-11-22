const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 1500;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'html')));

const users = [
    { username: 'admin', password: 'secret' },
    // Add more users if needed
];

app.get('/login', function(req, res) {
    res.sendFile(path.join(__dirname, 'html', 'login.html'));
});

app.post('/login', function(req, res) {
    const username = req.body.username;
    const password = req.body.password;

    const isValidUser = users.some(function(user) {
        return user.username === username && user.password === password;
    });

    if (isValidUser) {
        res.redirect('/html/index.html');
    } else {
        res.redirect('/login');
    }
});

app.get('/html/index.html', function(req, res) {
    res.sendFile(path.join(__dirname, 'html', 'index.html'));
});

app.listen(port, '0.0.0.0', function() {
    console.log('App listening at http://localhost:' + port);
});
