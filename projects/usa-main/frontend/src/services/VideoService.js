import $api from "../http";

export default class VideoService{
    static async getVideo(currentPage, pageSize, categoryid){
        const resp = $api.get('/api/video/', {
            params: {currentPage: currentPage, pageSize: pageSize, categoryid: categoryid}})
        return resp
    }

    // static async getCategoryVideos() {
    //     const resp = $api.get('/api/videocategory/')
    //     return resp 
    // }
}