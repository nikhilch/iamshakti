function success() {
    console.log("Data submitted successfully :)");
}

function error(err) {
    console.log("There was an error :(");
}

function send_jtm(data) {
    var xhr = new XMLHttpRequest();
    xhr.onload = success;
    xhr.onerror = error;

    xhr.open('POST', '/api/jtm/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


    xhr.send(JSON.stringify(data));
}

function jtm_member() {

    var data = {
                    "firstName": document.getElementById('firstName').value,
                    "lastName": document.getElementById('lastName').value,
                    "email": document.getElementById('emailAddr1').value,
                    "interests": document.getElementById('interests').value,
                    "memberType": "ME"
               }
    send_jtm(data);
}

function jtm_gen_ally() {
    var data = {
                    "email": document.getElementById('emailAddr2').value,
                    "memberType": "GA"
               }
    send_jtm(data);
}
