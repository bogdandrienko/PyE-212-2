import $api from "../http";
import { AxiosResponse } from "axios";
import { AuthResponse } from "../models/response/AuthResponse";
import { IUser } from "../models/User";

export default class UserServiceNotWorking {
  
    static fetchUsers(): Promise<AxiosResponse<IUser[]>> {

        return $api.get<IUser[]>('/users')
    }
}