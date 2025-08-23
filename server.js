const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const db = require('./db');
const path = require('path');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(session({ secret: 'hospital123', resave: false, saveUninitialized: false }));

app.use(express.static('public'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// GET login page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/public/login.html'));
});

// POST login
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  const [rows] = await db.execute(
    'SELECT * FROM users WHERE username = ? AND password = ?', 
    [username, password]
  );

  if (rows.length > 0) {
    req.session.user = username;
    res.redirect('/dashboard');
  } else {
    res.send('Invalid credentials');
  }
});

// GET dashboard
app.get('/dashboard', async (req, res) => {
  if (!req.session.user) return res.redirect('/');

  const [patients] = await db.execute('SELECT * FROM patients');
  res.render('dashboard', { user: req.session.user, patients });
});

// GET logout
app.get('/logout', (req, res) => {
  req.session.destroy(() => {
    res.redirect('/');
  });
});

app.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
