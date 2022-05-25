// console.log("Hello, World!");
var updateBtns = document.getElementsByClassName('update-cart')
// console.log(updateBtns);

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        // console.log("You clicked on button");
        var productId = this.dataset.product
        var action = this.dataset.action

        if (user == 'AnonymousUser') {
            console.log("You are not logged in");
        }
        else {
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action) {
    console.log("Product Added", productId, action);
    var url = '/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data);
            location.reload()
        })
}