function success() {
    console.log("Data submitted successfully :)");
}

function error(err) {
    console.log("There was an error :(");
}

function jtm_member() {
    var xhr = new XMLHttpRequest();
    xhr.onload = success;
    xhr.onerror = error;

    var data = {
                    "firstName": document.getElementById('firstName').value,
                    "lastName": document.getElementById('lastName').value,
                    "email": document.getElementById('emailAddr1').value,
                    "interests": document.getElementById('interests').value,
                    "memberType": "ME"
               }

    xhr.open('POST', 'http://127.0.0.1:8000/api/jtm/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


    xhr.send(JSON.stringify(data));
}

function jtm_gen_ally() {
    var xhr = new XMLHttpRequest();
    xhr.onload = success;
    xhr.onerror = error;

    var data = {
                    "email": document.getElementById('emailAddr2').value,
                    "memberType": "GA"
               }

    xhr.open('POST', 'http://127.0.0.1:8000/api/jtm/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


    xhr.send(JSON.stringify(data));
}
