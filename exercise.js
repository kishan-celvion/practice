const express = require('express')
const app = express()
app.use(express.json())

let persons = [
    { 
      "id": "1",
      "name": "Arto Hellas", 
      "number": "040-123456"
    },
    { 
      "id": "2",
      "name": "Ada Lovelace", 
      "number": "39-44-5323523"
    },
    { 
      "id": "3",
      "name": "Dan Abramov", 
      "number": "12-43-234345"
    },
    { 
      "id": "4",
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122"
    }
]

app.get('/', (req, res) => {
    res.send('<h1>Hello World!</h1>')
})

app.get('/api/persons', (req, res) => {
    res.json(persons)
})

app.get('/api/persons/:id', (req, res) => {
    const id = req.params.id
    const person = persons.find(person => person.id === id)
    if (person) {
        res.json(person)
    }
    else {
        res.status(400).end()
    }
})

app.get('/info', (req, res) => {
    const total = persons.length
    const date = Date()
    res.send(`
        <div>
            <p>Phonebook has info for <b>${total}</b> people</p>
            <p>${date}</p>
        </div>`)
})

app.delete('/api/persons/:id', (req, res) => {
    const id = req.params.id
    persons = persons.filter((person) => person.id !== id)
    res.status(204).end()
})

app.post('/api/persons', (req, res) => {
    const person_body = req.body

    if (!person_body.name || !person_body.number){
        return res.status(400).json({
            error: 'Name and Number is compulsory'
        })
    }

    const name_exists = persons.some(person => person.name === person_body.name)
    if (name_exists) {
        return res.status(400).json({
            error: 'Name numst be unique'
        })
    }
    
    const p_id = person_body.id ? person_body.id : String(Math.floor(Math.random() * 100))
    const person = {
        id: p_id,
        name: person_body.name,
        number: person_body.number,
    }

    persons = persons.concat(person)
    res.json(person)
})

const PORT = 5000
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`)
})