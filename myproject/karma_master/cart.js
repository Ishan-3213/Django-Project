var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.item_id
        var action = this.dataset.action
        console.log('productId:',item_id,'action:',action)

        console.log('User:',user)
    })
}

// function getCookie(update-cart) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, update-cart.length + 1) === (update-cart + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(update-cart.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');
// console.log(csrftoken)