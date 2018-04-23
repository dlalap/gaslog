console.log('Server running.')

const express = require('express');
const bodyParser = require('body-parser')
const MongoClient = require('mongodb').MongoClient
const app = express();

var db
var port = 4000

MongoClient.connect('mongodb://toyota:corolla@ds239648.mlab.com:39648/gas-log', (err, client) => {
	if (err) return console.log(err)
	db = client.db('gas-log')
	app.listen(port, () => {
		console.log('Listening on '+port)
	})
})

app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended: true}))

app.get('/', (req, res) => {
	db.collection('gas-log').find().toArray((err, result) => {
		if (err) return console.log(err)
		res.render('index.ejs', {gaslogs: result})
	})
	})

app.post('/gaslogs', (req, res) => {
	db.collection('gas-log').save(req.body, (err, result) => {
		if (err) return console.log(err)

		console.log('saved to database')
		res.redirect('/')
	})
})