import axios, { AxiosRequestConfig } from "axios";

export const API_URL = `http://127.0.0.1:8000/`

const $api = axios.create()

$api.interceptors.request.use( config => {
    
 
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
    return config;
})

$api.interceptors.response.use ((config) =>  {
    return config;
}, (error => {
    const originalRequest = error.config;
    if(error.response.status == 401 && error.config && !error.config._isRetry ){
        originalRequest._isRetry = true;
        try{
            const response = axios.post('/api/token/refresh/', {
                "refresh": localStorage.getItem('refreshToken')
            } )
            localStorage.setItem('token', response.data.access);
            localStorage.setItem('refreshToken', response.data.refresh);
            return $api.request(originalRequest);
        } catch (e) {
            console.log('НЕ АВТОРИЗОВАН')
        }     
    }
    throw error;
}))

export default $api;




// const $api = axios.create({
//     // withCredentials: true,
//     // baseURL: API_URL
// })
