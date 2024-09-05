
window.addEventListener('DOMContentLoaded', (event)=>{
    displayVisitorCount();
})

const localFunctionApi = 'http://localhost:7071/api/update_visitor_count';
const functionApi = 'https://visitorcountapi.azurewebsites.net/api/update_visitor_count?code=UM6NUWR-3DH7WW3Gl3M45wHGWaTsZLTwSDmONiFd_kSOAzFuaDsV8A%3D%3D';

const displayVisitorCount=() =>{
    let count = 0;
    fetch(functionApi).then(response=>{
        return response.json()
    }).then(response=>{
        console.log("Website called function API.");
        count =response;
        document.getElementById("visitor-count").innerHTML =count;
    }).catch(function(error){
        console.log(error);
    })
    return count;
}