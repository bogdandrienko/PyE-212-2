import $api from "../http";

export default class UserService {
    static async getUsers(currentPage, pageSize){
        
        const resp = $api.get('/api/users/', {
            params: {currentPage: currentPage, pageSize: pageSize}})
        return resp
    }
}

