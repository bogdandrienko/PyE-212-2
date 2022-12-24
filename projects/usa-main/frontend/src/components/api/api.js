import * as axios from "axios";

export const API_URL  = `http://localhost:8000/api`

const api = axios.create({   
    headers: {
        "token" : "5bfa63ed-8ed3-4d5b-97e1-6f862dc30e08"
    }
});

api.interceptors.request.use( (config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
    return config
})

export default api