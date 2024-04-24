function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
       const cookies = document.cookie.split(';');
       for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
          }
       }
    }
    return cookieValue;
 }

 const csrftoken = getCookie('csrftoken');
 const BASE_URL = 'http://127.0.0.1:8000/api';

 $('#add-todo').show();
        $('#edit-todo').hide();

 function loadTaskList(){
    fetch(BASE_URL + '/task-list/')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);

        let item_wrap = document.getElementById('item-wrap');
        item_wrap.innerHTML = '';  
        var htmlData = ''; 
        data.forEach((item) => {
            var check = item.completed ? 'checked' : '';
            htmlData += `
            <div class="item">
                <input type="checkbox" ${check} onchange="updateState(this)" data-id="${item.id}" >
                <div class="title" onclick="setModalData(${item.id})" data-bs-toggle="modal" data-bs-target="#exampleModal" type="button">${item.title}</div>
                <div class="icon-1" onclick="setUpdateData(${item.id})"><i class="bi bi-pencil-square"></i></div>
                <div class="icon-2" onclick="confirmation(${item.id})"><i class="bi bi-trash-fill"></i></div>
            </div>`;
        });
        item_wrap.innerHTML = htmlData;
    });
 }

 loadTaskList();

 function addNewListItem(){
    let title = document.getElementById('title').value;
    let description = document.getElementById('description').value;

    fetch(BASE_URL + '/task-create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'title': title,
            'description': description,
        })
    })
    .then((response) => console.log(response))
    .then((data) => {
        console.log(data);
        loadTaskList();
        $('#title').val('');
        $('#description').val('');
    });
 }

function confirmation(id){
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
          deleteListItem(id);
        }
      });
}

 function deleteListItem(id){
    fetch(BASE_URL + '/task-delete/' + id + '/', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    })
    .then((response) => console.log(response))
    .then((data) => {
        console.log(data);
        loadTaskList();
    });
 }

function setUpdateData(id){
    fetch(BASE_URL + '/task-details/' + id + '/')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        document.getElementById('title').value = data.title;
        document.getElementById('description').value = data.description;
        $('#add-todo').hide();
        $('#edit-todo').show();
        document.getElementById('edit-todo').setAttribute('data-id', data.id);//set data-id attribute
    });
 }

function updateListItem(){
    let id = document.getElementById('edit-todo').getAttribute('data-id');
    let title = document.getElementById('title').value;
    let description = document.getElementById('description').value;

    fetch(BASE_URL + '/task-update/' + id + '/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'title': title,
            'description': description,
        })
    })
    .then((response) => console.log(response))
    .then((data) => {
        console.log(data);
        loadTaskList();
        $('#add-todo').show();
        $('#edit-todo').hide();
        $('#title').val('');
        $('#description').val('');
    });
 }

function updateState(ele){
    let id = ele.getAttribute('data-id');
    
    let state = ele.checked;
console.log(state)
    fetch(BASE_URL + '/task-update/' + id + '/', {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
           'completed': state
        })
    })
    .then((response) => console.log(response))
    .then((data) => {
        console.log(data);
    });
 }

 function setModalData(id){
    fetch(BASE_URL + '/task-details/' + id + '/')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
       $('#exampleModalLabel').html(data.title);
       $('#modal-description').html(data.description);
       const datetime = new Date(data.created);
       const formatted = datetime.toLocaleString();
       $('#modal-date').html(formatted);

    });
 }