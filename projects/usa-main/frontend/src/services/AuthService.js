import $api from "../http";
// import { AxiosResponse } from "axios";
// import { AuthResponse } from "../models/response/AuthResponse";
// import { forwardRef } from "react";




export default class AuthService {
    static async login(username, password){

        
        const resp = $api.post('/api/token/', {"username": username, "password": password})
        // console.log("resp")
        // console.log(resp)
        return resp
            // .then(response => response.data.accessToken)
    }

    static async logout(){
        return $api.post('/logout')
            // .then(response => response.data.accessToken)
    }
}



//ts

// export default class AuthService {
//     static async login(username: string, password: string): Promise<AxiosResponse<AuthResponse>>{
//         return $api.post<AuthResponse>('/login', {username, password})
//             // .then(response => response.data.accessToken)
//     }

//     static async logout(): Promise<void>{
//         return $api.post('/logout')
//             // .then(response => response.data.accessToken)
//     }
// }


