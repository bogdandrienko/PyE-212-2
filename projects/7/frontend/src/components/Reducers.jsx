import * as constants from "./Constants.jsx";
import * as utils from "../components/utils";

export function getAllNewsBooks(state = {}, action = null) {
  //export const getAllNewsBooks = (state = {}, action=null ) => {
  switch (action.type) {
    case constants.CONST_NEWS_BOOKS_LOAD:
      return { load: true };
    case constants.CONST_NEWS_BOOKS_DATA:
      return { load: false, data: action.payload };
    case constants.CONST_NEWS_BOOKS_ERROR:
      return { load: false, error: "Ошибка на сервере" };
    case constants.CONST_NEWS_BOOKS_FAIL:
      return { load: false, fail: "Ошибка на клиенте" };
    default:
      return state;
  }
}

export const R_Categories = utils.ConstructorRR(constants.C_Categories);

export const R_TopBooks = utils.ConstructorRR(constants.C_TopBooks);
export const R_DeleteBook = utils.ConstructorRR(constants.C_DeleteBook);


/////////////////////////////////////////////////////////////////////
export const R_Token = utils.ConstructorRR(constants.C_Token);

export const R_Books = utils.ConstructorRR(constants.C_Books);
export const R_Book = utils.ConstructorRR(constants.C_Book);

