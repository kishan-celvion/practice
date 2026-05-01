// src/auth.js
// const base64 = require('base-64');

// function decodeCredentials(authHeader) {
//   // ...
// }

function decodeCredentials(authHeader) {
  if (!authHeader.startsWith('Basic ')) {
    return ['', ''];
  }

  const base64Credentials = authHeader.split(' ')[1];
  const credentials = Buffer.from(base64Credentials, 'base64').toString('utf-8');

  return credentials.split(':');
}

module.exports = function (req, res, next) {
  // Take the header and decode credentials
  const [username, password] = decodeCredentials(
    req.headers.authorization || ''
  );

  // Verify the credentials
  if (username === 'admin' && password === 'admin') {
    return next();
  }

  // Respond with authenticate header on auth failure.
  res.set('WWW-Authenticate', 'Basic realm="user_pages"');
  res.status(401).send('Authentication required.');
};
