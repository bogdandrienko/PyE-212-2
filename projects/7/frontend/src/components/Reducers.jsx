import * as constants from './Constants.jsx'

export function getAllNewsBooks(state = {}, action=null) {
//export const getAllNewsBooks = (state = {}, action=null ) => {
    switch (action.type) {
      case constants.CONST_NEWS_BOOKS_LOAD:
        return {load: true}
      case constants.CONST_NEWS_BOOKS_DATA:
        return {load: false, data: action.payload}
      case constants.CONST_NEWS_BOOKS_ERROR:
        return {load: false, error: "Ошибка на сервере"}
      case constants.CONST_NEWS_BOOKS_FAIL:
        return {load: false, fail: "Ошибка на клиенте"}
      default:
        return state
    }
  }