
window.addEventListener('DOMContentLoaded', (event)=>{
    displayVisitorCount();
})

const localFunctionApi = 'http://localhost:7071/api/update_visitor_count';
const functionApi = 'https://updatevisitors.azurewebsites.net/api/update_visitor_count?code=pp1CVOkbLtNwHhCMdkxIb6PlC50U0iCjGPrR4kRijLpuAzFurk_KBQ%3D%3D';

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