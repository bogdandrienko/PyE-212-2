import axios from "axios";
import * as constants from "./Constants";

export function getToken(dispatch: any){
    /////////////////////////////////////////////////////
    dispatch({type: constants.LOAD_TOKEN })
    /////////////////////////////////////////////////////
    axios.post("/api/token/", {"username": "admin", "password": "admin"}).then(
        response => {
            /////////////////////////////////////////////////////
            dispatch({type: constants.SUCCESS_TOKEN, payload: response.data })
            /////////////////////////////////////////////////////
        }
    ).catch(
        error => {
            /////////////////////////////////////////////////////
            dispatch({type: constants.ERROR_TOKEN })
            /////////////////////////////////////////////////////
            console.log(error)
        }
    )
  }