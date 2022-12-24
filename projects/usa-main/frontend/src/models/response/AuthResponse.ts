import { IUser } from "../User";

export interface AuthResponse {
    accessToken: string;
    refreshToken: string;
    user: IUser
}