/**
 * A handler function to prevent default submission and run our custom script.
 * @param  {Event} event  the submit event triggered by the user
 * @return {void}
 */

 let activities = [];
 const handleFormSubmit = event =>{
 	//собирать данные из формы
 	event.preventDefault();
 	let activity ={
 		id: Date.now(),
 		actName: document.getElementById("nameactivity").value,
 		time: document.getElementById("time").value,
 		date: document.getElementById("date").value,
 		address: document.getElementById("inputAddress").value,
 		group: document.getElementById("group").value,
 	}

 	//подключается к серверу
    let xhr = new XMLHttpRequest(); 
    let url = "./"; 
        
    // POST
    xhr.open("POST", url, true); 
    xhr.setRequestHeader("Content-Type", "application/json"); 
    xhr.onreadystatechange = function () { 
        if (xhr.readyState === 4 && xhr.status === 200) { 
  
            Print received data from server 
            result.innerHTML = this.responseText; 
  
        } 
    };

    //помещает данные в константу
 	activities.push(activity);
 	document.forms[0].reset();

 	console.warn('added', {activities});
 	let pre = document.querySelector("#msg pre");

 	//создать JSON
 	var data = JSON.stringify(activities);
 	localStorage.setItem('ActivitiesList',data);
 	var data2 = "'"+data+"'";
 	console.log(data2);
 	// отрправлять JSON в сервер
    xhr.send(data2);
    const disp_act = document.querySelector('#display');
    document.getElementById("display").innerHTML = data; 
    

    //ТАБЛИЦА

    // принимает имя значения данных в список
        var col = [];
        for (var i = 0; i < activities.length; i++) {
            for (var key in activities[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }
        console.log(col)
        
    // создает таблица
        var table = document.createElement("table");
        table.setAttribute('class','table');
        // Rows
        var tr = table.insertRow(-1);                   
        // Headers
        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");      
            th.innerHTML = col[i];
            tr.appendChild(th);
        }
       
         // заполняет таблицу данными JSON
        for (var i = 0; i < activities.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = activities[i][col[j]];
            }
        }

        // создает таблица в index.html
        var divContainer = document.getElementById("createTable");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
 
 }
//функция активируется при нажатии кнопки
 document.addEventListener('DOMContentLoaded', ()=>{
 	document.getElementById('button').addEventListener('click', handleFormSubmit);
 });
