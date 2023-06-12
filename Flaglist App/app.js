const express = require('express');
const redis = require('ioredis');
const app = express();
const client = new redis();

const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));


client.on('error', (err) => {
  console.error('Redis error:', err);
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/api/report', (req, res) => {
  const address = req.body.address;
  client.hincrby('addresses', address, 1, (err, count) => {
    if (err) {
      res.status(500).send('Error reporting address');
    } else {
      res.status(200).send({ count });
    }
  });
});

app.get('/api/search/:address', (req, res) => {
  const address = req.params.address;
  client.hget('addresses', address, (err, count) => {
    if (err) {
      res.status(500).send('Error searching address');
    } else {
      res.status(200).send({ count: count || 0 });
    }
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});