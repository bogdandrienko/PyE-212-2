
import ProfileService from "../services/ProfileService";

// const GETPROFILE = "GETPROFILE";
const SETPROFILE = "SETPROFILE";
const SETAVAST = "SETAVAST";

let initialState = {
    profile : {},
    avast: null   
};

const profileReducer = (state = initialState, action) => {
    switch(action.type){
        // case GETPROFILE: {
        //     return {...state, profile: action.profile};
        // }
        case SETPROFILE: {
            return {...state, profile: action.profile};
        }
        case SETAVAST: {
            return {...state, avast: action.avast};
        }

        default: return state;
    }
}

export const setProfile = (profile) => ({type: SETPROFILE, profile}) 
export const setavast = (avast) => ({type: SETAVAST, avast})

 
export const getProfile = async(dispatch) => {
    try{
        const response = await ProfileService.myProfile()
        console.log("profileReducer")
        console.log(response.data.profile.user)
        console.log("profileReducer")
        dispatch(setProfile(response.data.profile.user))
        dispatch(setavast(response.data.profile.user.avatar[0].avatar))

    } catch(e) {
        console.log(e)
    }
}

export const updateProfile = async (emailChange, dispatch) => {
    try{
        const response = await ProfileService.updateMyProfile(emailChange)
        console.log(response);
    } catch(e) {
        console.log(e)
    }
}

export const uploadProfilePhoto = async(uploadData, dispatch) => {
    try{
        const response = await ProfileService.uploadPhotoProfile(uploadData)
        console.log(response);
        
        dispatch(setavast(response.data.profile.user.avatar[0].avatar))
    } catch(e) {
        console.log(e)
    }
}

export default profileReducer;