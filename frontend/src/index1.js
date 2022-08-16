import axios from "axios";

axios.get('/api/course/').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})


fetch('/api/task/')
    .then((response) => response.json())
    .then((data) => console.log(data))

